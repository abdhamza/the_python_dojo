'''Question 4: List Comprehension
Use list comprehension to create a new list named squares that contains the squares of all numbers in the list numbers = [1, 2, 3, 4, 5]. Print the squares list.'''

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)