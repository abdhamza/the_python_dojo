'''Question 4: Find the Factorial of a Given Number
Calculate the factorial of a given number n provided by the user.
'''

n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("Factorial:", factorial)
