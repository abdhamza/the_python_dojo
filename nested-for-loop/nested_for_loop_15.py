'''Question 15: Staircase Pattern
Print a staircase pattern of asterisks (*), where each level has one more asterisk than the previous level, up to 5 levels.'''
# *
# **
# ***
# ****
# *****

levels = 5
for level in range(1, levels + 1):
    print('*' * level)
