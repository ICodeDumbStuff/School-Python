# Blank Int Vari
a = 0
b = 0
c = 0
d = 0
e = 0

def canRide(r_age, r_height):
    if r_age <= 10:
        if r_height <= 150:
            return True
    return False

def checkRiders(under16, over16, fam, stu):
    if under16 != 0:
        for i in under16:
            x = i + 1
            age = int(input(f"Please enter age of child {x}\n-> "))
            height = int(input(f"Please enter your height (cm)\n-> "))
            res = canRide(age, height)
            a = a + 1
    if over16 != 0:
        for i in under16:
            x = i + 1
            height = int(input(f"Please enter height of Adult {x} (cm)\n-> "))
            res = canRide(16, height)
            b = b + 1

    return f"{a} and {b}"


# Main Program
'''age = int(input("Please enter your age\n-> "))
height = int(input("Please enter your height (cm)\n-> "))
res = canRide(age, height)
print(res)'''

child = int(input("How Many Children (under 16)\n-> "))
adult = int(input("How Many Adults (over 16)\n-> "))
family = int(input("How Many Family (2x Adult, 2x Child)\n-> "))
student = int(input("How Many Students (over 16, full time education\n-> "))
res = checkRiders(child, adult, family, student)
print(res)

