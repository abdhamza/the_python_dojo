'''Question 5: Calculate the Power of a Number
Ask the user for the base x and exponent n and calculate x raised to the power n
'''

x = int(input("Enter the base: "))
n = int(input("Enter the exponent: "))
result = 1
i = 0
while i < n:
    result *= x
    i += 1
print(f"{x} to the power of {n} is: {result}")
