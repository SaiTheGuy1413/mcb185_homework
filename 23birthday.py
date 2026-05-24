import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for i in range(trials):
    bdays = []
    for k in range(people):
        bdays.append(random.randint(0, days))


    for j in range(len(bdays)):
        found = False
        for b in range(j+1, len(bdays)):
            if bdays[j] == bdays[b]:
                matches += 1
                found = True
        if found == True:
            break

percentage = (matches / trials) * 100

print(f'{percentage:0.4f}')