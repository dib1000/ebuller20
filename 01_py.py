#Emma Buller
#SoftDev
#K05 -- Better Living Through Amalgamation
# 2021-9-27

import random
pd1 = ["emma","shriya","william","aaron"]
pd2 = ["andrew", "yuqing","michael"]
krewes = {
    "one" : pd1,
    "two" : pd2
    }

def printName():
    period = input('Pick a period (Input 1 or 2): ')
    if period == '1':
        print(krewes["one"][random.randint(0,len(pd1)-1)])
    elif period == '2':
        print(krewes["two"][random.randint(0,len(pd2)-1)])
    else:
        print("This input goes against the rules")
        printName()
    
