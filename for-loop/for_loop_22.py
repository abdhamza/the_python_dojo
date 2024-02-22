'''Question 22: Check for Odd Numbers and Do Nothing
Given a list of numbers, write a for loop that checks if each number is odd. If a number is odd, use the pass statement; otherwise, print the number.'''

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 != 0:
        pass  # Do nothing for odd numbers
    else:
        print(num)  # Print even numbers