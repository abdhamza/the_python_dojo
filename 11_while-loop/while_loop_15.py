'''Question 15: Simple Interest Accumulation
Given principal p, interest rate r, and time t in years, calculate how much interest is earned. The user enters p, r, and t.'''

p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (as a decimal): "))
t = int(input("Enter time in years: "))
interest = 0
while t > 0:
    interest += p * r
    t -= 1
print("Total interest earned:", interest)
