'''Question 10: Concatenate All List Elements into a String
Given a list of strings, use a for loop to concatenate all elements into a single string.'''

strings = ["Hello", "world", "Python"]
result = ''
for string in strings:
    result += string + " "
print("Concatenated String:", result.strip())