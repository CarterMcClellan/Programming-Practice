## Reason for being
Ctypes is efficient for using simple C function in the Python runtime, but as they get more complex ctypes can be cumbersome to use.

Thus there are several tools which we can use to make things easier. 

## Def. Binding
A binding is an application programming interface (API) that provides glue code specifically made to allow a programming language to use a foreign library or operating system service (one that is not native to that language).

## CFFI (C foreign function interface)
CFFI is a methodology to automate the process of building bindings between C and Python. 

The CFFI has a mode called *API mode* which is used to generate the python module from the C using a C compiler. 

Inside of the *API mode* there is additional functionality in that we can choose whether we want to build the python module once (*out of line mode*), or every time the program runs (*in line mode*)


## Installation
```bash
pip install cffi
```

## Usage
CFFI is different than ctypes, you are creating a full python module. This means that there several steps
- Write python code to describe the bindings
- Run code to generate a loadable module
- Modify code to import the loadable module

### Writing the Bindings
This all starts with an FFI object
```python
import cffi
ffi = cffi.FFI()
```

With this FFI object you can automatically process C header files
```python
h_file_name = "cmult.h"
with open(h_file_name) as h_file:
    ffi.cdef(h_file.read())
```

## References
- https://en.wikipedia.org/wiki/Language_binding
- https://realpython.com/python-bindings-overview/