from tkinter import Tk, E, W, LEFT, RIGHT, TOP, CENTER, Entry, Button, Label, Scale, Checkbutton, Frame, IntVar, END, HORIZONTAL, PhotoImage
#from tkinter import *
import keyboard, json
import win32api, win32con
import multiprocessing, random
#from win10toast import ToastNotifier
#from win32api import mouse_event, Sleep, keybd_event as win32api
#from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP as win32con

#toaster = ToastNotifier()
global process_list
process_list = []

#Runs in seperate process
def running(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):

    while True:
        x = int()
        y = int()
        if morkcheckbuttonvar == 1:
            if lcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                if str(loadedjsonsettings["saveState"]['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

            if mcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
                if str(loadedjsonsettings["saveState"]['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)

            if rcbbuttonvar == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
                if str(loadedjsonsettings["saveState"]['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
            
        if morkcheckbuttonvar == 0:
            for a in range(len(keyboardentry.split(','))):
                win32api.keybd_event(ord(keyboardentry.split(',')[a]),0)
                if str(loadedjsonsettings["saveState"]['timeouttypes']) == '0':
                    win32api.Sleep(int(cpsvalue))
                print(keyboardentry.split(',')[a])

        if str(loadedjsonsettings["saveState"]['timeouttypes']) == '1':
            win32api.Sleep(int(cpsvalue))

def main(loadedjsonsettings):
    # morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings
    # morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings

    if loadedjsonsettings['settings']['hotKeys']['lcbhotkey'] != '':
        #if keyboard.is_pressed(lcbhotkey.get()): togglelcb()
        if keyboard.is_pressed(loadedjsonsettings['settings']['hotKeys']['lcbhotkey']): togglelcb()
    if loadedjsonsettings['settings']['hotKeys']['mcbhotkey'] != '':
        #if win32api.GetAsyncKeyState(ord(str(mcbhotkey.get()))) != 0: togglemcb()
        if keyboard.is_pressed(loadedjsonsettings['settings']['hotKeys']['mcbhotkey']): togglemcb()
    if loadedjsonsettings['settings']['hotKeys']['rcbhotkey'] != '':
        #if win32api.GetAsyncKeyState(ord(str(rcbhotkey.get()))) != 0: togglercb()
        if keyboard.is_pressed(loadedjsonsettings['settings']['hotKeys']['rcbhotkey']): togglercb()

    if loadedjsonsettings['settings']['hotKeys']['toggleHotKey'] != '':
        if keyboard.is_pressed(loadedjsonsettings['settings']['hotKeys']['toggleHotKey']):
            toggle(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings)

    root.after(1, lambda: main(loadedjsonsettings))

def toggle(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):
    try: toggle.currentStatus
    except: toggle.currentStatus = bool()
    if toggle.currentStatus == False:
        root.focus_set()
        if not len(process_list) >= 1:
            global p
            process_list.append(str(random.randint(0,999)))
            p = multiprocessing.Process(target=running, args = (morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings), name=process_list[len(process_list)-1])
            process_list[len(process_list)-1] = p
            print(p)
            p.start()
            save(loadedjsonsettings)
        win32api.Sleep(100)
        print('START')
        toggleButton.config(text='Stop')
        toggle.currentStatus = True
    elif toggle.currentStatus == True:
        root.focus_set()
        if bool(process_list) == True:
            p = process_list[len(process_list)-1]
            p.terminate()
            p.join()
            del(process_list[len(process_list)-1])
        print('STOP')
        toggleButton.config(text='Start')
        toggle.currentStatus = False
    else: toggle.currentStatus = False
    win32api.Sleep(1000)

def save(loadedjsonsettings):
    with open('./json_settings.json','w') as settingsfile:
        #Will be changed when setings is expanded
        loadedjsonsettings["saveState"]["mouseorkeyboard"] = morkcheckbuttonvar.get()
        loadedjsonsettings["saveState"]["lcbenabled"] = lcbbuttonvar.get()
        loadedjsonsettings["saveState"]["mcbenabled"] = mcbbuttonvar.get()
        loadedjsonsettings["saveState"]["rcbenabled"] = rcbbuttonvar.get()
        loadedjsonsettings["saveState"]["cpspreviousval"] = cpsvalue.get()

        json.dump(loadedjsonsettings, settingsfile, indent = 4)

    #initVars(loadedjsonsettings)
    return

def initVars(loadedjsonsettings):
    cpsslider.config(from_ = int(loadedjsonsettings["settings"]['general']["mincpsval"]), to = int(loadedjsonsettings["settings"]['general']["maxcpsval"]))
    cpsslider.set(int(loadedjsonsettings["saveState"]["cpspreviousval"]))
    
    morkcheckbuttonvar.set(loadedjsonsettings["saveState"]["mouseorkeyboard"])
    changeclickmode()

    lcbbuttonvar.set(loadedjsonsettings["saveState"]["lcbenabled"])
    mcbbuttonvar.set(loadedjsonsettings["saveState"]["mcbenabled"])
    rcbbuttonvar.set(loadedjsonsettings["saveState"]["rcbenabled"])

    originkeyboardentry = loadedjsonsettings["saveState"]["keyboardkeys"]
    keyboardentry.delete(0,END)
    keyboardentry.insert(0,originkeyboardentry)
    return

def togglelcb(): 
    lcbcheckbox.toggle()
    win32api.Sleep(200)
def togglemcb(): 
    mcbcheckbox.toggle()
    win32api.Sleep(200)
def togglercb(): 
    rcbcheckbox.toggle()
    win32api.Sleep(200)

def changeclickmode():
    if morkcheckbuttonvar.get() == 0:
        lcblabel.config(state='disabled')
        mcblabel.config(state='disabled')
        rcblabel.config(state='disabled')
        lcbcheckbox.config(state='disabled')
        mcbcheckbox.config(state='disabled')
        rcbcheckbox.config(state='disabled')
        keyboardlabel.config(state='normal')
        keyboardentry.config(state='normal')
    elif morkcheckbuttonvar.get() == 1:
        lcblabel.config(state='normal')
        mcblabel.config(state='normal')
        rcblabel.config(state='normal')
        lcbcheckbox.config(state='normal')
        mcbcheckbox.config(state='normal')
        rcbcheckbox.config(state='normal')
        keyboardlabel.config(state='disabled')
        keyboardentry.config(state='disabled')
    else: print('YOU FUCKED IT UP YOU DUMBASS')

    return

if __name__ == '__main__':

    #Super cool json file
    with open('./json_settings.json','r') as settingsfile:
        jsondata = settingsfile.read()
        loadedjsonsettings = json.loads(jsondata)
        settingsfile.close()

    #beutiful gui
    root = Tk()
    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'])
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

    cpsvalue = IntVar()
    cpsvaluelabel = Label(cpsframe, text = 'CPS value', bg = '#0F151D', fg = '#C96C00')
    cpsvaluelabel.pack(side = TOP)
    cpsslider = Scale(cpsframe, orient = HORIZONTAL, from_ = int(loadedjsonsettings["settings"]['general']["mincpsval"]), to = int(loadedjsonsettings["settings"]['general']["maxcpsval"]), resolution = 1, length = 500, variable = cpsvalue, troughcolor = '#2B2D31', bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#0F151D', activebackground = '#0F151D')
    cpsslider.pack(side = LEFT)

    toggleButton = Button(otherstuffframe, text = 'Start', command = lambda:toggle(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F', width=70)
    toggleButton.pack(anchor=W)
    #needs to fuck off later
    #sethotkeybutton = Button(setandresethotkeyframe, text = '  Set HotKey  ', command = lambda: sethotkey(loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    #sethotkeybutton.pack(anchor = W)

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

    #Keyboard button stuff
    #keyboard setting frames
    keyboardlabel = Label(keyboardstuff, text = 'Keboard keys:', bg = '#0F151D', fg = '#C96C00')
    keyboardlabel.pack(side = LEFT)
    keyboardentry = Entry(keyboardstuff, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
    keyboardentry.pack(side = LEFT)

    #toaster = ToastNotifier()

    changeclickmode()

    initVars(loadedjsonsettings)

    root.after(1000,lambda: main(loadedjsonsettings))
    root.mainloop()
