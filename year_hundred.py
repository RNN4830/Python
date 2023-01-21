

# ask user name and age
# print a message when they will turn 100

from datetime import datetime

yearNow = datetime.now().year
name = input ("What is your name?: ")
age =  int(input("What is your age?: "))
birthdayYet = input("Have you had a birthday yet this year? Y or N: ")

if birthdayYet == "Y":
    yearNow = yearNow
else:
    yearNow = (yearNow - 1)


turnHundred = (yearNow - age) + 100

print ("Hi, " + name + " the year that you will turn 100 is: " + str(turnHundred))