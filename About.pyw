import sys, os, webbrowser
from tkinter import Tk, Frame, Label, Button, PhotoImage, LEFT, BOTTOM, Radiobutton, IntVar, W, E, CENTER 
import tkinter
import Open_Clicker

def scriptbotlink():
    webbrowser.open('https://script-bot.netlify.com')

def githublink():
    webbrowser.open('https://github.com/no7macs/Open_Clicker')

def Done():
    root.destroy()
    Open_Clicker.main()

def main():
    global delayinputval
    global root
    root = Tk()
    root.title("About")
    #root.geometry("500x250")
    #root.geometry("262x200")
    root.resizable(0,0)
    #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='../../Images/favicon.png'))
    
    about = Frame(root)
    about.pack(side = LEFT)
    donecancel = Frame(root)
    donecancel.pack(side = BOTTOM)

    creator = Label(about, text = "Made by no7mac for script-bot")
    creator.pack(anchor = W)

    done = Button(donecancel, text = "Done", command = Done)
    done.pack(anchor = W)

    #Site Link Button
    scriptbot = Button(root,justify = LEFT, command = scriptbotlink )
    scriptbotphoto=PhotoImage(file="./Data/Images/logo.png")
    scriptbot.config(image=scriptbotphoto)
    scriptbot.pack(anchor=E)

    #git link button
    github = Button(root,justify = LEFT, command = githublink )
    githubphoto=PhotoImage(file="./Data/Images/github.png")
    github.config(image=githubphoto)
    github.pack(anchor=E)

    #creates clear tmp file button
    #clrtmpbtn = Button(root,justify = LEFT, text = "Clear tmp data",command = cleartmp )
    #clrtmpbtn.pack(anchor=E)

    root.mainloop()
