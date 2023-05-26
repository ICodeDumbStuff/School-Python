numbers = ["A","C","B","","A","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","B",""]
alive = ["A","B","C"]
counts = {"A":0, "B":0, "C":0}
def guess(who):
    def count():
        num = 0
        for i in range(len(numbers)):
            if numbers[i] == "":
                num += 1
        return num

    Choice = int(input(f"Player {who}, What is your number?\n-> "))
    if numbers[Choice] == "":
        numbers[Choice] = who
        counts[who] += 1
        return f"{Choice} is now taken by {who}, there are {count()} remaining"
    else:
        alive.remove(who)
        return f"Taken, there are {count()} remaining"
while len(alive) > 0:
    for i in alive:
        print(guess(i))
print(
    f"A: {counts['A']} | {round((counts['A'] / len(numbers))*100, 0)}%\n"
    f"B: {counts['B']} | {round((counts['B'] / len(numbers))*100, 0)}%\n"
    f"C: {counts['C']} | {round((counts['C'] / len(numbers))*100, 0)}%\n")