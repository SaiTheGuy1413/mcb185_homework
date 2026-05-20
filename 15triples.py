import math

for i in range(1, 100):
    for k in range(i, 100):
        n = math.sqrt(i ** 2 + k ** 2)
        if n % 1 == 0:
            print(i, k, int(n))
