'''Question 14: Cross Pattern
Print a cross (X) pattern of asterisks (*) that spans 5 lines.'''
# *   *
#  * *
#   *
#  * *
# *   *

n = 5
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()