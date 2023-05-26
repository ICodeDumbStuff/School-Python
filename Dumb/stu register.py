sNames = ["Rod", "Anna", "Huw", "Emma", "Patrice", "Inqbal"]

def register(names):
    yes = 0
    no = 0
    for i in names:
        attend = input(f"{i}\nHere? (Y/N)\n-> ")
        if attend[:1].upper() == "Y":
            yes += 1
        else:
            no += 1
    return f"There are {no} Students Absent\nThere are {yes} Students Here"
print(register(sNames))