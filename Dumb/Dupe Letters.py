def check(string):
    string = string.lower()
    checked = []
    for i in range(len(string)):
        if string[i] in checked:
            return True
        else:
            if string[i] != " ":
                checked.append(string[i])
    return False

checkthis = input("What would you like to check? \n-> ")
print(check(checkthis))