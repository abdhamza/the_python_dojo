'''Question 6: Immutable Tuples
Explain why you cannot change the value of an element in the tuple numbers = (1, 2, 3) and attempt to change the first element to 0.'''

numbers = (1, 2, 3)
try:
    numbers[0] = 0
except TypeError as e:
    print("Error:", e)