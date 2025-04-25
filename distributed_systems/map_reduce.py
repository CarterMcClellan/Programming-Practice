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