#Imports
import time
import random
# RandInt Function
def RandInt(a, b):
    output = random.randint(a, b)
    return output
#Inputs
age = int(input("Please Enter Your Age!\n-> "))
daymonth = int(input("Please The Day Of The Month!\n Example: 09/02/2022 (dd/mm/2022)\n It Would Be 09 **09**/02/22\n-> "))
#This = Nothing for now
select = input("What Do You Want Do To With The Numbers?")
# RandInt Print
print("Your Random Int Is:", RandInt(age, daymonth))