'''Question 3: Inverted Right-angled Triangle
Print an inverted right-angled triangle pattern of asterisks (*), with the right angle at the top left and 5 levels high.'''
# * * * * * 
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()