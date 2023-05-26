def user_name(un_name, un_year):
    unsl_name = un_name[0:3]
    return f"{unsl_name}{un_year}"
name = input("First Name\n-> ")
year = input("Year of Birth\n-> ")
getUn = user_name(name, year)
print(f"Username: {getUn}")