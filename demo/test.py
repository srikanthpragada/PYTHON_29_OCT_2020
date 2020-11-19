import sys

sys.path.insert(0, r'c:\classroom\oct29\demo\mylib')
print(sys.path)

import number_funs
import number_funs as nf
from number_funs import iseven

print(number_funs.PI)
print(number_funs.iseven(10))
print(nf.iseven(11))
print(iseven(10))

print(dir(nf))
help(iseven)
#print(iseven.__doc__)  # Print documentation of iseven
