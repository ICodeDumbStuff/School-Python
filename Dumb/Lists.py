def linearSearch(theList, toFind):
    for x in range(len(theList)):
        if theList[x] == toFind:
            return f"The position is: {x}"
    else:
        return "Sorry wasn't in list"

mylist = [234,23,156,126,58]
find = int(input("Enter number \n-> "))
print(linearSearch(mylist, find))