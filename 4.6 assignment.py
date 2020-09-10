def computepay(h,r):
    if h > 40:
        rate1 = (r * 1.5) * (h-40)
    added = ((h-5)*r) + rate1
    return added

hrs = input("Enter Hours:")
r1 = input("Enter Rate:")
h = float(hrs)
r = float(r1)
p = computepay(h, r)
print("Pay",p)
