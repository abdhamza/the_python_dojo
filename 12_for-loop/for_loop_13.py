'''Question 13: Maximum Number Before Reaching a Threshold
Given a list of numbers and a threshold value, use a for loop to find and print the maximum number in the list before any number exceeds the threshold.'''

numbers = [10, 20, 30, 40, 50, 25, 35]
threshold = 35
max_number = numbers[0]
for num in numbers:
    if num > threshold:
        break
    if num > max_number:
        max_number = num
print("Maximum number before exceeding threshold:", max_number)