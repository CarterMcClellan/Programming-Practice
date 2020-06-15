# Programming Practice

## Data Structures and Algorithms
During an interview you get 2 things
```
- A data structure
- Some question relating to that data structure
```
Or you get
```
- Some question asking you design some data structure
```

Algorithms and Data Structures in the interview process look something like this
```
(question, data structure) ---- (problem solving) ----> (correct algorithm, data structure)
```
The difficulty therefore arises from devising the correct algorithm in the amount of time alloted, and the goal of practice is therefore to expedite the rate at which one devises this algorithm. 

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

## Trivia
The more you know about Python the easier it is to work with. Knowing Python breaks up into a couple different pieces
```
trivia
├── fundamentals
├── numerical
├── standard lib
└── web
```

### Fundamentals
Fundamentals are the core concepts we use every day when working with python,
```
trivia/fundamentals/
├── Compilation
├── Constants
├── Data Structures
│   ├── Dict
│   ├── List
│   └── Set
├── Datatypes
├── Decorators
├── Functions
├── Loops
├── OO
└── Operators
```

### Numerical
Numerical are all the libraries that are used for data science, data engineering, machine learning, and deep learning
```
trivia/numerical/
├── Jupyter
├── Matplotlib
├── Numpy
├── Pandas
├── PyTorch
└── Scipy
```

### Standard Lib
Standard Lib is a subset of the most important libraries from the the python standard lib
```
trivia/standard lib/
├── Data Types
├── Functional
├── Math
└── Text Processing
```

### Web
Web is all the frameworks used in web development (might want to add requests, and json from the standard lib to this list)
```
trivia/web/
├── angular
├── d3
├── django
├── flask
└── react
```
