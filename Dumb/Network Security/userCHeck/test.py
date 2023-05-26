# Dice game Redone - Third time

# Imports
import random
import time

thisSection = "the Settings"  # Just like this bec when hiding code with dropdown comments hide

# Settings - eg: "opt.names"
class opt:
    names = True
    rolls = 3
    speed = 0.25
    DiceSize = 6  # 6 = 1-6 output possible
    DiceLow = 1  # Lowest possible output of a dice

thisSection = "Developer Options"
debugOpt = True

# Functions
def debug(debugmsg):
    if debugOpt == True:
        print(f"Debug: {debugmsg}")
    else:
        pass


def setName(playnum, playname):
    if playname == "" or playname == " ":
        playname = f"Player {playnum}"
    if playnum == 1:
        p1.name = playname
    if playnum == 2:
        p2.name = playname
    else:
        pass

def dice(low, high):
    dice = random.randint(low, high)
    return dice


thisSection = "Main Program Stuff"
while True:
    # Var - Player data stuff - In the loop so that it resets
    # Note: Could move playnames var out of loop to save them?
    class p1:
        score = 0
        name = "Player 1"

    class p2:
        score = 0
        name = "Player 2"

    if opt.names == True:
        setName(1, input("\nEnter PLAYER ONE name\n-> "))
        setName(2, input("\nEnter PLAYER TWO name\n-> "))
        debug(f"P1: '{p1.name}' and P2: '{p2.name}'")
    else:
        conti = input("Ready to start!\n(Press enter to continue)\n")
        debug("Bypassing Names because disabled...")

    for i in range(opt.rolls):
        print("=======================\n")
        p1roll = dice(opt.DiceLow, opt.DiceSize)  # so can be used in a message
        p1.score = p1.score + p1roll
        print(f"{p1.name} Rolled a {p1roll}\nTotal Score: {p1.score}")
        time.sleep(opt.speed)

        p2roll = dice(opt.DiceLow, opt.DiceSize)  # so can be used in a message
        p2.score = p2.score + p2roll
        print(f"\n{p2.name} Rolled a {p2roll}\nTotal Score: {p2.score}\n")

    # Finished Rolling Dice
    print("=======================\n")
    if p1.score > p2.score:
        print(
            f"{p1.name} WINS!\nTotal Score: {p1.score}\n({p2.name}'s Score: {p2.score})"
        )
    elif p1.score < p2.score:
        print(
            f"{p2.name} WINS!\nTotal Score: {p2.score}\n({p1.name}'s Score: {p1.score})"
        )
    elif p1.score == p2.score:
        print(
            f"GAME OVER! TIE!\n{p1.name}'s Score: {p1.score}\n({p2.name} Score: {p2.score})"
        )
    else:
        print("error")

    time.sleep(3)
    if opt.names == False:
        cont = input("Roll Again? (double press enter)\n")
    else:
        pass