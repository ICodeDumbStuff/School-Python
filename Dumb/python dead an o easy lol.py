print("Script Start\n=========================\n\n")

name = input("Please Enter Your Name?\n-> ")

age = int (input("\nHello, " + name + "!\nWhat Is Your Age?\n-> "))

if age > 17:
    print("You Are old enough to drive!")
else:
    print("You are NOT old enough to drive!")