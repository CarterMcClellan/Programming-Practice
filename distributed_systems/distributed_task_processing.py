# Implement a function `process_batch` that simulates processing a batch of tasks in parallel.
# 
# The function takes:
# - tasks: List of task IDs (integers)
# - num_workers: Number of available worker threads
# - process_time: A function that returns the processing time for a given task ID
# 
# Your function should:
# 1. Distribute the tasks among workers optimally to minimize total completion time
# 2. Return the total time to complete all tasks and which worker processed each task
# 3. Handle the case where there are more tasks than workers
# 
# Example:
# Input: tasks = [1, 2, 3, 4], num_workers = 2, process_time(task_id) returns [10, 5, 7, 8]
# Output: (15, {1: [1, 2], 2: [3, 4]}) # Total time: 15, Worker 1 processes task 1, Worker 2 processes tasks 2, 3, and 4
from typing import Callable

# Implement a function `process_batch` that simulates processing a batch of tasks in parallel.
# 
# The function takes:
# - tasks: List of task IDs (integers)
# - num_workers: Number of available worker threads
# - process_time: A function that returns the processing time for a given task ID
# 
# Your function should:
# 1. Distribute the tasks among workers optimally to minimize total completion time
# 2. Return the total time to complete all tasks and which worker processed each task
# 3. Handle the case where there are more tasks than workers
# 
# Example:
# Input: tasks = [1, 2, 3, 4], num_workers = 2, process_time(task_id) returns [10, 5, 7, 8]
# Output: (15, {1: [1, 2], 2: [3, 4]}) # Total time: 15, Worker 1 processes task 1, Worker 2 processes tasks 2, 3, and 4

# ok so we are trying to gauge how long it will take to complete these tasks
#
# proc 1 (free), proc 2 (free)
#   task 1, task 2 come in
#
# proc 1 (10), proc 2 (5)
#   5 minutes go by
#
# proc 1 (5), proc 2 (free)
#   task 3 comes in
# 
# proc 1 (5), proc 2 (7)
#   5 minutes go by
#
# proc 1 (free), proc 2 (2)
#   task 4 comes in 
#
# proc 1 (8), proc 2 (2)
#   2 minutes go by
# 
# proc 1 (6), proc 2 (free)
#   no more new tasks. 6 minutes go by
#
# proc 1 (free), proc 2 (free)
#
# total time spent 18 minutes
#
# Output: (18: {1: [1, 3], 2: [2, 3]})

# algorithmically this looks a bit like a min heap. 
# we take the first (n_workers) tasks we enque them into a heap.
# [10, 5]
# 
# we pop the min (5), we decrement all values in the heap by 5
# (this should not actually interfere with the heaps internal ordering
# if we uniformly subtract then the values should still be in order)
#
# we enqueue the next task (7)
# [5, 7]
#
# we pop the min (5), we decrement all values in the heap by 5
# 
# we enqueue the next task
# [2, 8]
#
# if we wanted to modify this st. we process in the optimal ordering (assuming
# we know how long each tasks is going to take before processing then we could 
# sort by process time in descending order).

from typing import Callable
import heapq as hq

def process_batch(tasks: list[int], num_workers: int, process_time: Callable[[int], int]):
    active_procs = []
    for _ in range(num_workers):
        to_add = tasks.pop()
        active_procs.append(process_time(to_add))
    
    hq.heapify(active_procs)
    ans = 0
    while active_procs:
        curr = hq.heappop(active_procs)
        ans += curr
        active_procs = [p-curr for p in active_procs]

        # add next task to queue
        if tasks:
            next = tasks.pop()
            tt = process_time(next)
            hq.heappush(active_procs, tt)

    return ans

task_ids = [1, 2, 3, 4]
process_map = {
    1: 10, 
    2: 5, 
    3: 7, 
    4: 8
}

num_workers = 2
process_time = lambda x: process_map.get(x)

process_batch(task_ids, num_workers, process_time)