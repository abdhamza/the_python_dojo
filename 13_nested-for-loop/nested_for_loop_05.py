'''Question 5: Diamond Pattern
Print a diamond pattern of asterisks (*) that is 5 levels high.'''
#   * 
#  * *
# * * *
#  * *
#   *

n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

