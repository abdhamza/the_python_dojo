'''Question 17: Exit Loop After Printing All Consonants in a String
Given a string, use a for loop to print each consonant. Stop and exit the loop once you've printed all consonants in the string, ignoring vowels and non-alphabet characters.'''

string = "technology"
vowels = "aeiou"
for char in string:
    if char.lower() not in vowels and char.isalpha():
        print(char, end=' ')
    elif not char.isalpha():
        break
