'''Question 17: Stop at Specific Word
Keep asking the user to enter words until they enter "stop". Once "stop" is entered, print "Program stopped" and terminate the loop.'''

while True:
    word = input("Enter a word (or 'stop' to end): ")
    if word == "stop":
        print("Program stopped")
        break