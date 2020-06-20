## Compilation is Implicit
Compilation inside of python is implicit! When you run the script

```bash 
python script.py
```

That script is automatically compiled into byte codes which can be interpreted by the python virutal machine, then those byte codes are executed by some interpreter.

Note how this is different from a compiled language like c, where the compilation process is explicit (you first compile, then you execute the machine code).

This behavior is what makes python seem like an interpreted language! Each time a statement is typed into a REPL or a Jupyter Notebook, the language acts like an interpreted language, much like bash or something we are used to seeing on the command line.

But each statement is actually compiling out to bytecode then being executed on a python virtual machine.

## just in time (jit) compilation (pypy) 
Using pypy python is compiled directly into machine level code. 

