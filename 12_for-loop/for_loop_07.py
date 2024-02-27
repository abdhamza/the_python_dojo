'''Question 7: Print Multiplication Table
Ask the user to enter a number, then print the multiplication table for that number up to 10.'''

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")