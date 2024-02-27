'''Question 8: Sum of Entered Numbers
Keep asking the user to enter numbers until they enter 0. Use a for loop (with range and input inside the loop) to sum all entered numbers.'''

sum = 0
for _ in range(1000000):  # Arbitrary large number
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        break
    sum += number
print("Sum of entered numbers:", sum)
