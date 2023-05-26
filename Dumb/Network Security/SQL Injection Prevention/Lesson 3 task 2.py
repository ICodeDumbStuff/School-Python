def password_checker(passw):
    # check password
    # get len
    length = len(passw)
    if length <= 8:
        if  "!" in passw or "$" in passw:
            return "Passed"
    return "not passed"
# Main Program
for i in range(4):
    left = 3 - i
    if left == 0:
        print("No Attempts Left")
    else:
        password = input(f"\n\n\n\n\nPlease enter your password\nAttempts Remaining: {left}\n-> ")
        result = password_checker(password)
        print(result, left)