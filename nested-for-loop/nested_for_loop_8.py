'''Question 8: Hourglass Pattern
Print an hourglass pattern of asterisks (*) that is 5 levels high.'''
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
for i in range(2, n + 1):
    print(' ' * (n - i) + '* ' * i)