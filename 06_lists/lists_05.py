'''Question 5: Manipulating Lists with Methods
Given a list items = ["Python", "Java", "C++", "JavaScript"], perform the following operations in order:

1) Sort the list in alphabetical order.
2) Reverse the order of the list.
3) Insert "Ruby" at index 2.
4) Print the final list.'''

items = ["Python", "Java", "C++", "JavaScript"]
items.sort()
items.reverse()
items.insert(2, "Ruby")
print(items)