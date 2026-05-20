import random

def deathsaves():
    s = 0
    f = 0
    while s < 3 and f < 3:
        score = random.randint(1,20)
        if score == 1:
            f += 2
        elif score == 20:
            return 'LIVED'
        elif score >= 10:
            s += 1
        else:
            f += 1
    if s >= 3:
        return 'STABLE'
    else:
        return 'DIED'

for i in range(10):
    print(deathsaves())