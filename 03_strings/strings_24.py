'''Question 24: Palindrome Check
Write a Python program to check if the string "radar" is a palindrome (reads the same backward as forward).'''

my_string = "civic"
if my_string == my_string[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")