#Cashew (Shriya Anand, Emma Buller, William Chen)
#SoftDev
#K06 -- Stl/O: Divine your Destiny! (Parsing through files)
#2021-09-29

# We first started by looking at shriyas code for the 05 assignment and how she read a file
# for that. We then pondered on how to split the lines in the file into a dictionary. We
# then wondered how to choose a job randomly with weighting involved. We thought of ways
# that included loops, but then William told us about and explained how to use the
# random.choices() method. We decided to use that and used some dictionary methods to
# split the keys and values into lists that can be inputted to the choices method.

import csv
import random
def selectJob():
    dictionary ={}
    with open('o.csv', newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
                 dictionary[row['Job Class']] = float(row['Percentage'])
    job = random.choices(list(dictionary.keys()),list(dictionary.values()), k = 1)
    return job[0]



