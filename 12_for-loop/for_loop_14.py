'''Question 14: Print Characters of a String Until a Vowel
Given a string, use a for loop to print each character until you encounter a vowel. When a vowel is encountered, stop the loop.'''

string = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
for char in string:
    if char in vowels:
        break
    print(char)