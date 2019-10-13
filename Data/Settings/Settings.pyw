import pyautogui, sys, time, keyboard, subprocess, csv, os
from tkinter import *
import tkinter
import gc, webbrowser

root = Tk()
root.title("Settings")
root.geometry("500x250")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='../../favicon.png'))

methodframe = Frame(root)
methodframe.pack(side = LEFT)
donecancel = Frame(root)
donecancel.pack(side = BOTTOM)

def scanning():

    root.after(1, scanning)

def save():
    delayinputtypesave = (str(delayinputval.get()))
    settingsfile = open("../Settings.txt", "w")
    settingsfile.write((delayinputtypesave))
    gc.collect()
    sys.exit()
def done():
    gc.collect()
    sys.exit()

def scriptbotlink():
    webbrowser.open('https://script-bot.netlify.com')

def githublink():
    webbrowser.open('https://github.com/no7macs/Open_Clicker')

#loads settings file
method = IntVar()
delayinputtype = IntVar()
filename = "../Settings.txt"
methods = []
with open(filename) as f:
    for line in f:
        methods.append([str(n) for n in line.strip().split(',')])
for pair in methods:
    try:
        delayinputtype = pair[0]
    except IndexError:
        print ("ERROR")

#creates delay input method ui
delayinputval = IntVar()
delayinputval.set(delayinputtype)
delayinputlabel = Label(methodframe, text = "CPS Input Type")
delayinputlabel.pack(anchor = W)
delayinputmethod1 = Radiobutton(methodframe, text = "Slide Bar", variable=delayinputval, value=1)
delayinputmethod1.pack(anchor = W)
delayinputmethod2 = Radiobutton(methodframe, text = "Input Boxes", variable=delayinputval, value=2)
delayinputmethod2.pack(anchor = W)

#creates done and cancel buttons
Done = Button(donecancel, text = "Done", command = save)
Done.pack(anchor = CENTER)
Cancel = Button(donecancel, text = "Cancel", command = done)
Cancel.pack(anchor = CENTER)

#Site Link Button
scriptbot = Button(root,justify = LEFT, command = scriptbotlink )
scriptbotphoto=PhotoImage(file="../../logo.png")
scriptbot.config(image=scriptbotphoto)
scriptbot.pack(anchor=E)

#git link button
github = Button(root,justify = LEFT, command = githublink )
githubphoto=PhotoImage(file="../../github.png")
github.config(image=githubphoto)
github.pack(anchor=E)

root.after(1000, scanning)
root.mainloop()
