import time
slep = 0
l = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
while True:
    for i in range(len(l)):
        time.sleep(slep)
        l[i] = "█"
        for i in l:
            print (i,end="")
        print ("")
    for i in range(len(l)):
        time.sleep(slep)
        l[(len(l)-i-1)] = "🨇"
        for i in l:
            print (i,end="")
        print ("")