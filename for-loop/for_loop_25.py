'''Question 25: Simulate a No-Operation in a Conditional Block
Imagine a scenario where you're iterating over a range of numbers and you want to print a message only if the number is a multiple of 5. If it's not, you deliberately choose to do nothing.'''

for i in range(1, 21):
    if i % 5 == 0:
        print(f"{i} is a multiple of 5")
    else:
        pass  # Explicitly doing nothing