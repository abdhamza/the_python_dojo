'''Question 9: Alphabet Triangle
Print a triangle pattern with alphabets, starting with 'A' at the top and increasing alphabetically with each level, up to 5 levels.'''
# A 
# A B 
# A B C 
# A B C D
# A B C D E

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()