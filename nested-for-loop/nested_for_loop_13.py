'''Question 13: Hollow Square
Print a 5x5 hollow square pattern of asterisks (*), where only the border is printed.'''
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
