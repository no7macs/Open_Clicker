import time, sys, shutil
from sys import sys.exit
from shutil import shutil.rmtree
from os import os.startfile, os.chdir
from tkinter import *
import tkinter

root = Tk()
root.title("Clear")
root.geometry("300x150")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='../../Images/favicon.png'))

def main():
    warningmessagetitle = Label(root, text = "WARNING")
    warningmessagebody = Label(root, text = "This should only be done if Open_Clicker has crached")
    warningmessgaeend = Label(root, text = "Are you sire you want to continue?")
    Continue = Button(root, justify = LEFT, text = "Continue", command = start) 
    Cancel = Button(root, justify = LEFT, text = "Cancel", command = end)

    warningmessagetitle.pack(anchor = CENTER)
    warningmessagebody.pack(anchor = CENTER)
    warningmessgaeend.pack(anchor = CENTER)
    Continue.pack(anchor = CENTER)
    Cancel.pack(anchor = CENTER)
    root.after(1, main)
def end():
    os.chdir('./Settings')
    os.startfile('Settings.exe')
    sys.exit()
    
def start():
    os.chdir('../../')
    shutil.rmtree('./tmp', ignore_errors=False, onerror=None)
    time.sleep(2)
    os.makedirs('./tmp')
    sys.exit()

root.after(1000, main)
root.mainloop()