#
# Website Status Checker
#

import requests
import time

class opt:
    timeout = 3
    consoleTitle = "Web Status"
    class webhook:
        discord = False

def getStatus(URL):
    try:
        r = requests.get(URL, timeout=opt.timeout)
        if r.status_code == 200:
            return [r.status_code, "✅ ONLINE  │"]
        else:
            return [r.status_code or None, "🟨 ERROR   │"]
    except Exception as e:
        return [None, "❌ OFFLINE │", e]

def coolMsg(title, data):
    def spaces(len, max):
        spc = ""
        for i in range((max+2)-len):
            spc = f"{spc} "
        return spc
    def dashes(num, pos):
        if pos == "top":
            out = "───┬───────────┤"
            for i in range(num):
                out = f"─{out}"
            return f"├{out}"
        elif pos == "bottem":
            out = "───┴───────────┘"
            for i in range(num):
                out = f"─{out}"
            return f"└{out}"
        elif pos == "toptop":
            out = "───────────────┐"
            for i in range(num):
                out = f"─{out}"
            return f"┌{out}"




    def center(text, totlen):
        center = totlen // 2
        centext = len(text) // 2
        math = center-centext-1
        for i in range(math):
            text = f" {text} "
        if math % 2 != 0:
            text = f"{text} "
        return f"│{text}│"
    x = 0
    for i in data:
        if len(i) > x:
            x = len(i)

    output = []
    output.append(dashes(x, "toptop"))
    output.append(center(title, len(dashes(x, 'top'))))
    output.append(dashes(x, 'top'))
    for i in data:
        output.append(f"│ {i}{spaces(len(i),x)}│{data[i][1]}")
    output.append(f"{dashes(x, 'bottem')}")
    return output




class storage:
    Sites = {
            "Github":"https://github.com",
            "GitHub API":"https://api.github.com",
            "SMP Map":"http://fn-hlk-1.viteza.cloud:25580",
            "SMP Node":"http://fn-hlk-1.viteza.cloud",
            }
    Status = {}

def run():
    for i in storage.Sites:
        storage.Status[i] = getStatus(storage.Sites[i])

    for i in coolMsg(opt.consoleTitle, storage.Status):
        print(i)
    time.sleep(10)
run()