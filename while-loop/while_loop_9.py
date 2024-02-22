'''Question 9: Sum of Entered Numbers
Keep asking the user to enter a number until they enter 0. Print the sum of all entered numbers.
'''
sum = 0
number = float(input("Enter a number (0 to quit): "))
while number != 0:
    sum += number
    number = float(input("Enter another number (0 to quit): "))
print("Sum of entered numbers:", sum)
