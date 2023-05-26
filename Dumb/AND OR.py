# Importsssssssssss
import time

def customer_check (ccheck_age):
    if ccheck_age >= 15:
        ccheck_output = "You Are old Enough To Watch The Film,"
        return ccheck_output
    else:
        ccheck_output = "You Are Younger Than 15 And Cannot See The Film!"
        return ccheck_output

def yes_no (yn_input):
    yn_format = yn_input.upper()
    yn_slice = yn_format[0:1]
    if yn_slice == "Y":
        yn_out = "You Are Allowed To Enter"
    elif yn_slice == "N":
        yn_out = "You Need To Have The Money To Buy A Ticket Before You Can Enter The Film!"
    else:
        yn_out = "Invalid Input!"
    return yn_out

#Main program here. Call your function from here
age = int(input("What is your age?\n-> "))


if customer_check(age) == "You Are old Enough To Watch The Film,":
    ticket = input("Do You Have A Ticket? (Yes/No)\n-> ")
    print(yes_no(ticket))
else:
    print("You Arnt Old Enough!")