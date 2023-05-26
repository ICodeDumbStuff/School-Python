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

dbUsers = ["Alex", "Cool", "Python", "C-Sharp", "Java", "JavaScript"]
dataFile = open('database.txt', 'r')
dbUsers2 = [datafile]

def userCheck(uC_name):
    if uC_name in dbUsers:
        return f"Welcome, {username}"
    else:
        return f"Sorry, '{username}' is not a registered username,\nWould you like to register? (Yes/No)"

def register(reg_name):
    ask = input("\n-> ")
    askLow = ask.lower()
    if askLow[:1] == "n":
        return f"Terminating Program!"
    else:
        dataFile = open(database.txt)
        dbUsers2

# Main Program
for i in range(4):
    if i == 3:
        print("no")
    else:
        username = input(f"{debug}\nPlease enter your username\n-> ")
        res = userCheck(username)
        print(res)
        if res == f"Sorry, '{username}' is not a registered username,\nWould you like to register? (Yes/No)":
            reg = register(username)
    if debug == True:
        print(f"Debug: {i}")