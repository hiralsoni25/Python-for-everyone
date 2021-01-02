# Here we have to write a query to slice all the number in .txt file using regular expression and sum all the numbers in list 

# File name = actual_data.txt & sample_data.txt 
# Right answer for Actual data = 359591 and Sample data = 445833

import os
os.chdir('F:\Coursera\Python\Code File\Files')

#import regular expression

import re
handle = input('Enter the file name:')
fd = open(handle)
numlist = []
for line in fd:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    # to skip the empty list []
    if len(stuff) == 0 : 
        continue
    for digits in stuff:
        # Convert string to int and append them to numlist
        num = int(digits)
        numlist.append(num)   
             
print('Total of All the Numbers is: ', sum(numlist))

