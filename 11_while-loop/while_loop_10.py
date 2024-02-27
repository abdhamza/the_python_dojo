'''Question 10: Multiplication Table
Ask the user to enter a number, then print the multiplication table for that number up to 10.
'''

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
