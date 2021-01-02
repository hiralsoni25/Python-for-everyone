import os
os.chdir('F:\Coursera\Python\Code File\Files')

fname = input('Enter file:')
fh = open(fname)

count = {}

for line in fh:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words = line.split()
        time = words[5]
        x = time.split(':')
        hrs = x[0:1]
        for hr in hrs:
            count[hr] = count.get(hr, 0) + 1


# if we want to sorted in terms of 'k'(keys):
for k,v in sorted(count.items()):
    print(k,v)

# if we want to sorted in terms of 'v'(value):(from big to small)
lst = []
for k,v in count.items():
    newtup = (v,k)
    lst.append(newtup)

for v,k in sorted(lst, reverse=True):
    print(v,k)


    

        
