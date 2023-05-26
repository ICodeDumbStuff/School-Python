# Voting
def voting():
    votes = [0,0,0]
    vote = ""
    while vote != "end":
        vote = input("Please enter a,b,c or end\n-> ")
        if vote == "a":
            votes[0] += 1
        elif vote == "b":
            votes[1] += 1
        elif vote == "c":
            votes[2] += 1
        elif vote == "end":
            out = f"\n\n\nEnding Vote\n\n\nFinal Votes\nA: {votes[0]} \nB: {votes[1]} \nC: {votes[2]}"
    return out
print(voting())