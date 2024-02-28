'''Question 3: Remove an Element Safely
Given a set fruits = {"apple", "banana", "cherry"}, remove "banana" from the set using a method that does not raise an error if the element is not present. Print the set afterwards.'''

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)