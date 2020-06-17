## numpy floats vs python floats
Under the hood, numpy uses C doubles for its float64 datatypes, thus np.float64 should be exactly the same as float

```python
>>> np.float64(.1) == float(.1)
True
```
Note however that this is not true for less precision
```python
>>> np.float32(.1) == float(.1)
False
```
(Unless the digit is finite)
```python
>>> np.float32(.5) == float(.5)
True
```


## References
- https://numpy.org/devdocs/user/basics.types.html