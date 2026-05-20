import random

#dc = difficulty class (can be 0-20)
#adv = advantage (can be 1 or -1 or 0)

def savthrow(dc, adv):
    if adv == 1:
        fd = random.randint(1,20)
        sd = random.randint(1,20)
        score = max(fd,sd)
    elif adv == -1:
        fd = random.randint(1,20)
        sd = random.randint(1,20)
        score = min(fd,sd)
    else:
        score = random.randint(1,20)
    if score >= dc:
        return 'Success'
    else:
        return 'Failed'
    
for i in range(10): 
    print(savthrow(5,-1))
    print(savthrow(10,-1))
    print(savthrow(15,1))