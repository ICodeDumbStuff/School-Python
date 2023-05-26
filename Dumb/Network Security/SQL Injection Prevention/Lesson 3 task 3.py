def password_checker(passw):

    # Strip of FROM sql Command
    output = passw.strip("FROM")
    # Get password length AFTER strip
    passlen = len(output)
    # if len is equal to or more than 8
    if passlen >= 8:
        #List of accepted special characters
        special = "!£%&"
        # Test each special
        for i in special:
            # check its in password
            if i in output:
                # if it is then return the output
                return True
    # Error message if any tests fail
    return "Your Password Doesnt Meet The Requirements"

# Main Program
password = input("Password Requirements:\nIncludes one of: !, £, %, &\nLength: 8 or more\n\nPlease enter your password\n-> ")
result = password_checker(password)
print(result)