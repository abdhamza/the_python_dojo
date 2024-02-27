'''Question 16: Break on Negative Input
Ask the user to enter numbers repeatedly and sum them up. Stop asking for numbers and print the sum when the user enters a negative number.'''

sum = 0
while True:
    number = int(input("Enter a number (or a negative number to stop): "))
    if number < 0:
        break
    sum += number
print("Sum of entered numbers:", sum)
