import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for j in range(trials):
    calendar = [0] * days

    for a in range(people):
        found = False
        bday = random.randint(0, days-1)
        calendar[bday] += 1
        if calendar[bday] > 1:
            matches += 1
            found = True
        if found == True:
            break
    
percentage = (matches / trials) * 100

print(f'{percentage:0.4f}')