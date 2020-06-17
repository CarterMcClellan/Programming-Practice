## strings

### Declaration
Strings can be declared with '', "", ''', or """. Inside "" words can be quoted with '', and vice versa. ''' or """ have the same functionality but can span multiple lines, for example
```python
'''
This comment
will run 
across 3 "lines"
'''
```

Strings can also be created out of other objects using the str constructor

### strings are immutable
Strings are immutable in python. When an existing string is modified, that actually creates an all new object in memory. 
```python
>>> a = "cat"
>>> id(a)
4430540224
>>> a += " in the hat"
>>> a
'cat in the hat'
>>> id(a)
4430912304
```
Another example with methods
```python
>>> def assign_new_val(n):
...     n = "dog"
... 
>>> g = "cat"
>>> assign_new_val(g)
>>> print(g)
cat
```

### string representation
Strings can be enocded in 3 different formats (each requiring a different numbers of bits). Latin-1 encodings require 1 bit to encode a character, UCS-2 requires 2 bits, and UCS-4 requires 4 bits. 

```python
>>> import sys
>>>
>>> string = "H"
>>> sys.getsizeof(string + '?')- sys.getsizeof(string)
1
>>>
>>> string = "©"
>>> sys.getsizeof(string + '®') - sys.getsizeof(string)
2
>>>
>>> string = '🐍'
>>> sys.getsizeof(string + '💻')- sys.getsizeof(string)
4
```

As a result memory allocation of strings in python can be complicated. Trying to slice a string with variable length bits could be disastorous and as a python must change the encoding of an entire string when a new encoding format is introduced.

```python
>>> import sys
>>> string = "a"
>>> sys.getsizeof(string + '💻') - sys.getsizeof(string)
34
>>> sys.getsizeof(string + '💻')
84
>>> sys.getsizeof(string)
50
>>> string = "abc"
>>> sys.getsizeof(string)
52
```

### string interning
As established in the above strings can take up a lot of memory, so python has to make some optimizations to avoid running out of that memory. The process *string interning* is pretty simple, under a particular set of conditions python will store that string in memory so that a new object does not have to be created with the same value. Hence why 

```python
>>> a = "foo"
>>> b = "foo"
>>> id(a) == id(b)
True
```

Note however that strings can only be interned under a particular set conditions 
- string must be a compile time constant
- string must consist of ascii letters digits and underscores.
```python
>>> id("".join(["f", "o", "o"])) is id("foo")
False
```

### raw strings


### references
- https://github.com/satwikkansal/wtfpython#-strings-can-be-tricky-sometimes
- https://medium.com/@bdov_/https-medium-com-bdov-python-objects-part-iii-string-interning-625d3c7319de