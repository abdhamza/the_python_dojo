'''Question 6: Print All Divisors of a Number
Ask the user to input a number and print all divisors of that number.
'''

number = int(input("Enter a number: "))
i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1
