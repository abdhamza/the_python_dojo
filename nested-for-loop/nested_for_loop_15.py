'''Question 15: Staircase Pattern
Print a staircase pattern of asterisks (*), where each level has one more asterisk than the previous level, up to 5 levels.'''

for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)