# changing the directory path
import os
os.chdir('F:\Coursera\Python\Code File\Files')
# Use the file name mbox-short.txt as the file name
fname = input('Enter File Name: ')
fh = open(fname)
#fh = open('mbox-short.txt')
count = 0
y = 0
for line in fh:
    # Removing space between line (must to be done)
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = 1 + count
        #finding the place number of ':'
        fline = line.find(':')
        # string slicing the number after ':' i.e., adding 1 and assigning it to 'x'
        x = line[fline+1:]
        # converting str(x) to float(x) and Adding it
        y = y + float(x)
print('totat sum of numbers:', y)
print('total number of line:', count)
print('Average spam confinence:', y/count)
