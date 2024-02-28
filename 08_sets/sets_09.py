'''Question 9: Symmetric Difference
Given two sets a = {1, 2, 3} and b = {3, 4, 5}, create and print a new set that contains the elements that are in either a or b but not in both.'''

a = {1, 2, 3}
b = {3, 4, 5}
symmetric_difference_set = a.symmetric_difference(b)
print(symmetric_difference_set)