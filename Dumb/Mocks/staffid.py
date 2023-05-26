surname = input("Enter Surname\n-> ")
year = input("Ender Starting Year\n-> ")
staffID = surname + str(year)
while len(staffID) < 10:
    staffID = staffID + "x"
print("ID "+ staffID)