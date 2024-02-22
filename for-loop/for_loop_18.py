'''Question 18: Count Items Until a Specific Item is Found
Given a list and a target item, count how many items appear before the target item in the list. Use a loop and break when the target is found.'''

items = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
target = 'date'
count = 0
for item in items:
    if item == target:
        break
    count += 1
print(f"Items before {target}: {count}")
