
# Database for auth users
users = {"alex":"123", "kenyon":"abcd"}

# Functions
# Login Function
def login(l_user, l_pass):
    if l_user in users:
        if l_pass == users[l_user]:
            return "OK"
    print("INVALID")

# Check Login and verify
username = input("Username\n-> ")
password = input("Password\n-> ")
logincheck = login(username, password)
if logincheck != "OK":
    print("Error")