# Programming Practice

## Data Structures and Algorithms
During an interview you get 2 things
```
- A data structure
- Some question asking you design some data structure
```

Thus the usage of Algorithms and Data Structures in the interview process look something like this
```
(question, data structure) ---- (problem solving) ----> (correct algorithm, correct data structure)
```
The difficulty therefore arises from devising the correct algorithm in the amount of time alloted, and the goal of practice is therefore to expedite the rate at which one devises this algorithm. Which in part boils down to some pattern recognition and memorization.

To start solving this we need some kind of decision tree to show how one gets from (question, data structure) to (correct algorithm, data structure). Based on my experience with leetcode that looks something like

```
(question, data structure)
├── if data structure equals Array, then Algorithm is likely
│   ├── Binary Search
│   ├── Divide and Conquer
│   ├── Dynamic Programming
│   └── Sorting
├── if data structure == Graph, then Algorithm is likely
│   ├── A Star
│   ├── Bellman Ford
│   ├── Bfs
│   └── Dijkstra
├── ...
```
