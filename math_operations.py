# Divison
a = 1
b = 2
c = 4
d = 2.5
print(c / b)
print(a / b)
print(d / a)

from operator import truediv
print(truediv(b, a))

# Addition
print(a + b)
# Using the "in-place" "+=" operator to add and assign
e = 5
e += b
print(e)

import operator
print(operator.add(e, a))

# Exponentation
exp = 2 ** 3
print(exp)
exp2 = pow(2, 3)
print(exp2)

import math
exp3 = math.pow(2, 3)  # (always float; does not allow complex results)
print(exp3)

# sqrt
num = 4
sqnum = (math.sqrt(c))  # (always float; does not allow complex results)
print(sqnum)

# Subtraction
sub = e - b
print(sub)
sub = operator.sub(e, b)
print(sub)

# Multiplication
multi = b * c
print(multi)
multi = operator.mul(b, c)
print(multi)

# Modules
print(6 % 4)
print(3 % 4)
print(operator.mod(6, 4))
print(operator.mod(3, 4))
