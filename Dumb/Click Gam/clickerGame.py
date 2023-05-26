import random
import time

# Bout 9 lines console
# Note for selections: 0,1,2,3,4 etc | Clicks, Multi, '
data = [0,1]

def MainMenuOut():
    print("1 | Welcome to Clicker Game (CLI) \n"
          "2 | \n"
          "3 | How to play, \n"
          "4 | Press (ENTER) to click! \n"
          "5 | \n"
          "6 | Extra Keybinds, Press the BIND then (ENTER)\n"
          "7 | 1, Shop \n8 | ")

def click():
    data[0] += 1 + (1 * data[1])
    print("\n\n"
         f"\nMultiplier: {data[1]}"
         f"\nClicks: {data[0]}"
          "\n\n\n")
    return

def shopMenu():
    while True:
        print("Welcome To The Upgrade Shop \n"
              "\n"
              "0, To Exit\n"
             f"1, Multiplier: {round((100 + ((data[1]*1.010))))}\n"
              "\n"
              "Extra Keybinds, Press the BIND then (ENTER)\n"
              "1, Shop \n")
        inp = input()
        try: # If input is just number (for keybinds)
                numID = int(inp)
                if numID == 0:
                    print("Press (ENTER) to click")
                    return
                elif numID == 1:
                    pass
                else:
                    print("Invalid Option")
                    click()
        except: # if not a number then they are "clicking"
            pass

MainMenuOut()

while True: #keep game running
    inp = input()

    try: # If input is just number (for keybinds)
            numID = int(inp)
            if numID == 1:
                shopMenu()
            else:
                print("Invalid Option")
                click()
    except: # if not a number then they are "clicking"
        click()