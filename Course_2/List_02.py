import os
os.chdir('F:\Coursera\Python\Code File\Files')

# using file mbox-short.txt

fname = input('Enter file name: ')
fh = open(fname)

count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
     # line which includes ':' in 'From' is to be skipped using continue 
        continue
    # line which startswith 'From'
    elif line.startswith('From'):
        count = count + 1
        # splitting words in the line
        words = line.split()
        # slicing only email in line which is on '1' position    
        email_list = words[1:2]

        # for converting email_list into email string we use:
        for email in email_list:
            print(email)
            
print('There were', count, 'lines in the file with From as the first word')       

