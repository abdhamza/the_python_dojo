'''Question 10: Check if List is Palindrome
Write code that returns True if a list is a palindrome (reads the same backward as forward), and False otherwise, without using a loop. For example, is_palindrome([1, 2, 3, 2, 1]) should return True.'''

lst = [5, 4, 3, 4, 5]
is_palindrome = lst == lst[::-1]

print(is_palindrome)
