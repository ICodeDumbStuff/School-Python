#03/12/2021
import time

domanual = int(input("Manual (1) Or Auto (2)?\n->"))
if domanual == 1:
    number = 0
    while True:
        database = ["Alex","Leo","Alexa","LoeIsDumb"]

        name = input("Please Enter Your Name\n->")

        if name in database:
            print("You Are Registered!")
            #Rest of code here
            for i in range(3):
                number = int(input("\nPlease Enter A Number!\n->"))
                if number % 3 == 0 and number % 5 == 0:
                    print("FizzBuzz")
                elif number % 3 == 0:
                    print("Fizz")
                elif number % 5 == 0:
                    print("Buzz")
                elif number == number:
                    print(number)
        else:
            print("You Arent Registered!")
        break

if domanual == 2:
    number = 1
    while True:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            number = number + 1
            time.sleep(0.5)
        elif number % 3 == 0:
            print("Fizz")
            number = number + 1
            time.sleep(0.5)
        elif number % 5 == 0:
            print("Buzz")
            number = number + 1
            time.sleep(0.5)
        elif number == number:
            print(number)
            number = number + 1
            time.sleep(0.5)
