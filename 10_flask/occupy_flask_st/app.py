#Cashew (Shriya Anand, Emma Buller, William Chen)
#SoftDev
#K10 -- Putting Little Pieces Together (More things with Flask)
#2021-10-05

from flask import Flask
app = Flask(__name__)

import random
import csv

def selectJob():
    dictionary ={}
    with open('occ_per.csv', newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
                 dictionary[row['Job Class']] = float(row['Percentage'])
    job = random.choices(list(dictionary.keys()),list(dictionary.values()), k = 1)
    return job[0]

@app.route("/")
def hello_world():
    print(__name__)
    return selectJob()

app.run()
