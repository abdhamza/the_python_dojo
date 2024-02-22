'''Question 7: Downward Number Triangle
Print a triangle of numbers descending from 5 to 1, with each row starting from 5 and reducing to the current level.'''
# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
