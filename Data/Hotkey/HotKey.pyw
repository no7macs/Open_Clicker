#!/bin/pyton3
import pyautogui, sys
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import keyboard
import os
import time

root = Tk()
root.title("Open Clicker Hotkey Settings")
root.geometry("500x350")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='../../favicon.png'))

def save():
    hotkeyfile = open("../Hotkey.txt", "w")
    hotkeyfile.write(Startentry.get()+','+Stopentry.get()+','+Reloadentry.get())
    sys.exit()
def done():
    sys.exit()
    
#Create Gui
Startlabel = Label(root, text = "Start Hotkey")
Startlabel.pack(anchor = CENTER)

Startentry = Entry(root, bd = 5)
Startentry.pack(anchor = CENTER)

Stoplabel = Label(root, text = "Stop Hotkey")
Stoplabel.pack(anchor = CENTER)

Stopentry = Entry(root, bd = 5)
Stopentry.pack(anchor = CENTER)

Reloadlabel = Label(root, text = "Reload Program")
Reloadlabel.pack(anchor = CENTER)

Reloadentry = Entry(root, bd = 5)
Reloadentry.pack(anchor = CENTER)

Done = Button(root, text = "Done", command = save)
Done.pack(anchor = CENTER)

Cancel = Button(root, text = "Cancel", command = done)
Cancel.pack(anchor = CENTER)

Info1 = Label(root, text = "For special keys like enter, spell out the word in the box.")
Info2 = Label(root, text = "ex: enter, tab, ctrl, shift, backspace, del, f5, f3")
Info1.pack(anchor = CENTER)
Info2.pack(anchor = CENTER)

filename = "../Hotkey.txt"
hotkeys = []
with open(filename) as f:
    for line in f:
        hotkeys.append([str(n) for n in line.strip().split(',')])
for pair in hotkeys:
    try:
        startpresettext,stoppresettext,reloadpresettext = pair[0],pair[1],pair[2]
    except IndexError:
        print ("ERROR")

Startentry.delete(0,END)
Startentry.insert(0,startpresettext)

Stopentry .delete(0,END)
Stopentry .insert(0,stoppresettext)

Reloadentry .delete(0,END)
Reloadentry .insert(0,reloadpresettext)

root.mainloop()

