'''Question 24: Print Every Third Number
Write a program that asks the user to enter numbers continuously. Use a counter to print every third number entered and skip the rest. Stop the loop if the user enters -1.'''

counter = 0
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    counter += 1
    if counter % 3 != 0:
        continue
    print("Every third number:", number)
