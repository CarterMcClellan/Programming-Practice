import re
from glob import glob
import os

def rename(my_string):
    # zero pad all double digit numbers with 1 zero
    my_string = re.sub(r"(\b\d\d\b)", r"0\1", my_string)

    # zero pad all single digit numbers with 2 zeros
    my_string = re.sub(r"(\b\d\b)", r"00\1", my_string)
    return my_string

for fname in glob("*.ipynb"):
    os.rename(fname, rename(fname))
