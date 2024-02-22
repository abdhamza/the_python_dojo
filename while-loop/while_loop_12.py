'''Question 12: Count Down Timer
Ask the user to enter a number of seconds, then count down to zero, printing each second.'''

seconds = int(input("Enter number of seconds: "))
while seconds >= 0:
    print(seconds)
    seconds -= 1