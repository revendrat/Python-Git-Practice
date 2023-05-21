# write a program that calculates future value on a given principal and interest rate
pv = 1000 #(in dollars)
r = 0.045 #(interest rate divided over 100)
n = 5 #(number of years)

#fv = pv*pow((1+r),n)

def inretest_rate(pv,r,n):
    fv = pv*pow((1+r)),n)
    return fv

inretest_rate(1000,0.05,2)