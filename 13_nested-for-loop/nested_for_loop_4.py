'''Question 4: Number Pyramid
Print a pyramid pattern with numbers increased by 1, with the peak being 5.'''
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    print(' ' * (5 - i) + ' '.join(str(i) for j in range(i)))