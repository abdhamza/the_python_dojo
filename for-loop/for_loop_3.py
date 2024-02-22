'''Question 3: Print Even Numbers Less Than N
Ask the user for a number n and use a for loop to print all even numbers less than n.'''

n = int(input("Enter a number: "))
for i in range(2, n, 2):
    print(i)