'''Question 13
Create a Python script that removes duplicates from a list my_list = [1,2,2,3,4,4,5].'''

my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list))
print(my_list)