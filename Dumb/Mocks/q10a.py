def user(firstName, lastName, accType):
    if accType == "t":
        return f"{lastName[-3:] + firstName[0:2]}"
    elif accType == "s":
        return f"{firstName[0:3] + lastName[0:2]}"
    else:
        return "Invalid Input"
res = user(input("Firstname\n-> "), input("surname\n-> "), input("Student or Teacher?\n-> ")[0:1].lower())
print(res)