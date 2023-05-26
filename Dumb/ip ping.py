'''
This was made to have no real purpose
But it pings all ipv4 addresses - Its kinda designed to find open ips that can ping
09/05/2023
'''
import requests
import time
import threading

blocks1 = [0,0,0,10, False]# Its backwards

works = []

def test(ip):
    if ip != "http://0.0.0.0":
        try:
            res = requests.get(ip, timeout=2) # May have to use CMD to ping which means this not gonna workies - Good for finding websites tho ig
            works.append(ip[7:])
            return [True, res.status]
        except Exception as e:
            return f"Invalid IP / Error / Unreachable / Timeout / Basicly useless ip / {ip}"

def check():
    return False
    t = 0
    for i in blocks1:
        if i == 255:
            t += 1
    if t >= 4:
        blocks[4] = True
    else:
        blocks[4] = False


while blocks1[4] != True:

    for this1 in range(len(blocks1)):
        if blocks1[this1] == 255:
            if check():
                break
            blocks1[this1] = 0
            blocks1[this1+1] += 1
    blocks1[0] += 1

    print(test(f"http://{blocks1[3]}.{blocks1[2]}.{blocks1[1]}.{blocks1[0]}"))
