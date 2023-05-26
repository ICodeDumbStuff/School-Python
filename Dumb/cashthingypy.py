correct_pin = int("123")

# 19/11/2021

reg_users = ["reg1","reg2","reg3","reg4"]

check_reg = input("What is your name?\n->")

if check_reg in reg_users:
    print("\n\nHello, " + check_reg + "!\nYou are already registered!\n\n")
else:
    print("\n\nSorry, " + check_reg + "!\nYou are not registered!\nWould you like to register? (Y/N)\n->\n\n")

for i in range(3):
    user_pin = int(input("Enter Pin\n->"))
    if user_pin == correct_pin:
        print ("Correct")
        break
    else:
        if i == 2:
            print("Sorry you have exceeded your maximum attempts")
            break
        else:
            print("Incorrect")

#Rest of the program

print("You are in this is the end of the program byeeeeeeeeee")