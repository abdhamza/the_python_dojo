'''Question 22: Sum of Positive Numbers Only
Prompt the user to enter numbers until they enter 0. Use a while loop to calculate the sum of only the positive numbers entered. Skip any negative numbers using the continue statement.'''

sum = 0
while True:
    number = int(input("Enter a number (0 to end): "))
    if number == 0:
        break
    if number < 0:
        continue
    sum += number
print("Sum of positive numbers:", sum)
