import random

attemps = 20

def guess(uguess, num):
    if uguess == num:
        return True
    else:
        return False

def play():
    try:
        guess1 = int(input(f"Attemps: {i+1}/20\nWhats your guess?\n-> "))
        res = guess(guess1, num)
        if res == True:
            return True
        else:
            return "Try Again"
    except:
        return "Not a number"

while True: # Keeps it running forever - so can play again
    num = random.randint(1,100)
    print("Debug:",num)
    print("Guess between 1-100")
    print(f"You Have {attemps} Attemps\n\n")

    for i in range(attemps):
        res = play()

        if res == True:
            print(f"\n\nYou Win!\nAttemps: {i+1}\n")
            q = input("Press (ENTER) to play again!")
            break
        else:
            print(res)


        if i == 19:
            print("\nYou Failed!\n")
            q = input("Press (ENTER) to play again!")
            break