import time
import random

bestHigh = 0
bestLow = 0

timeSlep = 0

stop = False

while True:

    tryget = 10000
    attemps = 0
    num = 0

    while num != tryget:
        attemps = attemps + 1
        num = random.randint(0, tryget)
        if num == tryget:
            print("\nTrying:", tryget, "\nAttemps:", attemps, "\nbestHigh:", bestHigh, "\nbestLow:", bestLow)

            if bestHigh < attemps:
                bestHigh = attemps
            if bestLow > attemps:
                bestLow = attemps
            if bestLow == 0:
                bestLow = attemps
    time.sleep(timeSlep)

    if bestLow == 1 and stop == True:
        break
print("One Attempt Coool")