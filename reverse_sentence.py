
#take input from user
#split the input from user at the spaces and add to list
#reverse list
#print words in reverse


userInput = input("Please enter a sentence, we will convert it to see it backwards: ")
print (userInput)
splitList = userInput.split(" ")
reverseList = splitList[::-1]
# print(reverseList)
print(*reverseList)