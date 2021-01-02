import os
os.chdir('F:\Coursera\Python\Code File\Files')
fname = input("Enter file name:")
f = open(fname)   
for line in f:
    line = line.rstrip()
    line = line.upper()
    print(line)
