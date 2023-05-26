# 08/12/2021
# 09/12/2021
# Voting System Testing for computer science

import time

#Setup stuff
endpassword = input("\nVoting System Setup!\nEnd Vote Password\n-> ")
#who vote for
canda_1 = input("Who Is Candadate 1\n-> ")
canda_2 = input("Who Is Candadate 2\n-> ")
canda_3 = input("Who Is Candadate 3\n-> ")

#Vote Counter
canda_1_c = 0
canda_2_c = 0
canda_3_c = 0
votes = 0

active = 1

while active ==1:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome To The Voting System!")
    print("Total Votes: ", votes)
    print("Please Enter Who You Want To Vote For!")
    print("\nA -", canda_1)
    print("B -", canda_2)
    print("C -", canda_3)
    vote = input("\nPlease Enter Who You Are Voting For Below!\n-> ")

    if vote == "A":
        print("Vote Registered")
        canda_1_c = canda_1_c + 1
        votes = votes + 1
    elif vote == "B":
        print("Vote Registered")
        canda_2_c = canda_2_c + 1
        votes = votes + 1
    elif vote == "C":
        print("Vote Registered")
        canda_3_c = canda_3_c + 1
        votes = votes + 1
    elif vote == endpassword:
        print("\n\n\n====================================================================\n\n\nVote Ended")
        print("\nHere Are The Results!\n")
        print(canda_1, "Has", canda_1_c, "Votes!")
        print(canda_2, "Has", canda_2_c, "Votes!")
        print(canda_3, "Has", canda_3_c, "Votes!")
        print("Total Votes: ", votes, "\n\n\n====================================================================\n\n\n")
        break
    else:
        print("Invalid Vote")
        time.sleep(1)