# Cashew SoftDev K<06> 
#### Divine Your Destiny Pt.2 Summative Assessment (Explain the code)
#### (Shriya Anand, Emma Buller, William Chen)
#### <2021>-<09>-<29>
#### How the code works
## Correct Method:
1. We first opened the csv file- 'occ.csv' is the file we are opening and 'newline = ''' handles the line breaks for us (we do not need to worry about splitting the data for each line).
2. We then read through the file using a csv reader.
3. Then, we used a for loop to go through the entire file row by row.
4. Then we put the job and percentage in a previously created dictionary. In the dictionary, each entry has a key (like a word) and a corresponding value (like definition). In our case, the job was the key and percentage was the value.
5. We then split the dictionary into two lists: one for the keys and one for the values. We do this for the random.choices method. Random.choices lets us pick a value in a list with weighted values (or different levels of importance).
## Old Method:
1. We opened the file in read mode which lets us go through the file's content without being able to edit (write mode). Originally, we had copied the data wrong. so we treated it as a text file instead of a csv (comma separated value).
2. Then we used the split function to divide the content of the file wherever there was a newline and added each piece to a list.
3. This list had all the jobs and percents as one string. Then we looped through the list and looked at each item.
4. We then split the string by the character in between the job and the percentage.
5. Then we put the job and percentage in a dictionary. In the dictionary, each entry has a key (like a word) and a corresponding value (like definition). In our case, the job was the key and percentage was the value.
6. We then split the dictionary into two lists: one for the keys and one for the values. We do this for the random.choices method. Random.choices lets us pick a value in a list with weighted values.
**Dictionaries:**
Dictionaries are useful because you store two sets of related data together. The order is also not preserved so it is easy to sort, unlike lists. You can also easily find values using keys rather than their index. They also don't allow duplicates, which can be useful in some cases.
**Lists:**
Lists are an easy way to store and retrieve data. Lists allow for duplicates, which can be useful in some cases. Lists can be 2d and are not restricted to only 1 key having 1 value associated with it.
