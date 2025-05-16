# Implement a simplified version of the map-reduce pattern for word counting.
# 
# Your implementation should include:
# 1. A `map` function that takes a document and outputs (word, count) pairs
# 2. A `shuffle` function that groups the output by key
# 3. A `reduce` function that aggregates the counts for each word
# 
# Your solution should:
# - Work with a stream of text documents
# - Be memory efficient (don't load all documents into memory)
# - Support parallel processing of documents
# - Handle large volumes of text
# 
# Example usage:
# documents = ["hello world", "world of programming", "hello programming"]
# result = map_reduce(documents, map_fn, shuffle_fn, reduce_fn)
# Result should be: {"hello": 2, "world": 2, "of": 1, "programming": 2}

import random, uuid, os, json
from typing import Callable, Generator
import multiprocessing as mp

def map_reduce(documents: Generator, 
               map_fn: Callable, 
               shuffle_fn: Callable, 
               reduce_fn: Callable
    ) -> dict[str, int]:
    with mp.Pool(4) as p:
        map_results = p.map(map_fn, documents)
      
    shuffle_results = shuffle_fn(map_results)
    counts = reduce_fn(shuffle_results)
    return counts

def fake_generator():
    random_words = ["foo", "bar", "hello", "world"]
    for _ in range(10):
      doc = []

      for _ in range(1000):
          doc += [random.choice(random_words)]

      yield doc

def map_fn(document: list[str]) -> str:
    """counts all the words in a document"""
    mapper_id = uuid.uuid1()
    cnts = {}
    for word in document:
        cnts[word] = cnts.get(word, 0) + 1

    data = list(cnts.items())
    f_out = f"{mapper_id}.txt"
    with open(f_out, "w") as f:
        f.write(json.dumps(data))

    return f_out

def shuffle_fn(map_outputs: list[str]) -> dict[str, list[int]]:
    """group output by key for all maps"""

    # this should be an on-disk key value (something like rocksdb)
    # which handles spill (otherwise we are holding) all the shuffle
    # data in memory at once (which is no bueno for large datasets)
    grouped = {} 

    for fname in map_outputs:
        with open(fname, "r") as f:
            data = json.loads(f.read())
          
        for (word, count) in data:
            grouped[word] = grouped.get(word, []) + [count]

        # delete the mapper file after we have removed it
        os.remove(fname)
      
    return grouped

def reduce_fn(shuffle_outputs: dict[str, list[int]]) -> dict[str, int]:
    """aggregate the count for each word (this should be across all words)"""
    result = {}

    # we would want to iterate through each of the key/ value pairs in the 
    # ondisk kv store rather than load the entire dictionary into once like 
    # this.
    for word in shuffle_outputs:
        result[word] = sum(shuffle_outputs[word])
      
    return result

document_generator = fake_generator()