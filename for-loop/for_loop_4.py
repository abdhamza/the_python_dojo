'''Question 4: Factorial of a Given Number
Calculate the factorial of a given number n provided by the user.'''

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("Factorial:", factorial)