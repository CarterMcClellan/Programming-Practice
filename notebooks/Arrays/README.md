## Arrays

### Array Algorithms
|                     | Runtime Complexity     | Function                        |
|---------------------|------------------------|---------------------------------|
| Binary Search       | O(log N)               | Find single element             |
| Divide and Conquer  | O(log N) or O(N log N) | Break Array into smaller Arrays |
| Dynamic Programming | O(N) or O(N^2)         | Maximize/ Minimize              |
| Windowing           | O(N) or O(N^2)         | Array Subsets                   |
| Hashing             | O(N)                   | Count Array                     |
| Bit Manipulation    | O(N)                   | Identify Unique Elements        |
| Generation          | O(2^N)                 | Generate all subsets            |


### Complexity
|          | Complexity | Alternatives |
|----------|------------|--------------|
| append   | O(N)       | heapq        |
| insert   | O(N)       | heapq        |
| pop last | O(1)       | heapq        |
| sort     | O(N log N) | sorted       |
| reverse  | O(N)       | reversed     |
| copy     | O(N)       | deep copy    |
| in       | O(N)       |              |
| min, max | O(N)       |              |
| len      | O(1)       |              |

### Intuition
- Maximize/ Minimize = Dynamic Programming
- Generate = Backtracking/ Dfs
- Subarray = Windowing/ Prefix Sum