from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import tkinter
import threading
from PIL import Image, ImageTk
import time

# python W:\ClickGam\idk.py
fileloc = "W:\\ClickGam\\"
#fileloc = "./"

class storage:
    cookies = 0
    shopOn = False
    acOn = False
    # Upgrades Format: ["Name",MaxCanHave,AmountHave,IncreaseCpsBy,InitialPrice,IncreaseCostBy,poslist]
    upgrades = [["Kitchen",0,0,1,100,200,0],["Worker",0,0,5,250,250,1],["Oven",0,0,10,500,750,2],]
    addition = 0

def saveQuit(load=None):
    if load == True:
        # Save Game Data
        saveData = []
        for i in storage.upgrades:
            saveData.append(i)

        # Write data to file
        with open(fileloc+"save.txt", "w") as f:
            f.write(f"{storage.cookies}\n")
            for data in saveData:
                for x in range(len(data)):
                    f.write(f"{str(data[x])},")
                f.write("\n")
            f.close()
    elif load == None:
        # Load Game Data
        with open(fileloc+"save.txt", "r") as f:
            saveData = []
            x = 0
            for line in f:
                if x == 0:
                    # then its line 1 and value is cookies
                    saveData.append(int(line))
                else:
                    items = line.split(",")
                    y = 0
                    upg = []
                    for ea in items:
                        if ea == "\n":
                            pass
                        else:
                            try:
                                upg.append(int(ea))
                            except:
                                upg.append(ea)
                            y += 1
                    saveData.append(upg)
                x += 1
            f.close()

        # Update game state
        storage.cookies = int(saveData[0])
        storage.upgrades = saveData[1:]
        uptstats()
        uptshop()

        storage.addition = 0
        for i in storage.upgrades:
            storage.addition += (i[2] * i[3])



def uptstats():
    # Update every version of stats where they have to be displayed like Main click page and shop
    ttk.Label(frm, text=f"{storage.cookies} Cookies\n\n").grid(column=0, row=1)
    ttk.Label(shop, text=f"{storage.cookies} Cookies\n\n").grid(column=0, row=0)

    storage.addition = 0x
    for i in storage.upgrades:
        print(i)
        storage.addition += (i[2] * i[3])
        print((i[2] * i[3]))
    print(f"Updated Addition: {storage.addition}")

def uptshop():
    y = 0
    for i in storage.upgrades:
        cost = i[4] + (i[5] * i[2])
        ttk.Button(shop, text=f"{i[0]}\n+{i[3]} Cookies/Click\nCost: {cost}", command=lambda x=i: upgrade(x)).grid(column=0,row=5+y)
        y += 1

def click():
    storage.cookies += (1 + storage.addition)
    uptstats()


def autoClick():
    if not storage.acOn:
        storage.acOn = True
        while storage.acOn == True:
            time.sleep(0.01)
            click()
    else:
        storage.acOn = False

def upgrade(data):
    print(f"Upgrading: {data}")

    # Upgrades Format: ["Name",MaxCanHave,AmountHave,IncreaseCpsBy,InitialPrice,IncreaseCostBy,poslist]

    cost = data[4] + (data[5] * data[2])
    if data[1] == 0:
        if storage.cookies >= cost:
            storage.cookies -= cost
            storage.upgrades[data[6]][2] += 1

        uptstats()
        uptshop()
        return

    if data[2] < data[1]:
        if storage.cookies >= cost:
            storage.cookies -= cost
            storage.upgrades[data[6]][2] += 1

        uptstats()
        uptshop()
        return

def shopOpen():
    if not storage.shopOn:
        storage.shopOn = True
        shop.grid()
        frm.grid_forget()
        ttk.Button(shop, text="Close Shop", command=shopOpen).grid(column=0, row=2)
        ttk.Label(shop, text="\n").grid(column=0, row=3)

        uptshop()
    else:
        shop.grid_forget()
        frm.grid()
        storage.shopOn = False

def quitAndSave():
    t = threading.Thread(target=autoClick)
    t.start()
    pass

root = Tk()

shop = ttk.Frame(root, padding=100)
shop.grid()

frm = ttk.Frame(root, padding=100)
frm.grid()
root.title("Click Ting")

image=Image.open(fileloc+'cookie.png')
img=image.resize((200, 200))
my_img=ImageTk.PhotoImage(img)

shopOpen() # Fix stats at top coz need to upt in shop aswell
shopOpen()

ttk.Button(frm, image=my_img, command=click).grid(column=0, row=3)
uptstats()
ttk.Button(frm, text="Shop", command=shopOpen).grid(column=0, row=16)

quitRows = 20
ttk.Label(frm, text="\n").grid(column=0, row=quitRows)
ttk.Button(frm, text="Save Game", command=lambda: saveQuit(True)).grid(column=0, row=quitRows+1)
ttk.Button(frm, text="Load Game", command=saveQuit).grid(column=0, row=quitRows+2)
ttk.Button(frm, text="Autoclicker", command=quitAndSave).grid(column=0, row=quitRows+3)


root.mainloop()