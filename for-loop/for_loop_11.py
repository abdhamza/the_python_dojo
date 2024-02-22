'''Question 11: Skip to the First Non-alphabetic Character
Given a string, use a for loop to iterate through each character and break the loop when the first non-alphabetic character is encountered. Print the position of this character.'''

string = "Hello123"
for i, char in enumerate(string):
    if not char.isalpha():
        print("First non-alphabetic character at position:", i)
        break