import os
os.chdir('F:\Coursera\Python\Code File\Files')

# using file romeo.txt

fname = input('Enter file name: ')
fh = open(fname)

# Creatina a new empty list name "data"
data = list()

for line in fh:
    line = line.strip()
    #splitting the line  
    words = line.split()

    for single_word in words:
        # exclude all word in the words that are same

        if single_word not in data:
            # adding single word into 'data'
            data.append(single_word)
            #sorting the data alphabetically
            data.sort()

print(data)
    





    
  
