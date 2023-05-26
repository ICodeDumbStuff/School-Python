#imports
import time

allowed = 0

timslep = 0.75

while allowed != 8:

    height = int(input("Height (cm)\n-> "))

    # is 140 or taller
    if height >= 140:
        print ("You Are Allowed To Ride!\n")
        allowed = allowed + 1
        time.sleep(timslep)

    #with adult 120+
    elif height >= 120:
        adult = input("Are You Riding With A Adult? (Yes/No)\n-> ")
        #adult = input("Are You Riding With A Adult Taller than 140cm? (Yes/No)\n-> ")

        #conversion stuff
        a_format = adult.upper()
        a_slice = a_format[0:1]

        if a_slice == "Y":
            print("You Are Allowed To Ride!\n")
            allowed = allowed + 1
            time.sleep(timslep)
        elif a_slice == "N":
            print("You Are NOT Allowed To Ride!\n")
        else:
            print("Invalid Input...")
            time.sleep(0.5)
            print("\nRestarting...\n")
            time.sleep(0.5)

    # ur short
    elif height <= 119:
        print("You Are NOT Allowed To Ride!\n")