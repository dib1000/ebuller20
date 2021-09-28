#Emma Buller
#SoftDev
#K05 -- Better Living Through Amalgamation
# 2021-9-27

# SUMMARY OF TRIO DISCUSSION (Emma, Gavin, Naomi)
# 
# DISCOVERIES
# We rememberd that dictionaries existed in python and also how to use them
# its "elif" instead of "else if"
# QUESTIONS
# 
# COMMENTS
# We need to be careful with typing as we could make silly mistakes.

import random
pd1 = ["emma","shriya","william","aaron","owen","haotian","ishraq","ivan l",
       "michelle", "naomi", "lewis cass", "renggeng", "oscar", "tami", "aryman",
       "alejandro","deven","tina","yusuf","ella","ltw", "julia","angela"
       ,"christopher","sadid","gavin","ivan m","rayat","tomas","theo","shyne"]
pd2 = ["andrew", "yuqing","michael", "raymond", "kevin","josephine","alif",
       "william","justin","andy","rachel","shadman","david","daniel","cameron",
       "austin","thomas","yaying","jessie","eric","jonathan","zhaoyu","joshua",
       "naokai","yoonah","roshani","qina","han","sophie"]
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
    