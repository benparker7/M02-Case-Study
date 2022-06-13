"""
Author: Ben Parker
Name: Dean's list or honor roll
This application takes a user's input in the form of
their last name, first name, and GPA. If 'ZZZ' is entered
for the last name, the program halts. If their GPA is
higher than 3.5, a message will be displayed saying
they made the Dean's list, and if their GPA is 3.25
or higher, it will say they made the honor roll. If
neither of these have been met, it will say you made
neither.
"""

lastName = input("What is your last name? ")

if lastName == "ZZZ":
    exit()

firstName = input("What is your first name? ")
studentGPA = float(input("What is your GPA? "))

if studentGPA >= 3.5:
    print("You have made the Dean's list")
elif studentGPA >= 3.25:
    print("You have made the honor roll")
else:
    print("You have made neither")
