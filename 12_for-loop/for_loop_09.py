'''Question 9: Find Average of List
Given a list of numbers, use a for loop to calculate the average.'''

numbers = [10, 20, 30, 40, 50]
sum = 0
for number in numbers:
    sum += number
average = sum / len(numbers)
print("Average:", average)
