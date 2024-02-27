'''Question 14: Print a Triangle of Stars
Print a right-angled triangle of stars with height n provided by the user.'''

n = int(input("Enter the height of the triangle: "))
i = 1
while i <= n:
    print('*' * i)
    i += 1
