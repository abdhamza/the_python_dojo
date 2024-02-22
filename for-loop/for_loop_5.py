'''Question 5: Reverse a Given String
Ask the user for a string and use a for loop to reverse it.'''

string = input("Enter a string: ")
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print("Reversed String:", reversed_string)