# Memory Blocks
In the second volume of the Python for Data Analysis series its stated
```
"NumPy internally stores data in a contiguous block of memory, independent of
other built-in Python objects. NumPy’s library of algorithms written in the C lan‐
guage can operate on this memory without any type checking or other overhead.
NumPy arrays also use much less memory than built-in Python sequences." - 
```

Lets unpack this, 
- How does python handle sequence data types? How is numpy different?
- How are Contiguous Blocks of Memory used?

## 