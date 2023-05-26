# Prices
c = 2.50
a = 4.50
f = a + a + c + c
s = 4.50*0.5

def canRide(r_age, r_height):
    if r_age > 10:
        if r_height >= 150:
            return True
    return False

def isStu():
    q = input("Are you in full time education? (Yes/No)\n-> ")
    q = q[:1]
    q = q.lower()
    if q == "y":
        return True
    return False

def isFam():
    pass

def ticketPrice(tp_age, tp_check):
    if tp_check == True:
        return s
    if tp_age <= 15:
        return c
    if tp_age >= 16:
        return a



# Main Program
age = int(input("Please enter your age\n-> "))
height = int(input("Please enter your height (cm)\n-> "))
res = canRide(age, height)

if res == True:
    check = isStu()
    check2 = isFam()
    res = ticketPrice(age, check)
else:
    print("Not allowed")

print(res)

