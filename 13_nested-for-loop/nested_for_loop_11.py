'''Question 11: Zigzag Pattern
Print a zigzag pattern of asterisks (*) spanning 3 rows and 9 columns.'''
# *   *   *   *   * 
#   *   *   *   *

# Number of rows and columns
rows = 3
columns = 9

# Loop through each row
for row in range(rows):
    # Loop through each column
    for col in range(columns):
        # Calculate the position in the zigzag pattern
        if (col % (rows - 1) == 0 and row == 0) or (col % (rows - 1) == 1 and row == 1) or (col % (rows - 1) == 2 and row == 2) or (col % (rows - 1) == 1 and row == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Move to the next line after finishing each row
    print()