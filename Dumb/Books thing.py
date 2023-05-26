#26/01/2022
#27/01/2022

#imports
import random
import time
while True:
    # student or teacher kinda self explanitory
    p_t = input("Student or Teacher?\n-> ")
    p_tu = p_t.upper()
    p_t2 = p_tu[0:1]

#checking there input

    if p_t2 == "T": #teacher stuff
        print("Teacher")
    elif p_t2 == "S": # student stuff
        print("student")
        YS = input("What Year Did You Start High School?\n-> ")
        YG = input("What Year Are You In? (7, 8, 9, 10, 11)\n-> ")
        FirstName = input("First Name\n-> ")
        LastName = input("Last Name\n-> ")

        s_user = FirstName[0:1] + LastName + YS[2:4]
        print("\n\nUsername:", s_user)
        #First letter upper
        s_ln_2 = LastName[0:1]
        s_ln = s_ln_2.upper()

        #00Year(Number Here)
        s_code1 = random.randint(100,999)
        s_code = str(s_code1)

        s_pass = YG[0:2] + s_ln + LastName[1:4] + s_code
        print("Password:", s_pass)

        #Email Stuff
        print("Email:", s_user + "@stu.todhigh.co.uk\n\n")
        time.sleep(10)

    else:
        print("\nInvalid Input\n")