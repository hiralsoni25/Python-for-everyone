import os
os.chdir('F:\Coursera\Python\Code File\Files')

fname = input('Enter file:')
fh = open(fname)

count = dict()

for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words = line.split()
        emails = words[1:2]
        for email in emails:
            count[email] = count.get(email,0) + 1


bigcount = None
bigemail = None
for email,count in count.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
