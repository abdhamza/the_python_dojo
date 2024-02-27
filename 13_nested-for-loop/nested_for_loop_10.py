'''Question 10: Inverted Pyramid of Numbers
Print an inverted pyramid pattern with numbers, starting with 1 to 5 at the top and decreasing by one number each level.'''
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

for i in range(5, 0, -1):
    print(' ' * (5 - i) + ' '.join(str(j) for j in range(1, i + 1)))