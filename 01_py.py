#Emma Buller
#SoftDev
#K05 -- Refactoring
# 2021--9--26

import random
pd1 = ["emma","shriya","william","aaron"]
pd2 = ["andrew", "yuqing","michael"]

def printName():
    period = input('Pick a period (Input 1 or 2): ')
    if period == '1':
        print(pd1[random.randint(0,len(pd1)-1)])
    elif period == '2':
        print(pd2[random.randint(0,len(pd2)-1)])
    else:
        print("This input goes against the rules")
        printName()
    
