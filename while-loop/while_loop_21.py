'''Question 21: Print Non-negative Numbers
Ask the user to enter numbers repeatedly. Use a while loop to print only the non-negative numbers. If the user enters a negative number, do not print it and ask for another number.'''

while True:
    number = int(input("Enter a number (or -1 to stop): "))
    if number == -1:
        break
    if number < 0:
        continue
    print(number)
