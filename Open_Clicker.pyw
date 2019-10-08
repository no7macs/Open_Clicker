#!/bin/pyton3
import pyautogui, sys, time, keyboard, subprocess, csv, os, mouse
from tkinter import *
import tkinter
import win32api, win32con

#Gravina's INFINITY
root = Tk()
root.title("Open Clicker")
root.geometry("500x250")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Data/favicon.png'))

simpleclick = Frame(root)
simpleclick.pack(side = LEFT)

advancedclick = Frame(root)
advancedclick.pack(side = RIGHT)

startstop = Frame(root)
startstop.pack(side = BOTTOM)

running = 'False'  # Global flag

def scanning():

    #checks to see if a hotkey is pressed
    if keyboard.is_pressed(starthotkey):
        startclicking()

    elif keyboard.is_pressed(stophotkey):
        stopclicking()

    if keyboard.is_pressed(reloadfile):
        reload()

    if running == 'True':  # Only do this if the Stop button has not been clicked
        if delaybartype == '1': timeout = (((2)/(cpsval.get()) - 0.001))
        else: timeout = (int(2)/int(cpsval) - 0.001) 
        time.sleep(timeout)

        if buttonvar1.get() == 1:
                x = int()
                y = int()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                if doubleleftclickval.get() == 1:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                        
        if buttonvar2.get() == 1:
            x = int()
            y = int()
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
            if doubleleftclickval.get() == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
        else: print("ERROR")

    root.after(1, scanning)

def stopclicking():
    global running
    running = 'False'
    label.config(text = "Currently:OFF")
def startclicking():
    global running
    running = 'True'
    label.config(text = "Currently:ON")

def reload():
    path = "./Data/Reload/"
    os.chdir(path)
    os.startfile("Reload.exe")
    os.chdir("../../../")
    sys.exit()

def hotkeysettings():
    path = "./Data/Hotkey/Hotkey/" 
    os.chdir(path)
    os.startfile("HotKey.exe")
    os.chdir("../../../")

def opensettings():
    global changesettingsydir
    path = "./Data/Settings/Settings/"
    os.chdir(path)
    changesettingsydir = 'True'
    os.startfile("Settings.exe")
    os.chdir("../../../")

#loads settings file
methoddata = []
delaybartype = []
filename = "./Data/Settings/Settings.txt"
with open(filename) as f:
    for line in f:
        methoddata.append([str(n) for n in line.strip().split(',')])
for pair in  methoddata:
    try:
        delaybartype = pair[0]
    except IndexError:
        print ("ERROR")

cpsval = IntVar()
cpslabel = Label(simpleclick, text='Clicks Per Second')
cpslabel.pack(anchor=W)
if delaybartype == '1':
    cpsscale = Scale(simpleclick, var=cpsval, orient=HORIZONTAL)
    cpsscale.pack(anchor=W)
elif delaybartype == '2':
    cpsinput = Entry(simpleclick, bd = 5, width = 15)
    cpsinput.pack(anchor=W)

else: print("ERROR")

buttonvar1 = IntVar()
buttonvar2 = IntVar()

Buttonlabel = Label(simpleclick, text = "What buttons to press")
LCButton = Checkbutton(simpleclick,text="Left Mouse Button", variable=buttonvar1)
RCButton = Checkbutton(simpleclick,text="Right Mouse Button", variable=buttonvar2)
Buttonlabel.pack(anchor = CENTER)
LCButton.pack(anchor = CENTER)
RCButton.pack(anchor = CENTER)

#Start Stop
start = Button(startstop, text = "Start", justify = LEFT, command = startclicking)
start.pack(anchor=CENTER)
stop = Button(startstop, text = "Stop", justify = LEFT, command = stopclicking)
stop.pack(anchor=CENTER)

hotkey = Button(startstop, text = "Hotkey Settings", justify = LEFT, command = hotkeysettings)
hotkey.pack(anchor=CENTER)

settingsbutton = Button(startstop, text = "Settings", justify = LEFT, command = opensettings)
settingsbutton.pack(anchor=CENTER)

label = Label(startstop, text = "Currently:OFF")
label.pack(anchor = CENTER)

#creates double click radio buttons
doubleleftclickval = IntVar()
Doubleleftclick = Checkbutton(advancedclick, text="Double Left Click", justify = LEFT, variable=doubleleftclickval)
Doubleleftclick.pack(anchor = W)

doublerightclickval = IntVar()
Doublerightclick = Checkbutton(advancedclick, text="Double Right Click", justify = LEFT, variable=doublerightclickval)
Doublerightclick.pack(anchor = W)

#loads the hotkey file 
filename = "./Data/Hotkey/Hotkey.txt"
hotkeys = []
with open(filename) as f:
    for line in f:
        hotkeys.append([str(n) for n in line.strip().split(',')])
for pair in hotkeys:
    try:
        starthotkey,stophotkey,reloadfile = pair[0],pair[1],pair[2]
    except IndexError:
        print ("ERROR")
f.close()

root.after(1000, scanning)
root.mainloop()
