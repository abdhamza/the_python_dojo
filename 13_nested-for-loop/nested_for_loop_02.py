'''Question 2: Right-angled Triangle
Print a right-angled triangle pattern of asterisks (*), with the right angle at the bottom left and 5 levels high.'''
# * 
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()