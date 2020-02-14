### Array Algorithms
- Windowing
	- Use 2 pointers to study various contiguous subsets of the array
- Dynamic Programming
	- Use external memory to store additional information about an array. Usually we can use this previous memory to infer something about the current index in our iteration. Eg, Fibonacci, Kadane's Algorithm.
- Generation
	- Given an array build some kind of recursive algorithm to study various permtutations of that array or its subarrays.
	- Note that this algorithm usually has exponential complexity, so we have to be aware of input size, and of loop alternatives (which are usually superior as they only have polynomial time complexity)
- Binary Search
	- Given a sorted array, find the first index of a given target element.
- Hashing
	- This applies when the problem pertain to duplicates. Eg, count the most common letters accross strings, compute the average score of various students etc...
- Bit Manipulation
	- Useful for studying patterns in Strings or in integers. Eg, find the only non-duplicate element in a string/list in O(N) time with O(1) memory (just XOR all the elements together).
- Divide and Conquer
	- If the problem can be divided into smaller sub-contexts, eg, find peaks, merge sort.

### Insight
#### Sums and Products
- If we want to find a (contiguous) sum which is precisely equal to something then its hashing problem. 
- If we want to find a non-contiguous sum which is equal to or close to something, then its a left and right pointer problem. If we want to find a contiguous sum which is greater than something this can also be a windowing problem.
- If we want to try and maximize the sum or the product, then its a dynamic programming problem.

#### Log(n)
- If a problem has log(n) runtime complexity and its a list and its sorted its probably binary search.
- If a problem has log(n) runtime complexity and its a list and its not sorted the best guess is Divide and Conquer.
