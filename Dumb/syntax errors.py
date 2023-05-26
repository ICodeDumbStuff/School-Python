def sqlSanatiser(x):
    #Removes SQL key words from inputs
    x = x.strip("SELECT")
    return x

def upperCaseChecker(x):
    #Checks if a password contains an uppercase letter
    for i in x:
        if i.isupper():
            return True
    return False

#Main program
password = input("Please enter your username ")
sqlCheck = sqlSanatiser(password)
upperCaseChecker = upperCaseChecker(sqlCheck)
print(sqlCheck,upperCaseChecker)