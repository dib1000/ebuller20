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

import random

def selectJob():
    #reading file and getting rid of the new lines
    file = open("occupations.csv","r")
    contents = file.read()
    contentlist = contents.split("\n")
    
    #putting the content of the file into dictionaries
    occupations = {}
    for x in range(1,len(contentlist)-2): #no top line or last 2 lines that don't have the same structure as the other lines of file
        item = contentlist[x].split(" \t") #the job names and percentage were connected by this sequence of characters
        occupations[item[0]] = float(item[1])

    jobs = list(occupations.keys()) #list for the jobs
    percentages = list(occupations.values()) #list for the percentages
    job = random.choices(jobs, percentages, k = 1); #method chooses 1 of the jobs randomly based on weighted
                                                    #average based on percentages list. It makes a 1 item list
    return job[0] #only returns the job, not the list
    