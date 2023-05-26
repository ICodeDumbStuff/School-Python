from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import tkinter
import threading
from PIL import Image, ImageTk
import time
import datetime

quitRows = 0

def uptClock():
    while True:
        time.sleep(0.5)
        ttk.Label(frm, text=f"{datetime.datetime.now().strftime('%X')}").grid(column=0, row=quitRows)

root = Tk()

frm = ttk.Frame(root, padding=100)
frm.grid()
root.title("Clock")

ttk.Label(frm, text=f"hi").grid(column=0, row=quitRows)

def run():
    t = threading.Thread(target=uptClock)
    t.start()
run()
print("hi12")
root.mainloop() | run()