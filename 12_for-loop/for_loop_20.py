'''Question 20: Print Elements Up to a Specific Value (Exclusive)
Given a sorted list of numbers and a threshold value, print each number up to but not including the first number that is greater than or equal to the threshold.'''

numbers = [1, 3, 5, 7, 9, 11, 13]
threshold = 10
for num in numbers:
    if num >= threshold:
        break
    print(num)