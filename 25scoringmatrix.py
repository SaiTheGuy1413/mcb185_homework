import sys

alphabet = sys.argv[1]
mat = sys.argv[2]
mismat = sys.argv[3]

print(' ', end = '')
for char in alphabet:
    print(f'{char:>3}', end = '')
print()

for row in alphabet:
    print(row, end = '')
    for col in alphabet:
        if row == col:
            print(f'{mat:>3}', end = '')
        else:
            print(f'{mismat:>3}', end = '')
    print()
