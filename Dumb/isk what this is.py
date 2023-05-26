import random
import time

i = int(0)
times = str(0)

while True:
    inttostringty = random.randint(1,6)
    rolleda = str(inttostringty)
    print ("Run " + times + " | Rolled: " + rolleda +"!")
    time.sleep(0.0)
    i = i + 1
    times = str(i)