word=input("enter a word")
print("The ordinal values of the word id:",word)
for character in word:
    print (character,"=>",ord(character))