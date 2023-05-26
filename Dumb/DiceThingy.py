#01/12/2021

import random
import time

#database = {"player1":0,"player2":0}

player_1 = 0
player_2 = 0
while True:
    #Welcome To The Game Message
    print("Welcome To Dice Game!\nHere Two Dice Will Be Thrown three times for you and a friend!\nWinner is the one with the highest rolls at the end!\nDouble 6's add 12 points!\n")

    player_1_name = input("Please Enter Player 1's Name\n->")
    player_2_name = input("Please Enter Player 2's Name\n->")


    for i in range(3):
        p1_roll = random.randint(1,6)
        p1_roll_2 = random.randint(1,6)
        print("\nPlayer 1 Scores ", p1_roll, "And", p1_roll_2)
        player_1 = player_1 + p1_roll
        player_1 = player_1 + p1_roll_2
        if p1_roll == 6:
            if p1_roll_2 == 6:
                print("+ 12 Points! (Double 6)")
                player_1 = player_1 + 12

        time.sleep(0.5)

        p2_roll = random.randint(1,6)
        p2_roll_2 = random.randint(1,6)
        print("Player 2 Scores ", p2_roll, "And", p1_roll_2)
        player_2 = player_2 + p2_roll
        player_2 = player_2 + p2_roll_2
        if p2_roll == 6:
            if p2_roll_2 == 6:
                print("+ 12 Points! (Double 6)")
                player_2 = player_2 + 12

        time.sleep(0.5)

    if player_1 > player_2:
        print("\n\n",player_1_name,"Wins!\n  Total: ", player_1)
        time.sleep(15)
        print("\n\nRestarting...\n\n")
        time.sleep(3)
        continue
    else:
        print("\n\n",player_2_name,"Wins!\n  Total: ", player_2)
        time.sleep(15)
        print("\n\nRestarting...\n\n")
        time.sleep(3)
        continue