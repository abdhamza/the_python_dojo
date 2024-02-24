'''Question 25: Character Frequency
Write a Python program to count the frequency of each character in the string "mississippi" and print the frequencies in descending order.'''

from collections import Counter
my_string = "mississippi"
frequencies = Counter(my_string)
for char, count in frequencies.most_common():
    print(f"{char}: {count}")
