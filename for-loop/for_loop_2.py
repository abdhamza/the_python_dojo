'''Question 2: Sum of First N Natural Numbers
Ask the user for a number n and use a for loop to calculate the sum of the first n natural numbers.'''

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum is:", sum)