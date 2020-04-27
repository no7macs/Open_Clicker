from tkinter import Tk, E, W, LEFT, RIGHT, TOP, CENTER, Entry, Button, Label, Scale, Checkbutton, Frame, IntVar, END, HORIZONTAL, PhotoImage
import keyboard, time, webbrowser
import win32api, win32con
#from win10toast import ToastNotifier
running = int(0)

def main(running):
    x = int()
    y = int()
    if starthotkeyentry.get() != '':
        if keyboard.is_pressed(starthotkeyentry.get()): 
            running = int(1)
            #toaster.show_toast('Open_Clicker','Started', duration = 2, icon_path='./favicon.ico')
    if stophotkeyentry.get() != '': 
        if keyboard.is_pressed(stophotkeyentry.get()): 
            running = int(2)
            #toaster.show_toast('Open_Clicker','Stopped', duration = 2, icon_path='./favicon.ico')
    
    print(running)
    #print(lcbbuttonvar.get())
    if running == 1:
        if lcbbuttonvar.get() == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
            time.sleep(cpsvalue.get()/1000)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

        if rcbbuttonvar.get() == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
            time.sleep(cpsvalue.get()/1000)
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
    hotkeyfile = open('./HotKey.txt','w')
    hotkeyfile.write(starthotkeyentry.get() + '|' + stophotkeyentry.get())
    hotkeyfile.close()
    root.destroy()
    import main

def resethotkey(): 
    starthotkeyentry.delete(0,END)
    starthotkeyentry.insert(0,originstarthotkey)

    stophotkeyentry.delete(0,END)
    stophotkeyentry.insert(0,originstophotkey)

def scriptbotlink():
    webbrowser.open('https://script-bot.netlify.com')

#beutiful gui
root = Tk()
root.title('Open_Clicker 3')
root.config(bg = '#0F151D')
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

cpsframe = Frame(root, bg = '#0F151D')
cpsframe.pack(side = TOP)
otherstuffframe = Frame(root, bg = '#0F151D')
otherstuffframe.pack(anchor = CENTER)

cdbuttonframe = Frame(otherstuffframe, bg = '#0F151D')
cdbuttonframe.pack(side = LEFT)
startandstopframe = Frame(otherstuffframe, bg = '#0F151D')
startandstopframe.pack(side = LEFT)
hotkeyframe = Frame(otherstuffframe, bg = '#0F151D')
hotkeyframe.pack(side = LEFT)
setandresethotkeyframe = Frame(otherstuffframe, bg = '#0F151D')
setandresethotkeyframe.pack(side = LEFT)

cpsvalue = IntVar()
cpsvaluelabel = Label(cpsframe, text = 'CPS value', bg = '#0F151D', fg = '#C96C00')
cpsvaluelabel.pack(side = TOP)
cpsslider = Scale(cpsframe, orient = HORIZONTAL, from_ = 1, to = 1000, resolution = 1, length = 500, variable = cpsvalue, troughcolor = '#2B2D31', bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#0F151D', activebackground = '#0F151D')
cpsslider.pack(side = TOP)

lcbbuttonvar = IntVar()
rcbbuttonvar = IntVar()
lcbcheckbox = Checkbutton(cdbuttonframe, text = 'LCB Button',variable = lcbbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
lcbcheckbox.pack(anchor = W)
rcbcheckbox = Checkbutton(cdbuttonframe, text = 'RCB Button',variable = rcbbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
rcbcheckbox.pack(anchor = W)
lcbbuttonvar.set(1)
rcbbuttonvar.set(0)

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

hotkeyfile = open('./HotKey.txt','r')
hotkeylines = hotkeyfile.readlines()

originstarthotkey = hotkeylines[0].split('|')[0]
starthotkeyentry.delete(0,END)
starthotkeyentry.insert(0,originstarthotkey)
originstophotkey = hotkeylines[0].split('|')[1]
stophotkeyentry.delete(0,END)
stophotkeyentry.insert(0,originstophotkey)
hotkeyfile.close()

scriptbotlogo = Button(root,justify = LEFT, command = scriptbotlink, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
scriptbotphoto=PhotoImage(file="logo.png")
scriptbotlogo.config(image=scriptbotphoto)
scriptbotlogo.pack(anchor=E)

version = Label(root, text = 'Version 3.0', bg = '#0F151D', fg = '#C96C00')
version.pack(anchor = E)

#toaster = ToastNotifier()

root.after(1000,lambda: main(running))
root.mainloop()