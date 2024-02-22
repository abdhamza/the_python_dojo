'''Question 12: Numeric Pyramid with Spacing
Print a pyramid pattern where numbers increase from 1 at the top to 5 at the base, with appropriate spacing on each side.'''
#         1
#       1   2
#     1   2   3
#   1   2   3   4
# 1   2   3   4   5

for i in range(1, 6):
    print('  ' * (5 - i) + '   '.join(str(j) for j in range(1, i + 1)))

