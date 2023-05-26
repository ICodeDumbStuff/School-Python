age = int(input("What is your age\n-> "))
gender = input("What is your gender\n-> ")

if age <= 20:
    Dose = age * 0.1
else:
    Dose = 2

if gender[0:1].lower == "f":
    ispregnant = input("Is u with child\n-> ")
    if ispregnant == True and Dose > 1.5:
        Dose = 1.5
else:
    Dose = Dose * 0.5
#end
print(Dose)