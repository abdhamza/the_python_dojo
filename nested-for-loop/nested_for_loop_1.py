'''Question 1: Square Pattern
Print a 5x5 square pattern of asterisks (*).'''

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

'''Question 4: Number Pyramid
Print a pyramid pattern with numbers increased by 1, with the peak being 5.'''

for i in range(1, 6):
    print(' ' * (5 - i) + ' '.join(str(i) for j in range(i)))
'''Question 5: Diamond Pattern
Print a diamond pattern of asterisks (*) that is 5 levels high.'''

n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
'''Question 6: Checkerboard Pattern
Print an 8x8 checkerboard pattern using hashtags (#) and spaces.'''

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(" ", end="")
        else:
            print("#", end="")
    print()
'''Question 7: Downward Number Triangle
Print a triangle of numbers descending from 5 to 1, with each row starting from 5 and reducing to the current level.'''

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''Question 8: Hourglass Pattern
Print an hourglass pattern of asterisks (*) that is 5 levels high.'''

n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
for i in range(2, n + 1):
    print(' ' * (n - i) + '* ' * i)
'''Question 9: Alphabet Triangle
Print a triangle pattern with alphabets, starting with 'A' at the top and increasing alphabetically with each level, up to 5 levels.'''

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
'''Question 10: Inverted Pyramid of Numbers
Print an inverted pyramid pattern with numbers, starting with 1 to 5 at the top and decreasing by one number each level.'''

for i in range(5, 0, -1):
    print(' ' * (5 - i) + ' '.join(str(j) for j in range(1, i + 1)))
'''Question 11: Zigzag Pattern
Print a zigzag pattern of asterisks (*) spanning 3 rows and 9 columns.'''

for i in range(3):
    for j in range(9):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''Question 12: Numeric Pyramid with Spacing
Print a pyramid pattern where numbers increase from 1 at the top to 5 at the base, with appropriate spacing on each side.'''

for i in range(1, 6):
    print(' ' * (5 - i) + ' '.join(str(j) for j in range(1, i + 1)))
'''Question 13: Hollow Square
Print a 5x5 hollow square pattern of asterisks (*), where only the border is printed.'''

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''Question 14: Cross Pattern
Print a cross (X) pattern of asterisks (*) that spans 5 lines.'''

n = 5
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''Question 15: Staircase Pattern
Print a staircase pattern of asterisks (*), where each level has one more asterisk than the previous level, up to 5 levels.'''

for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)