'''Question 25: Filter Specific Word
Keep asking the user to input words. If the user inputs the word "skip", do not print it and ask for another word. Stop the loop if the user inputs "stop".'''

while True:
    word = input("Enter a word ('stop' to quit): ")
    if word == "stop":
        print("Program stopped")
        break
    if word == "skip":
        continue
    print(word)