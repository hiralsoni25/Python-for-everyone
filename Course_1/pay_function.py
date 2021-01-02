# calculating pay by creating computepay() function
def computepay(h,r):
    if h > 40:
        gp = h*r + ((h-40)*r*0.5)
        return gp
    else:
        gp = h*r
        return gp

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)
