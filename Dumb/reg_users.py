# 19/11/2021

reg_users = ["reg1","reg2","reg3","reg4"]

check_reg = input("What is your name?\n-> ")

if check_reg in reg_users:
    print("\n\nHello, " + check_reg + "!\nYou are already registered!\n\n")
else:
    reg_y_n = bool(input("\n\nSorry, " + check_reg + "!\nYou are not registered!\nWould you like to register? (true/false)\n-> "))

if reg_y_n == True:
    name = input("\n\nPlease Enter Your Name\n-> ")
else:
    print("Goodbye!")