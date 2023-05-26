#15/12/2021
#Topic Test
while True:
    l1 = int(input("Length 1 =\n-> "))
    l2 = int(input("Length 2 =\n-> "))
    l3 = int(input("Length 3 =\n-> "))
    if l1 == l2:
        print("Isosceles")
    elif l1 == l3:
        print("Isosceles")
    elif l2 == l3:
        print("Isosceles")
    else:
        print("Not Isosceles")