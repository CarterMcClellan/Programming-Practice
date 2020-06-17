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

### memory representation
Like a integer a float has a pointer to the object type, size, and reference count. Unlike an integer floats have a maximum precision value. The remaining 8 bits go to holding a double in the C runtime.

### overflow errors and IEEE 754 quirks

```python
>>> x = 1.7976931348623157e+308
>>> x
1.7976931348623157e+308
>>> x * 10
inf
>>> x ** x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Result too large')
```

The underlying C code here is somewhat inconsistent. The ** operator will call the pow function, which in this case handles overflow differently than the * operator. 

- \* calls the the C language mul function for doubles, this function has been written to abide by IEEE 754 standards and is expected to throw an infinity
- ** or pow is defined in python, does not have a prewritten standard to meet and throws a OverflowError
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

Note that this issue appears again when dealing with rounding. For example
```
>>> a
13.949999999999999
>>> round(a, 2)
13.949999999999999
```

### more on floating point representation
How does one find the representation for .1 in binary? Python abides by IEEE-754 convention, therefore on input, the computer strives to convert .1 to a fraction of the form J/(2**N), where J is an integer 53 bits of precision. 

```
.1 ~= 2**53/2**N 
```
Some simple algebra gives us N ~= 56 
```
.1 ~= 2**53/2**56
```

## complex

### construction
The complex method acts as a constructor and can be used to construct complex numbers in a couple of different ways
```python
>>> complex('1+2j')
(1+2j)
>>> complex(1, 2)
(1+2j)
>>> complex(1+2j)
(1+2j)
>>> 1+2j
(1+2j)
```

### memory representation
Underneath the real and imaginary components of a complex number are each floats. Therefore the size of the underlying is equal to the object type, size, and reference count. With the remaining 2 values being 2 doubles in C. 

Note that with this comes some of the same floating point quirkiness we have seen already
```python
>>> complex(.1, .1) + complex(.2, .2)
(0.30000000000000004+0.30000000000000004j)
>>> .1 + .2
0.30000000000000004
```


# References
- https://stackoverflow.com/questions/23016610/why-do-ints-require-three-times-as-much-memory-in-python
- https://stackoverflow.com/questions/40344159/understanding-memory-allocation-for-large-integers-in-python
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- https://www.programiz.com/python-programming/numbers
- https://docs.python.org/3/tutorial/floatingpoint.html
- https://stackoverflow.com/questions/46432189/python-how-come-a-large-float-turns-into-inf-automatically