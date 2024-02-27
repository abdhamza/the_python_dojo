'''Question 18: First Even Number
Ask the user to enter numbers until they enter an even number. Print "Even number entered" and stop asking for more numbers.'''

while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even number entered")
        break