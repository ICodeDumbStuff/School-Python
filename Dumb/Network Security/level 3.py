db = ["abc", "aro", "zhe"] # Very real
def username(first, last):
    # first letter frst name, first two of surname = username, if exists first two first, first one surname
    first1 = first[:1]
    last1 = last[:2]
    username = f"{first1}{last1}"
    if username in db:
        first1 = first[:2]
        last1 = last[:1]
        return f"{first1}{last1}"
    return username
# Main program
firstnm = input("First Name\n-> ")
surname = input("Surname\n-> ")
res = username(firstnm, surname)
print(res)