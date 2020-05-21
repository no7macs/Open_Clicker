#from tkinter import Tk, E, W, LEFT, RIGHT, TOP, CENTER, Entry, Button, Label, Scale, Checkbutton, Frame, IntVar, END, HORIZONTAL, PhotoImage
from tkinter import *
import webbrowser, keyboard
import win32api, win32con
#import changecpslimits
#from win32api import mouse_event
#from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP
#from win10toast import ToastNotifier
running = int(0)

def main(running):

    if lcbhotkey.get() != '':
        #if win32api.GetAsyncKeyState(ord(str(lcbhotkey.get()))) != 0: togglelcb()
        if keyboard.is_pressed(lcbhotkey.get()): togglelcb()
    if mcbhotkey.get() != '':
        #if win32api.GetAsyncKeyState(ord(str(mcbhotkey.get()))) != 0: togglemcb()
        if keyboard.is_pressed(mcbhotkey.get()): togglemcb()
    if rcbhotkey.get() != '':
        #if win32api.GetAsyncKeyState(ord(str(rcbhotkey.get()))) != 0: togglercb()
        if keyboard.is_pressed(rcbhotkey.get()): togglercb()

    x = int()
    y = int()
    if starthotkeyentry.get() != '':
        if keyboard.is_pressed(starthotkeyentry.get()): 
            running = int(1)
            win32api.Sleep(1000)
            #toaster.show_toast('Open_Clicker','Started', duration = 2, icon_path='./favicon.ico')
    if stophotkeyentry.get() != '': 
        if keyboard.is_pressed(stophotkeyentry.get()): 
            running = int(2)
            win32api.Sleep(1000)
            #toaster.show_toast('Open_Clicker','Stopped', duration = 2, icon_path='./favicon.ico')
    
    if running == 1:
        if lcbbuttonvar.get() == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
            win32api.Sleep(int(cpsvalue.get()))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

        if mcbbuttonvar.get() == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
            win32api.Sleep(int(cpsvalue.get()))
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)

        if rcbbuttonvar.get() == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
            win32api.Sleep(int(cpsvalue.get()))
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

        root.after(1,lambda: main(running))
        
    else: root.after(100,lambda: main(running))

def Start(running):
    running = int(1)
    print('START')
    #toaster.show_toast('Open_Clicker','Started', duration = 5, icon_path='./favicon.ico')
    root.after(100,lambda: main(running))

def Stop(running):
    running = int(2)
    print('STOP')
    #toaster.show_toast('Open_Clicker','Stopped', duration = 5, icon_path='./favicon.ico')
    root.after(100,lambda: main(running))

def sethotkey():
    hotkeyfile = open('./Settings.txt','w')
    hotkeyfile.write(starthotkeyentry.get() + '|' + stophotkeyentry.get() + '|' + lcbhotkey.get() + '|' + mcbhotkey.get() + '|' + rcbhotkey.get() + '|'+ settingslines[0].split('|')[5] + '|' + settingslines[0].split('|')[6])
    hotkeyfile.close()
    root.destroy()
    import main

def resethotkey(): 
    starthotkeyentry.delete(0,END)
    starthotkeyentry.insert(0,originstarthotkey)

    stophotkeyentry.delete(0,END)
    stophotkeyentry.insert(0,originstophotkey)

    lcbhotkey.delete(0,END)
    lcbhotkey.insert(0,originstophotkey)

    mcbhotkey.delete(0,END)
    mcbhotkey.insert(0,originstophotkey)

    rcbhotkey.delete(0,END)
    rcbhotkey.insert(0,originstophotkey)

def scriptbotlink():
    webbrowser.open('https://script-bot.netlify.com')

def togglelcb(): 
    lcbcheckbox.toggle()
    win32api.Sleep(200)
def togglemcb(): 
    mcbcheckbox.toggle()
    win32api.Sleep(200)
def togglercb(): 
    rcbcheckbox.toggle()
    win32api.Sleep(200)

def changecpslimits():
    win32api.Sleep(1000)
    root.destroy()
    win32api.Sleep(1000)
    #changecpslimits.main()
    import changecpslimits

#beutiful gui
root = Tk()
root.title('Open_Clicker 3')
root.config(bg = '#0F151D')
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

cpsframe = Frame(root, bg = '#0F151D')
cpsframe.pack(side = TOP)
otherstuffframe = Frame(root, bg = '#0F151D')
otherstuffframe.pack(side = TOP)
cbbuttonframe = Frame(root, bg = '#0F151D')
cbbuttonframe.pack(side = TOP)

#Start and Stop Hotkey frames
classichotkeyframe = Frame(otherstuffframe, bg = '#0F151D')
classichotkeyframe.pack(anchor = W)
startandstopframe = Frame(classichotkeyframe, bg = '#0F151D')
startandstopframe.pack(side = LEFT)
hotkeyframe = Frame(classichotkeyframe, bg = '#0F151D')
hotkeyframe.pack(side = LEFT)
setandresethotkeyframe = Frame(classichotkeyframe, bg = '#0F151D')
setandresethotkeyframe.pack(side = LEFT)

settingsfile = open('./Settings.txt','r')
settingslines = settingsfile.readlines()

