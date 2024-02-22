'''Question 23: Odd Numbers Skipper
Ask the user to enter a series of numbers. Print each number except for when it is odd. Use the continue statement to skip odd numbers.'''

while True:
    number = int(input("Enter a number (or -1 to stop): "))
    if number == -1:
        break
    if number % 2 != 0:
        continue
    print(number)
