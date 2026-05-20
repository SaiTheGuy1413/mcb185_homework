import math
import random

def triangle(n):
    ans = 0
    if n <= 0 or n % 1 > 0:
        return None
    else:
        for i in range(1, n+1):
            ans = ans + i
        return ans
        
#print(triangle(4))

def factorial(n):
    ans = 1
    if n < 0 or n % 1 > 0:
        return None
    else:
        for i in range(1, n+1):
            ans = ans * i
        return ans

#print(factorial(4))

def poisson(n, k):
    if n <= 0 or k < 0 or k % 1 > 0:         
        return None   
    prob = (n ** k) * (math.e ** -n) / factorial(k)
    return prob

#print(poisson(2, 3))

def nchoosek(n, k):
    if n <= 0 or k < 0 or k % 1 > 0:
        return None
    ans = factorial(n) / (factorial(k) * (factorial(n-k)))
    return ans

#print(nchoosek(2, 3))

#random.seed(1)
#print(random.randint(1,6))