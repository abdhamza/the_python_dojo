'''Question 28: Substring Occurrences
Write a Python program to find the number of occurrences of the substring "is" in the string "This is an island and it is beautiful", including overlapping occurrences.'''

my_string = "This is an island and it is beautiful"
substring = "is"
count = sum(1 for i in range(len(my_string)) if my_string.startswith(substring, i))
print(count)