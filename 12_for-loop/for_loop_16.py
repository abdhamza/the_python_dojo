'''Question 16: Identify and Print the Index of the First Duplicate in a List
Given a list of integers, identify the first element that appears more than once and print its index. If there are no duplicates, print a message indicating so.'''

numbers = [3, 5, 7, 3, 1, 5, 7]
seen = set()
for i, num in enumerate(numbers):
    if num in seen:
        print("First duplicate at index:", i)
        break
    seen.add(num)
else:
    print("No duplicates found.")
