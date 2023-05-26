def libarycode(title, year):
    parta = title[0:3]
    partb = year[2:]
    out = f"{parta.upper()}{partb}"

    f = open("bookcodes.txt", "a")
    f.write(f"{out}, ")
    f.close()

    return out
print(libarycode(input("title\n->"),input("year")))
