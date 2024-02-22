'''Question 12: Stop Reading After a Specific Word
Given a list of words, use a for loop to print each word until you encounter the word "stop". Once "stop" is encountered, exit the loop.'''

words = ["hello", "world", "stop", "python", "programming"]
for word in words:
    if word == "stop":
        break
    print(word)