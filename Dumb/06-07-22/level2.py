def canRide(r_age, r_height):
    if r_age <= 10:
        if r_height <= 150:
            return "Allowed"
    return "Not allowed"
# Main Program
age = int(input("Please enter your age\n-> "))
height = int(input("Please enter your height (cm)\n-> "))
res = canRide(age, height)
print(res)