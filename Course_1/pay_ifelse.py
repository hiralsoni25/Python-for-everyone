# Calculating pay using if - else 
hrs = input('Enter hours:')
rate = input('Enter rate:')
h = float(hrs)
r = float(rate)
if h > 40:
    gp = ((40 * r) + ((h-40)*r*1.5))
else:
    gp = h * r
print(gp)
