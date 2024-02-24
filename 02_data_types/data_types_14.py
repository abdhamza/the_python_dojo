'''Question 14
Write a Python code to merge two dictionaries and check type of resultant dictionary dict1 = {'a': 100, 'b': 200} and dict2 = {'x': 300, 'y': 200}.'''

dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
dict1.update(dict2)
print(dict1)
print(type(dict1).__name__)