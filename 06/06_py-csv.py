#Cashew (Shriya Anand, Emma Buller, William Chen)
#SoftDev
#K06 -- Stl/O: Divine your Destiny! (Parsing through files)
#2021-09-29

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
    print(occupations)
