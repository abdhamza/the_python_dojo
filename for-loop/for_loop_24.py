'''Question 24: Skip Printing Specific Words
Given a list of words, write a for loop to print each word except the word "skip". Use the pass statement for "skip" and continue to the next iteration.'''

words = ["hello", "world", "skip", "python", "programming"]
for word in words:
    if word == "skip":
        pass  # Intentionally doing nothing and moving to the next iteration
    else:
        print(word)