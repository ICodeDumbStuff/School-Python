#Import Stuffs
import time

# Important Stuffs from document
#
# 1% = 10 Min charge
# 80% - 100% = 200 Min Charging
# Output Full When == 100

#Var's
timslep = 1

#Debug enabled?
# 1 = Yes
# 0 = No
debug = 0

#just so can repeat Stuffs
while True:
    #Inputs
    charge = int(input("How Charged Is The Battery? ( !! Without % !! )\n-> "))

    #Computer go brrrrrr
    if charge == 100:
        print("The Battery Is Fully Charged!")
        time.sleep(timslep)
    else:
        ans = 100 - charge
        mins = ans * 10
        fulltim = mins/60

        print("It will take:", mins, "Minutes, to charge the car!")
        time.sleep(timslep)

        if debug == 1:
            #Me Dubug my var's at end of code :D
            print("\n##################\n# IGNORE THIS\n# Debug Info:\n# Ans:", ans, "\n# Time:", mins, "Minutes\n# Formatted:", fulltim, "\n##################\n")
            time.sleep(timslep)