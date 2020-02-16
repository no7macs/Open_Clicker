#!/bin/python3
import sys, keyboard, csv, os, gc, time
import win32api, win32con
from multiprocessing import Process
from tkinter import Tk, Button, Label, Scale, Entry, Checkbutton, PhotoImage, Frame, LEFT, RIGHT, BOTTOM, HORIZONTAL, CENTER, IntVar, W, S
import HotKey
import About
def stopclicking():
    global running
    running = False
    label.config(text = "Currently:OFF")
    timeout = ((int(cpsval.get()))/int(1000))
    print(timeout)
    scanning()

def startclicking():
    global running
    global timeout
    running = True
    label.config(text = "Currently:ON")
    timeout = ((int(cpsval.get()))/int(1000))
    print(timeout)
    scanning()

def hotkeysettings(starthotkey, stophotkey):
    #path = "./Data/Hotkey/Hotkey/" 
    #os.chdir(path)
    #os.startfile("HotKey.exe")
    #os.chdir("../../../")
    #sys.exit()
    root.destroy()
    HotKey.main(starthotkey, stophotkey)

def openabout():
    #path = "./Data/Settings/Settings/"
    #os.chdir(path)
    #os.startfile("Settings.exe")
    #os.chdir("../../../")
    #sys.exit()
    root.destroy()
    About.main()
    
def scanning():
    if keyboard.is_pressed(starthotkey): startclicking()

    elif keyboard.is_pressed(stophotkey): stopclicking()

    if running == True:  # Only do this if the Stop button has not been clicked
        if buttonvar1.get() == 1:
            x = int()
            y = int()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
            time.sleep(timeout)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        else: print("no LCB")
                        
        if buttonvar2.get() == 1:
            x = int()
            y = int()
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
            time.sleep(timeout)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
        else: print("no RCB")
        root.after(1, scanning)
    else: root.after(100, scanning)


def main():
    global root
    global starthotkey, stophotkey, buttonvar1, buttonvar2, label, cpsval, running
    root = Tk()
    root.title("Open Clicker")
    root.geometry("525x250")
    #root.geometry("262x125")
    root.resizable(0,0)
    #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Data/Images/favicon.png'))

    simpleclick = Frame(root)
    simpleclick.pack(side = LEFT)

    advancedclick = Frame(root)
    advancedclick.pack(side = RIGHT)

    info = Frame(root)
    info.pack(side = BOTTOM)

    settingsframe = Frame(root)
    settingsframe.pack(side = BOTTOM)

    startstop = Frame(root)
    startstop.pack(side = BOTTOM)

    running = False  # Global flag

    cpsval = IntVar()
    cpslabel = Label(simpleclick, text='Click interval')
    cpslabel.pack(anchor=W)

    cpsscale = Scale(simpleclick, from_=1, to=1000, var=cpsval, orient=HORIZONTAL, length = 125)
    cpsscale.pack(anchor=W)

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
    start.pack(side=LEFT)
    stop = Button(startstop, text = "Stop", justify = LEFT, command = stopclicking)
    stop.pack(side=LEFT)

    #settings and info
    hotkey = Button(settingsframe, text = "Hotkey", justify = LEFT, command = lambda: hotkeysettings(starthotkey, stophotkey))
    hotkey.pack(side=LEFT)
    settingsbutton = Button(settingsframe, text = "About", justify = LEFT, command = openabout)
    settingsbutton.pack(side=LEFT)

    label = Label(info, text = "Currently:OFF")
    label.pack(anchor = S)

    #loads the hotkey file 
    filename = "./Hotkey.txt"
    hotkeys = []
    with open(filename) as f:
        for line in f:
            hotkeys.append([str(n) for n in line.strip().split(',')])
    for pair in hotkeys:
        try:
            starthotkey,stophotkey = pair[0],pair[1]
        except IndexError:
            print ("ERROR")
    f.close()

    if starthotkey == ("") or stophotkey == (""):
        print("Hotkey not loaded")
    else: print("Properly loaded hotkeys")

    #gc.collect()

    root.after(1000, scanning)
    root.mainloop()