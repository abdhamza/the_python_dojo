'''Question 20: Accept Only Valid Input
Ask the user to enter an integer within a specified range, say 1 to 10. Repeat asking for the number until a valid input is entered. Use break to exit the loop once a valid number is entered.'''

while True:
    number = int(input("Enter an integer between 1 and 10: "))
    if 1 <= number <= 10:
        print("Valid input received:", number)
        break
    else:
        print("Invalid input. Please try again.")