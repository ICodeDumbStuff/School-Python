#02/03/2022

#Imports
from array import * #Not using this In this code

def validDiscount(discCode):

    ValidCodes = {"PVFC7":10,"CPU5":5,"BGF2":15}

    if (discCode in ValidCodes):
        return ValidCodes[discCode]
    else:
        return 0

def checkDiscount(price, discounted):
    newprice = price - discounted
    return newprice

leinput = input("Please Enter Your Discount Code!\n -> ")
price_pass = 100.00
checked = validDiscount(leinput)

if checked != 0:
    print("Price: " + str(checkDiscount(price_pass, checked)))
else:
    print("Invalid Discount Code")