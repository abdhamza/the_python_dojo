'''Question 6: Checkerboard Pattern
Print an 8x8 checkerboard pattern using hashtags (#) and spaces.'''
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(" ", end="")
        else:
            print("#", end="")
    print()

