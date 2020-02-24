#!/bin/pyton3
import sys, os
from tkinter import Tk, Label, Button, Entry, PhotoImage, CENTER, END
from PIL import ImageTk, Image
import Open_Clicker

def save():
    hotkeyfile = open("./Hotkey.txt", "w")
    hotkeyfile.write(Startentry.get()+','+Stopentry.get())
    done()

def done():
    #os.chdir('../../main/Open_Clicker')
    #os.startfile('Open_Clicker.exe')
    #os.chdir('../../Hotkey/Hotkey')
    #sys.exit()
    root.destroy()
    Open_Clicker.main()

def main(startpresettext, stoppresettext):  
    global Startentry
    global Stopentry
    global root

    root = Tk()
    root.title("Open Clicker Hotkey Settings")
    #root.geometry("500x350")
    #root.geometry("300x200")
    root.resizable(0,0)
    #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    #Create Gui
    Startlabel = Label(root, text = "Start Hotkey")
    Startlabel.pack(anchor = CENTER)

    Startentry = Entry(root, bd = 5)
    Startentry.pack(anchor = CENTER)

    Stoplabel = Label(root, text = "Stop Hotkey")
    Stoplabel.pack(anchor = CENTER)

    Stopentry = Entry(root, bd = 5)
    Stopentry.pack(anchor = CENTER)

    Done = Button(root, text = "Done", command = save)
    Done.pack(anchor = CENTER)

    Cancel = Button(root, text = "Cancel", command = done)
    Cancel.pack(anchor = CENTER)

    Info1 = Label(root, text = "For special keys like enter, spell out the word in the box.")
    Info2 = Label(root, text = "ex: enter, tab, ctrl, shift, backspace, del, f5, f3")
    Info1.pack(anchor = CENTER)
    Info2.pack(anchor = CENTER)

#    filename = "./Hotkey.txt"
#    hotkeys = []
#    with open(filename) as f:
#        for line in f:
#            hotkeys.append([str(n) for n in line.strip().split(',')])
#    for pair in hotkeys:
#        try:
#            startpresettext,stoppresettext = pair[0],pair[1]
#        except IndexError:
#            print ("ERROR")
#    f.close()

    Startentry.delete(0,END)
    Startentry.insert(0,startpresettext)

    Stopentry .delete(0,END)
    Stopentry .insert(0,stoppresettext)

    root.mainloop()