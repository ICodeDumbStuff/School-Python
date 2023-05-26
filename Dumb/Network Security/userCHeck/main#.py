'''
get username -> if register -> return str
Yes: Welcome username
no: sorry username is not a registered username, please try again

Ext: 3 attemps
Ext: Allow registers

Notes for register,
if e=nrg in f-string for userCheck
Register username
'''

debug = True# Ignore dis

dataFile = open('database.txt', 'r')
dataFileWr = open('database.txt', 'w')
dbread = dataFile.read()


def userCheck(uC_name):
    if uC_name in dbread:
        return f"Welcome, {username}"
    else:
        return f"Sorry, '{username}' is not a registered username,\nWould you like to register? (Yes/No)"

def register(reg_name):
    ask = input("-> ")
    askLow = ask.lower()
    if askLow[:1] == "n":
        return f"Terminating Program!"
    else:
        dataFileWr.write(f"\n{username}")
        print("Attempted to Add to file")

# Main Program
for i in range(4):
    if i == 3: # if had 3 attemps end
        print("no")
    else:
        username = input(f"{debug}\nPlease enter your username\n-> ")
        res = userCheck(username)
        print(res)
        if res == f"Sorry, '{username}' is not a registered username,\nWould you like to register? (Yes/No)":
            reg = register(username)
    if debug == True:
        print(f"Debug: {i}")