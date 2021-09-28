#Cashew (Shriya Anand, Emma Buller, William Chen)
#SoftDev
#K06 -- Stl/O: Divine your Destiny! (Parsing through files)
#2021-09-29

#reading file and splitting everything
file = open("occupations.csv","r")
contents = file.read()
contentlist = contents.split("\n")


weight = 0
occupations = {}
for x in range(1,len(contentlist)-1):
    item = contentlist[x].split("\t")
    print(item[0])
    print(item[1])

