## About
Ctypes is a a foreign function library defined in the python standard library. It allows you to load a dynamic link library and call functions on these libraries from Python.

Meaning that  it is a library which exists to help send objects between C and Python, the premise being that C code is more performant than Python code. Sending objects between C and Python has several considerations.

## Consideration 1 Marshalling
The python and C memory footprint for objects is different. In C an unsigned int might only be 8 bits, but in python everything starts its life as an object (see fundamentals/datatypes), meaning that even an integer will occupy several bytes.

Thus if a C program uses an integer, to pass that integer to python it will need to be converted into a python object
```
uint_8 -> Py_Obj -> int
```

## Consideration 2 Mutability
In python certain data types are mutable, certain data types are immutable.

In C you can either pass a pointer to the object (pass by reference), or a copy of the object (pass by value).

As a result, you cannot modify immutable objects when dealing with them in C.

## Consideration 3 Memory Managment
Pointers need to be freed in C, this means that you have to remember to include this in your python bindings.

## References
- https://realpython.com/python-bindings-overview/
- https://stackoverflow.com/questions/10202306/python-bindings-how-does-it-work#:~:text=%22Bindings%22%20are%20implemented%20either%20as,%2Dplate%22%20code%20or%20Boost.