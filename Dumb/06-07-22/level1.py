reg = ["jim", "sarah"]

def isRegistered(reg_user):
    if reg_user in reg:
        return True
    return False
# Main Program
name = input("Please enter your name\n-> ")
res = isRegistered(name)
print(res)