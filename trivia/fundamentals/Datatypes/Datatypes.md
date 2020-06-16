# Data Types in Python
Datatypes are interesting in python. The language features dynamic typing, so its not always something at the forefront of a python developers mind, but there is a tremendous amount of variability. 

## The Basics
People familiar with python already know about which data types are present
- int, str, float
- list, tuple, range
- dict, set
Less common usecases might involve
- bool, bytes, bytearray, complex, frozenset, memoryview

## int

### int memory allocation
Ints have unlimited precision in python. From a memory allocation perspective this has some pretty interesting implications.

All integers start their lives as a C struct

```c
struct _longobject {
    PyObject_VAR_HEAD
    digit ob_digit[1];
};
```

*digit* holds the numeric value of the integer (15-30 bits in length depending on your OS), *PyObject_VAR_HEAD* holds the size of the object, the type of the object (in this case int), and the number of references to that object (or "reference count"), (note that this is important to the python garbage collector).

To handle a precision increase, python will allocate a new chunk of memory, adding a new digit object to the array. 

### int division
Despite the fact that the "//" operator is also called *integer division*, the result is not the same as a casting the result of a division to an integer or "int(/)".

```python
>>> int(1/(-2))
0
>>> (-1)//2
-1
```

this is because "//", will always round towards negative infinity.


## float

### binary precision tricky-ness

```python
>>> print( (1.1 + 2.2) == 3.3 )
False
```

Why? Because 0.1 has no finite binary representation. As a result

```python
>>> 1.1 + 2.2
3.3000000000000003
```

This is why the decimal Module exists in python, to get around issues like this
```
>>> from decimal import Decimal as D
>>> D('.1') + D('.2') == D('.3')
True
```


# References
- https://stackoverflow.com/questions/23016610/why-do-ints-require-three-times-as-much-memory-in-python
- https://stackoverflow.com/questions/40344159/understanding-memory-allocation-for-large-integers-in-python
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- https://www.programiz.com/python-programming/numbers