'''Question 2: Sum of First N Natural Numbers
Ask the user for a number n and then calculate the sum of the first n natural numbers.
'''

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum is:", sum)
