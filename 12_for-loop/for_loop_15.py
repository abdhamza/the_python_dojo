'''Question 15: Sum Numbers Until a Negative Entry
Given a list of numbers, use a for loop to calculate the sum of the numbers until a negative number is encountered. Print the sum when the loop ends or breaks.'''

numbers = [4, 5, -1, 2, 3]
sum = 0
for num in numbers:
    if num < 0:
        break
    sum += num
print("Sum before negative entry:", sum)