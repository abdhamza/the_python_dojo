'''Question 7: Negative to Positive Number Conversion
Ask the user to enter a negative number and keep asking until a positive number is entered. Then, print the positive number.
'''

number = int(input("Enter a positive number: "))
while number < 0:
    number = int(input("That's not a positive number. Try again: "))
print("You entered:", number)
