## Arrays are Pointers

```python
>>> import numpy as np
>>> l = np.array(range(1, 10, 2))
>>> l
array([1, 3, 5, 7, 9])
>>> c = l[1:3]
>>> c[1] = 50000
>>> l
array([    1,     3, 50000,     7,     9])
```

Note the distinction from normal python
```python
>>> l = list(range(1, 10, 2))
>>> c = l[1:3]
>>> c[1] = 5000
>>> l
[1, 3, 5, 7, 9]
```

## Fancy Indexing
```python
>>> l = [[row_num for _ in range (4)] for row_num in range(10)]
>>> np_l = np.array(l)
>>> np_l
array([[0, 0, 0, 0],
       [1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4],
       [5, 5, 5, 5],
       [6, 6, 6, 6],
       [7, 7, 7, 7],
       [8, 8, 8, 8],
       [9, 9, 9, 9]])
>>> np_l[[4, 3, 1]]
array([[4, 4, 4, 4],
       [3, 3, 3, 3],
       [1, 1, 1, 1]])
```

```python
>>> l = np.arange(32).reshape(8, 4)
>>> l
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])
>>> l[[1, 2, 5],[3, 3, 3]]
array([ 7, 11, 23])
```