cpsvalue = IntVar()
cpsvaluelabel = Label(cpsframe, text = 'CPS value', bg = '#0F151D', fg = '#C96C00')
cpsvaluelabel.pack(side = TOP)
cpsslider = Scale(cpsframe, orient = HORIZONTAL, from_ = int(settingslines[0].split('|')[5]), to = int(settingslines[0].split('|')[6]), resolution = 1, length = 500, variable = cpsvalue, troughcolor = '#2B2D31', bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#0F151D', activebackground = '#0F151D')
cpsslider.pack(side = LEFT)
changecpssliderlimits = Button(cpsframe, text = 'Change cps slider limits', command = lambda: changecpslimits(), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
changecpssliderlimits.pack(side = LEFT)

startbutton = Button(startandstopframe, text = 'Start', command = lambda: Start(running), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
startbutton.pack(anchor = W)
stopbutton = Button(startandstopframe, text = 'Stop', command = lambda: Stop(running), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
stopbutton.pack(anchor = W)

starthotkeyframe = Frame(hotkeyframe, bg = '#0F151D')
starthotkeyframe.pack(anchor = W)
starthotkeytext = Label(starthotkeyframe, text = 'Start HotKey:', bg = '#0F151D', fg = '#C96C00')
starthotkeytext.pack(side = LEFT)
starthotkeyentry = Entry(starthotkeyframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
starthotkeyentry.pack(side = LEFT)

stophotkeyframe = Frame(hotkeyframe, bg = '#0F151D')
stophotkeyframe.pack(anchor = W)
stophoykeylabel = Label(stophotkeyframe, text = 'Stop HotKey:',bg = '#0F151D', fg = '#C96C00')
stophoykeylabel.pack(side = LEFT)
stophotkeyentry = Entry(stophotkeyframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
stophotkeyentry.pack(side = LEFT)

sethotkeybutton = Button(setandresethotkeyframe, text = '  Set HotKey  ', command = sethotkey, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
sethotkeybutton.pack(anchor = W)
Resethotkey = Button(setandresethotkeyframe, text = 'Reset HotKey', command = resethotkey, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
Resethotkey.pack(anchor = W)

originstarthotkey = settingslines[0].split('|')[0].upper()
starthotkeyentry.delete(0,END)
starthotkeyentry.insert(0,originstarthotkey)
originstophotkey = settingslines[0].split('|')[1].upper()
stophotkeyentry.delete(0,END)
stophotkeyentry.insert(0,originstophotkey)

#button Hotkey frames
buttonlabelframe = Frame(cbbuttonframe, bg = '#0F151D')
buttonlabelframe.pack(side = LEFT)
buttoncheckboxframe = Frame(cbbuttonframe, bg = '#0F151D')
buttoncheckboxframe.pack(side = LEFT)
buttonhotkeylabel = Frame(cbbuttonframe, bg = '#0F151D')
buttonhotkeylabel.pack(side = LEFT)
buttonhotkeyframe = Frame(cbbuttonframe, bg = '#0F151D')
buttonhotkeyframe.pack(side = LEFT)

lcblabel = Label(buttonlabelframe, text = 'LCB Button  ', bg = '#0F151D', fg = '#C96C00')
lcblabel.pack(anchor = W)
mcblabel = Label(buttonlabelframe, text = 'MCB Button', bg = '#0F151D', fg = '#C96C00')
mcblabel.pack(anchor = W)
rcblabel = Label(buttonlabelframe, text = 'RCB Button ', bg = '#0F151D', fg = '#C96C00')
rcblabel.pack(anchor = W)

lcbbuttonvar = IntVar()
mcbbuttonvar = IntVar()
rcbbuttonvar = IntVar()
lcbcheckbox = Checkbutton(buttoncheckboxframe, variable = lcbbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
lcbcheckbox.pack(anchor = W)
mcbcheckbox = Checkbutton(buttoncheckboxframe, variable = mcbbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
mcbcheckbox.pack(anchor = W)
rcbcheckbox = Checkbutton(buttoncheckboxframe, variable = rcbbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
rcbcheckbox.pack(anchor = W)
lcbbuttonvar.set(1)
mcbbuttonvar.set(0)
rcbbuttonvar.set(0)

lcbhotkeylabel = Label(buttonhotkeylabel, text = 'LCB Hotkey  ', bg = '#0F151D', fg = '#C96C00')
lcbhotkeylabel.pack(anchor = W)
mcbhotkeylabel = Label(buttonhotkeylabel, text = 'MCB Hotkey', bg = '#0F151D', fg = '#C96C00')
mcbhotkeylabel.pack(anchor = W)
rcbhotkeylabel = Label(buttonhotkeylabel, text = 'RCB Hotkey ', bg = '#0F151D', fg = '#C96C00')
rcbhotkeylabel.pack(anchor = W)

lcbhotkey = Entry(buttonhotkeyframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
lcbhotkey.pack(anchor = W)
mcbhotkey = Entry(buttonhotkeyframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
mcbhotkey.pack(anchor = W)
rcbhotkey = Entry(buttonhotkeyframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
rcbhotkey.pack(anchor = W)

originlcbhotkey = settingslines[0].split('|')[2].upper()
lcbhotkey.delete(0,END)
lcbhotkey.insert(0,originlcbhotkey)
originmcbhotkey = settingslines[0].split('|')[3].upper()
mcbhotkey.delete(0,END)
mcbhotkey.insert(0,originmcbhotkey)
originrcbhotkey = settingslines[0].split('|')[4].upper()
rcbhotkey.delete(0,END)
rcbhotkey.insert(0,originrcbhotkey)


#Version and link to de neat website
scriptbotlogo = Button(root,justify = LEFT, command = scriptbotlink, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
scriptbotphoto=PhotoImage(file="logo.png")
scriptbotlogo.config(image=scriptbotphoto)
scriptbotlogo.pack(anchor = E)

version = Label(root, text = 'Version 3.1', bg = '#0F151D', fg = '#C96C00')
version.pack(anchor = E)

#toaster = ToastNotifier()

root.after(1000,lambda: main(running))
root.mainloop()