#10demo.py by sai

import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2**3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
#print(1 / 0)           # divide by zero error
#print(math.log(0))     # math domain error
#print(math.sqrt(-1))   # math domain error

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

hyp = pythagoras(3,4)
print(hyp)

#simpler version
def hypontenuse(a,b):
    return math.sqrt(a**2 + b**2)

print (hypontenuse(3,4))