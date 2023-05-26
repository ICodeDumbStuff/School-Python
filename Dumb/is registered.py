# 18/02/2022
# Imports
# Non

# Le Database :)
data = {
    "Admin":"AdminPassword1234",
    "Alex":"pass1234",
    "Leo":"6969420",
    "Ken":"6969422"}

# Authentication Server
def Auth(a_user, a_pass):

    checkuser = is_reg(a_user)

    if checkuser == True:
        if a_pass == data[a_user]:
            return True
        else:
            return "Invalid Password!"
    else:
        return "Username Doesnt Exist!"

# Check Username Exist
def is_reg(r_user):
    if r_user in data:
        return True
    else:
        return False

# Main Stuffs (Not Functions)

# Input Username And Password
username = str(input("Username\n-> "))
password = str(input("Password\n-> "))

# Print The Output!
print(Auth(username, password))

data[inspect]