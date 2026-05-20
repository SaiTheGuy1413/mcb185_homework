fv = 0
sv = 1 
for i in range(10):
    fibo = fv + sv
    print(fv)
    fv = sv
    sv = fibo