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

print(hypontenuse(3,4))

#F to C conversion

def ftoc(temp):
    return (temp - 32) * (5/9)

cel = ftoc(50)
print(cel)

#MPH to KPH conversion

def speedcon(mph):
    return mph * 1.609

kph = speedcon(10)
print(kph)

#Distance between two points

def dist(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

points = dist(3,2,5,-1)
print(points)