def letter_check(yes):
    #Checks the first letter and returns the words from a list
    words = ["sand","lake","friend","french","fly"]

    output = []

    #if stuffs
    for x in words:
        if yes == x[0:1]:
            output.append(x)
    if output == "":
        return f"sorry, there are no words with the letter: {yes}"
    else:
        return output
#Main program
letter = input("Enter letter\n-> ")
res = letter_check(letter)
print(res)