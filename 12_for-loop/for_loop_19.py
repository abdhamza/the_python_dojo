'''Question 19: Find and Print the First Perfect Square in a List
Given a list of positive integers, find and print the first perfect square number. If there is no perfect square in the list, indicate so.'''

import math

numbers = [3, 8, 14, 16, 18]
for num in numbers:
    root = math.sqrt(num)
    if root.is_integer():
        print("First perfect square:", num)
        break
else:
    print("No perfect square found.")