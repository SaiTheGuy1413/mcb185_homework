import sys
import math

count = 0
inp = sys.argv[1:]
for i in inp:
    count += 1

minval = inp[0]
maxval = inp[0]
for i in inp:
    if i > maxval:
        maxval = i
    if i < minval:
        minval = i

total = 0
mean = 0
sd = 0
for i in inp:
    total += float(i)
mean = total / count
sdtotal = 0
for i in inp:
    sdtotal += ((float(i) - mean) ** 2)
sd = math.sqrt(sdtotal/count)


sorted_list = sorted(inp)
median = 0
if  count % 2 != 0:
    median = inp[round(count/2)]
else:
    median = ((float(inp[count/2])) + float(inp[(count/2)+1])) / 2

print(inp)
print('Total amount of numbers is: ' + str(count))
print('Max and min value are: ' + str(maxval) + ' and ' + str(minval))
print('Mean and standard deviation are: ' + str(mean) + ' and ' + str(sd))
print('Median is: ' + str(median))