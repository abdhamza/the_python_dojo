'''Question 6: Count Digits in a Number
Ask the user to input a number and use a for loop to count the number of digits in that number.'''

number = int(input("Enter a number: "))
count = 0
for digit in str(number):
    count += 1
print("Number of digits:", count)