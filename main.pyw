from tkinter import Tk, E, W, LEFT, RIGHT, TOP, CENTER, Entry, Button, Label, Scale, Checkbutton, Frame, IntVar, END, HORIZONTAL, PhotoImage
#from tkinter import *
import webbrowser, keyboard, json
import win32api, win32con
import multiprocessing, random
#from win32api import mouse_event, Sleep, keybd_event as win32api
#from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP as win32con
#from win10toast import ToastNotifier

global process_list
process_list = []

def running(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):

    while True:
        x = int()
        y = int()
        if morkcheckbuttonvar == 1:
            if lcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                if str(loadedjsonsettings['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

            if mcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
                if str(loadedjsonsettings['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)

            if rcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
                if str(loadedjsonsettings['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
            
        if morkcheckbuttonvar == 0:
            for a in range(len(keyboardentry.split(','))):
                win32api.keybd_event(ord(keyboardentry.split(',')[a]),0)
                if str(loadedjsonsettings['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                print(keyboardentry.split(',')[a])

        if str(loadedjsonsettings['timeouttypes']) == '1':
            win32api.Sleep(int(cpsvalue))

def main(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):

    if lcbhotkey.get() != '':
        #if keyboard.is_pressed(lcbhotkey.get()): togglelcb()
        if keyboard.is_pressed(lcbhotkey.get()): togglelcb()
    if mcbhotkey.get() != '':
        #if win32api.GetAsyncKeyState(ord(str(mcbhotkey.get()))) != 0: togglemcb()
        if keyboard.is_pressed(mcbhotkey.get()): togglemcb()
    if rcbhotkey.get() != '':
        #if win32api.GetAsyncKeyState(ord(str(rcbhotkey.get()))) != 0: togglercb()
        if keyboard.is_pressed(rcbhotkey.get()): togglercb()

    if starthotkeyentry.get() != '':
        if keyboard.is_pressed(starthotkeyentry.get()): 
            #morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings
            Start(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings)
            #toaster.show_toast('Open_Clicker','Started', duration = 2, icon_path='./favicon.ico')
    if stophotkeyentry.get() != '': 
        if keyboard.is_pressed(stophotkeyentry.get()): 
            if bool(process_list) == True:
                p = process_list[len(process_list)-1]
                p.terminate()
                p.join()
                del(process_list[len(process_list)-1])
            win32api.Sleep(1000)
            #toaster.show_toast('Open_Clicker','Stopped', duration = 2, icon_path='./favicon.ico')
        
    root.after(1, lambda: main(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings))

def Start(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):
    if not len(process_list) >= 1:
        global p
        process_list.append(str(random.randint(0,999)))
        p = multiprocessing.Process(target=running, args = (morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings), name=process_list[len(process_list)-1])
        process_list[len(process_list)-1] = p
        print(p)
        p.start()
    win32api.Sleep(100)
    print('START')
    #toaster.show_toast('Open_Clicker','Started', duration = 5, icon_path='./favicon.ico')
    return

def Stop():
    if bool(process_list) == True:
        p = process_list[len(process_list)-1]
        p.terminate()
        p.join()
        del(process_list[len(process_list)-1])
    print('STOP')
    #toaster.show_toast('Open_Clicker','Stopped', duration = 5, icon_path='./favicon.ico')
    return

def sethotkey(loadedjsonsettings):

    with open('./json_settings.json','w') as settingsfile:

        loadedjsonsettings["lcbhotkey"] = lcbhotkey.get()
        loadedjsonsettings["mcbhotkey"] = mcbhotkey.get()
        loadedjsonsettings["rcbhotkey"] = rcbhotkey.get()

        json.dump(loadedjsonsettings, settingsfile)

    root.destroy()
    import main

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
    import changecpslimits

def changeclickmode():
    if morkcheckbuttonvar.get() == 0:
        lcblabel.config(state='disabled')
        mcblabel.config(state='disabled')
        rcblabel.config(state='disabled')
        lcbcheckbox.config(state='disabled')
        mcbcheckbox.config(state='disabled')
        rcbcheckbox.config(state='disabled')
        lcbhotkeylabel.config(state='disabled')
        mcbhotkeylabel.config(state='disabled')
        rcbhotkeylabel.config(state='disabled')
        lcbhotkey.config(state='disabled')
        mcbhotkey.config(state='disabled')
        rcbhotkey.config(state='disabled')
        keyboardlabel.config(state='normal')
        keyboardentry.config(state='normal')
    elif morkcheckbuttonvar.get() == 1:
        lcblabel.config(state='normal')
        mcblabel.config(state='normal')
        rcblabel.config(state='normal')
        lcbcheckbox.config(state='normal')
        mcbcheckbox.config(state='normal')
        rcbcheckbox.config(state='normal')
        lcbhotkeylabel.config(state='normal')
        mcbhotkeylabel.config(state='normal')
        rcbhotkeylabel.config(state='normal')
        lcbhotkey.config(state='normal')
        mcbhotkey.config(state='normal')
        rcbhotkey.config(state='normal')
        keyboardlabel.config(state='disabled')
        keyboardentry.config(state='disabled')
    else: print('YOU FUCKED IT UP YOU DUMBASS')

    return

if __name__ == '__main__':
    #beutiful gui
    root = Tk()
    root.title('Open_Clicker 4')
    root.config(bg = '#0F151D')
    root.resizable(0,0)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    #Frame for the cps slider and button to change it's limits
    cpsframe = Frame(root, bg = '#0F151D')
    cpsframe.pack(side = TOP)
    #yes lets put the start and stop stuff in a frame titled other stuff
    otherstuffframe = Frame(root, bg = '#0F151D')
    otherstuffframe.pack(side = TOP)
    #The frame the button and keyboard button selection stuff goes in.
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
    restoredefaultframe = Frame(classichotkeyframe, bg = '#0F151D')
    restoredefaultframe.pack(side = LEFT)

    #Super cool json file
    with open('./json_settings.json','r') as settingsfile:
        jsondata = settingsfile.read()
        loadedjsonsettings = json.loads(jsondata)
        settingsfile.close()

    cpsvalue = IntVar()
    cpsvaluelabel = Label(cpsframe, text = 'CPS value', bg = '#0F151D', fg = '#C96C00')
    cpsvaluelabel.pack(side = TOP)
    cpsslider = Scale(cpsframe, orient = HORIZONTAL, from_ = int(loadedjsonsettings["mincpsval"]), to = int(loadedjsonsettings["maxcpsval"]), resolution = 1, length = 500, variable = cpsvalue, troughcolor = '#2B2D31', bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#0F151D', activebackground = '#0F151D')
    cpsslider.pack(side = LEFT)
    changecpssliderlimits = Button(cpsframe, text = 'Change cps slider limits', command = lambda: changecpslimits(), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    changecpssliderlimits.pack(side = LEFT)
    cpsslider.set(int(loadedjsonsettings["cpspreviousval"]))

    startbutton = Button(startandstopframe, text = 'Start', command = lambda: Start(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    startbutton.pack(anchor = W)
    stopbutton = Button(startandstopframe, text = 'Stop', command = lambda: Stop(), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
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

    sethotkeybutton = Button(setandresethotkeyframe, text = '  Set HotKey  ', command = lambda: sethotkey(loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    sethotkeybutton.pack(anchor = W)

    originstarthotkey = loadedjsonsettings["Starthotkey"]
    starthotkeyentry.delete(0,END)
    starthotkeyentry.insert(0,originstarthotkey)
    originstophotkey = loadedjsonsettings["Stophotkey"]
    stophotkeyentry.delete(0,END)
    stophotkeyentry.insert(0,originstophotkey)

    #thing for containing all the hotkey buttons and other neat stuff for keyboard

    #The overarchinge frame
    mouseandkeyboardsettingframe = Frame(cbbuttonframe, bg = '#0F151D')
    mouseandkeyboardsettingframe.pack(side = LEFT)
    #The 2 frames for the settings and selecting mouse or keyboard
    selectkeyboardormouseframe = Frame(mouseandkeyboardsettingframe, bg = '#0F151D')
    selectkeyboardormouseframe.pack(side = LEFT)
    mandksettingsframe = Frame(mouseandkeyboardsettingframe, bg = '#0F151D')
    mandksettingsframe.pack(side = LEFT)
    #The 2 frames for the mouse and keyboard settings
    mousesettingstuff = Frame(mandksettingsframe, bg = '#0F151D')
    mousesettingstuff.pack(anchor = W)
    keyboardstuff = Frame(mandksettingsframe, bg = '#0F151D')
    keyboardstuff.pack(anchor = W)

    #The things for changing between mouse and keyboard
    morkcheckbuttonvar = IntVar()
    mousecheckbutton = Checkbutton(selectkeyboardormouseframe, pady = 15,text = 'mouse', variable = morkcheckbuttonvar, onvalue = 1, offvalue = 0, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F', command = lambda: changeclickmode())
    mousecheckbutton.pack(anchor = W)
    keyboardcheckbutton = Checkbutton(selectkeyboardormouseframe, pady = 15, text = 'keyboard', variable = morkcheckbuttonvar, onvalue = 0, offvalue = 1, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F', command = lambda: changeclickmode())
    keyboardcheckbutton.pack(anchor = W)
    morkcheckbuttonvar.set(loadedjsonsettings["mouseorkeyboard"])

    #mouse button stuff
    #mouse button setting frames
    buttonlabelframe = Frame(mousesettingstuff, bg = '#0F151D')
    buttonlabelframe.pack(side = LEFT)
    buttoncheckboxframe = Frame(mousesettingstuff, bg = '#0F151D')
    buttoncheckboxframe.pack(side = LEFT)
    buttonhotkeylabel = Frame(mousesettingstuff, bg = '#0F151D')
    buttonhotkeylabel.pack(side = LEFT)
    buttonhotkeyframe = Frame(mousesettingstuff, bg = '#0F151D')
    buttonhotkeyframe.pack(side = LEFT)

    #Mouse button stuff
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
    lcbbuttonvar.set(loadedjsonsettings["lcbenabled"])
    mcbbuttonvar.set(loadedjsonsettings["mcbenabled"])
    rcbbuttonvar.set(loadedjsonsettings["rcbenabled"])

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

    originlcbhotkey = loadedjsonsettings["lcbhotkey"]
    lcbhotkey.delete(0,END)
    lcbhotkey.insert(0,originlcbhotkey)
    originmcbhotkey = loadedjsonsettings["mcbhotkey"]
    mcbhotkey.delete(0,END)
    mcbhotkey.insert(0,originmcbhotkey)
    originrcbhotkey = loadedjsonsettings["rcbhotkey"]
    rcbhotkey.delete(0,END)
    rcbhotkey.insert(0,originrcbhotkey)

    #Keyboard button stuff
    #keyboard setting frames
    keyboardlabel = Label(keyboardstuff, text = 'Keboard keys:', bg = '#0F151D', fg = '#C96C00')
    keyboardlabel.pack(side = LEFT)
    keyboardentry = Entry(keyboardstuff, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
    keyboardentry.pack(side = LEFT)
    originkeyboardentry = loadedjsonsettings["keyboardkeys"]
    keyboardentry.delete(0,END)
    keyboardentry.insert(0,originkeyboardentry)

    #keyboard stuff
    #Version and link to de neat website
    scriptbotlogo = Button(root,justify = LEFT, command = scriptbotlink, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    scriptbotphoto=PhotoImage(file="logo.png")
    scriptbotlogo.config(image=scriptbotphoto)
    scriptbotlogo.pack(anchor = E)

    version = Label(root, text = 'Version 4.5', bg = '#0F151D', fg = '#C96C00')
    version.pack(anchor = E)

    #toaster = ToastNotifier()

    changeclickmode()

    root.after(1000,lambda: main(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings))
    root.mainloop()
