import time
z = 0
while True:
    z += 1
    x = z
    y = 0
    while x > 0:
        y += 1
        x -= y
    print(y)