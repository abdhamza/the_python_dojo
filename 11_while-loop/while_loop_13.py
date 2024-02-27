'''Question 13: Fibonacci Sequence Up to N
Generate and print the Fibonacci sequence up to a number n provided by the user.'''

n = int(input("Enter the value of n: "))
a, b = 0, 1
while a <= n:
    print(a, end=' ')
    a, b = b, a + b
