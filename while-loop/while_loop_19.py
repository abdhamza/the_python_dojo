'''Question 19: Skip to Next Iteration and Break
Prompt the user to enter a series of integers. Use a while loop to add these integers to a sum. If the user enters 0, print "Zero encountered, skipping" and continue to the next iteration. If the user enters -1, break out of the loop and print the sum.'''

sum = 0
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == 0:
        print("Zero encountered, skipping")
        continue
    elif number == -1:
        break
    sum += number
print("Sum of entered numbers:", sum)