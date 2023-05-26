#17/12/2021

#Imports
import time

#Declaring stuffs
Adult = 19.99
Child = 8.99
Senior = 14.99
Student = 9.99
Fee = 2.50

#Welcome tingg
mainMenu = int(input("Welcome To OCR Land Theme Park.\n"
                "Please Select one of the following options:\n"
                "(1) Purchase Tickets | (2) Quit\n-> "))
time.sleep(0.25)

if mainMenu == 2:
    print("\nThank You For Using OCR Lands's, Ticket Service\n")

while mainMenu != 2:
    atot = int(input("\nHow Many Adults\n-> "))
    ctot = int(input("\nHow Many Children\n-> "))
    Sentot = int(input("\nAny Seniors? (65+)\n-> "))
    Stutot = int(input("\nAny Students?\n-> "))

    aCost = Adult * atot
    cCost = Child * ctot
    SenCost = Senior * Sentot
    StuCost = Student * Stutot

    if ctot == 2 and atot == 2 and Sentot == 0 and Stutot == 0:
        print("Your Total Is: 49.00 +", Fee, "Booking Fee")

    elif Sentot >= 1 and Stutot >= 1:
        UFT = aCost + cCost + SenCost + StuCost + Fee
        total = round(UFT, 2)
        print("\nYour Total Is", total, "\nTotal Adults:", atot, "\nTotal Children:", ctot, "\nTotal Seniors:", Sentot, "\nTotal Students:", Stutot)
        time.sleep(10)

    elif Sentot >= 1:
        UFT = aCost + cCost + SenCost + StuCost + Fee
        total = round(UFT, 2)
        print("\nYour Total Is", total, "\nTotal Adults:", atot, "\nTotal Children:", ctot, "\nTotal Seniors (65+):")
        time.sleep(10)

    elif Stutot >= 1:
        UFT = aCost + cCost + SenCost + StuCost + Fee
        total = round(UFT, 2)
        print("\nYour Total Is", total, "\nTotal Adults:", atot, "\nTotal Children:", ctot, "\nTotal Students:", Stutot)
        time.sleep(10)

    else:
        UFT = aCost + cCost + Fee

        total = round(UFT, 2)

        print("\nYour Total Is", total, "\nTotal Adults:", atot, "\nTotal Children:", ctot)
        time.sleep(10)

