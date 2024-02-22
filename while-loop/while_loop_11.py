'''Question 11: Detecting Palindrome
Ask the user to enter a word and check if it is a palindrome (reads the same backward and forward).'''

word = input("Enter a word: ")
reversed_word = ''
i = len(word) - 1
while i >= 0:
    reversed_word += word[i]
    i -= 1
if word == reversed_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
