from tkinter import Tk, E, W, LEFT, RIGHT, TOP, CENTER, Entry, Button, Label, Scale, Checkbutton, Frame, IntVar, END, HORIZONTAL, PhotoImage, Toplevel
#from tkinter import *
import keyboard, json
import win32api, win32con
import multiprocessing, random, winreg, sys, os
import Settings, toolTip
import win32com.shell.shell as shell
#from win10toast import ToastNotifier
#from win32api import mouse_event, Sleep, keybd_event as win32api
#from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP as win32con

#toaster = ToastNotifier()
global process_list
process_list = []

#Giant dictonary to hold key name and VK value
VK_CODE = {'backspace':0x08, 'tab':0x09, 'clear':0x0C, 'enter':0x0D, 'alt':0x12, 'pause':0x13, 'caps_lock':0x14, 'esc':0x1B,
    'spacebar':0x20, 'page_up':0x21, 'page_down':0x22, 'end':0x23, 'home':0x24, 'left_arrow':0x25, 'up_arrow':0x26, 'right_arrow':0x27, 'down_arrow':0x28,
    'select':0x29, 'print':0x2A, 'execute':0x2B, 'print_screen':0x2C, 'ins':0x2D, 'del':0x2E, 'help':0x2F, '0':0x30, '1':0x31, '2':0x32, '3':0x33,
    '4':0x34, '5':0x35, '6':0x36, '7':0x37, '8':0x38, '9':0x39, 'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
    'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50, 'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 
    'w':0x57, 'x':0x58, 'y':0x59, 'z':0x5A, 'numpad_0':0x60, 'numpad_1':0x61, 'numpad_2':0x62, 'numpad_3':0x63, 'numpad_4':0x64, 'numpad_5':0x65,
    'numpad_6':0x66, 'numpad_7':0x67, 'numpad_8':0x68, 'numpad_9':0x69, 'multiply_key':0x6A, 'add_key':0x6B, 'separator_key':0x6C, 'subtract_key':0x6D,
    'decimal_key':0x6E, 'divide_key':0x6F, 'F1':0x70, 'F2':0x71, 'F3':0x72, 'F4':0x73, 'F5':0x74, 'F6':0x75, 'F7':0x76, 'F8':0x77, 'F9':0x78,
    'F10':0x79, 'F11':0x7A, 'F12':0x7B, 'F13':0x7C, 'F14':0x7D, 'F15':0x7E, 'F16':0x7F, 'F17':0x80, 'F18':0x81, 'F19':0x82, 'F20':0x83, 'F21':0x84,
    'F22':0x85, 'F23':0x86, 'F24':0x87, 'num_lock':0x90, 'scroll_lock':0x91, 'left_shift':0xA0, 'right_shift':0xA1, 'left_control':0xA2, 'right_control':0xA3,
    'left_menu':0xA4, 'right_menu':0xA5, 'browser_back':0xA6, 'browser_forward':0xA7, 'browser_refresh':0xA8, 'browser_stop':0xA9, 'browser_search':0xAA,
    'browser_favorites':0xAB, 'browser_start_and_home':0xAC, 'volume_mute':0xAD, 'volume_Down':0xAE, 'volume_up':0xAF, 'next_track':0xB0, 'previous_track':0xB1,
    'stop_media':0xB2, 'play/pause_media':0xB3, 'start_mail':0xB4, 'select_media':0xB5, 'start_application_1':0xB6, 'start_application_2':0xB7, 'attn_key':0xF6,
    'crsel_key':0xF7, 'exsel_key':0xF8, 'play_key':0xFA, 'zoom_key':0xFB, 'clear_key':0xFE, '+':0xBB, ',':0xBC, '-':0xBD, '.':0xBE, '/':0xBF, '`':0xC0,
    ';':0xBA, '[':0xDB, '\\':0xDC, ']':0xDD, "'":0xDE,'xbutton1':0x05,'xbutton2':0x06}
#Runs in seperate process
def running(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):
    actionSet = {'before':[],'after':[]}
    x = int()
    y = int()
    if morkcheckbuttonvar == 1:
        if lcbbuttonvar == 1:
            actionSet['before'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)', '<string>', 'exec'))
            actionSet['after'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)', '<string>', 'exec'))
        if mcbbuttonvar == 1:
            actionSet['before'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)', '<string>', 'exec'))
            actionSet['after'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)', '<string>', 'exec'))
        if rcbbuttonvar == 1:
            actionSet['before'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)', '<string>', 'exec'))
            actionSet['after'].append(compile('win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)', '<string>', 'exec'))
    if morkcheckbuttonvar == 0:
        for a in (keyboardentry.split('+')):
            print(VK_CODE[a])
            actionSet['before'].append(compile('win32api.keybd_event(' + str(VK_CODE[a]) + ', 0,0,0)', '<string>', 'exec'))
            actionSet['after'].append(compile('win32api.keybd_event(' + str(VK_CODE[a]) + ', 0,win32con.KEYEVENTF_KEYUP, 0)', '<string>', 'exec'))
    if loadedjsonsettings['saveState']['timeoutTypes'] == 1:
        actionSet['before'].append(compile('win32api.Sleep(int(cpsvalue))', '<string>', 'exec'))
    else:
        actionSet['after'].append(compile('win32api.Sleep(int(cpsvalue))', '<string>', 'exec'))

    while True:
        for a in actionSet['before']:
            exec(a)
        for b in actionSet['after']:
            exec(b)

def main(loadedjsonsettings):
    def detect(call, keys):
        keys = keys.split('+')
        keypress = 0
        for a in range(0, len(keys)):
            key = win32api.GetAsyncKeyState(VK_CODE[keys[a]])
            if key != 0:
                keypress += 1
            else: keypress == 0
        if keypress == len(keys):
            call()

    #root.protocol('WM_DELETE_WINDOW', customExit(loadedjsonsettings))  # root is your root window

    if loadedjsonsettings['settings']['hotKeys']['lcbHotKey'] != '':
        detect(call=lambda:togglelcb(),
                keys=loadedjsonsettings['settings']['hotKeys']['lcbHotKey'])
    if loadedjsonsettings['settings']['hotKeys']['mcbHotKey'] != '':
        detect(call=lambda:togglemcb(),
                keys=loadedjsonsettings['settings']['hotKeys']['mcbHotKey'])
    if loadedjsonsettings['settings']['hotKeys']['rcbHotKey'] != '':
        detect(call=lambda:togglercb(),
                keys=loadedjsonsettings['settings']['hotKeys']['rcbHotKey'])
    if loadedjsonsettings['settings']['hotKeys']['toggleHotKey'] != '':
        detect(call=lambda:toggle(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings),
                keys=loadedjsonsettings['settings']['hotKeys']['toggleHotKey'])

    root.after(1, lambda: main(loadedjsonsettings))

def toggle(morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings):
    save(loadedjsonsettings)
    try: toggle.currentStatus
    except: toggle.currentStatus = bool()
    if toggle.currentStatus == False:
        root.focus_set()
        if not len(process_list) >= 1:
            process_list.append(str(random.randint(0,999)))
            p = multiprocessing.Process(target=running, args = (morkcheckbuttonvar, lcbbuttonvar, mcbbuttonvar, rcbbuttonvar, keyboardentry, cpsvalue, loadedjsonsettings), name=process_list[len(process_list)-1])
            process_list[len(process_list)-1] = p
            print(p)
            p.start()
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
        initVars(loadedjsonsettings)
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
        loadedjsonsettings["saveState"]["keyboardKeys"] = keyboardentry.get()

        json.dump(loadedjsonsettings, settingsfile, indent = 4)

    #initVars(loadedjsonsettings)
    return

def settings():
    #settingsstop = Toplevel()
    #settings = Settings.mainView(settingsstop, bg='#0F151D')
    #settings.pack(anchor=W)
    #settingsstop.mainloop()
    p = multiprocessing.Process(target=Settings.main)
    p.start()

def customExit(loadedjsonsettings):
    save(loadedjsonsettings)
    sys.exit()

def initVars(loadedjsonsettings):
    cpsSlider.config(from_ = int(loadedjsonsettings["settings"]['general']["mincpsval"]), to = int(loadedjsonsettings["settings"]['general']["maxcpsval"]))
    cpsSlider.set(int(loadedjsonsettings["saveState"]["cpspreviousval"]))
    
    morkcheckbuttonvar.set(loadedjsonsettings["saveState"]["mouseorkeyboard"])
    changeclickmode()

    lcbbuttonvar.set(loadedjsonsettings["saveState"]["lcbenabled"])
    mcbbuttonvar.set(loadedjsonsettings["saveState"]["mcbenabled"])
    rcbbuttonvar.set(loadedjsonsettings["saveState"]["rcbenabled"])

    originkeyboardentry = loadedjsonsettings["saveState"]["keyboardKeys"]
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
    multiprocessing.freeze_support()
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
    cpsSlider = Scale(cpsframe, orient = HORIZONTAL, from_ = int(loadedjsonsettings["settings"]['general']["mincpsval"]), to = int(loadedjsonsettings["settings"]['general']["maxcpsval"]), resolution = 1, length = 500, variable = cpsvalue, troughcolor = '#2B2D31', bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#0F151D', activebackground = '#0F151D')
    cpsSlider.pack(side = LEFT)
    cpsSliderTTP = toolTip.CreateToolTip(cpsSlider, 'Change the timeout between clicks (1 is fastest)')
    #Start/Stop button
    toggleButton = Button(otherstuffframe, text = 'Start', command = lambda:toggle(morkcheckbuttonvar.get(), lcbbuttonvar.get(), mcbbuttonvar.get(), rcbbuttonvar.get(), keyboardentry.get(), cpsvalue.get(), loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F', width=70)
    toggleButton.pack(anchor=W)
    toggleButtonTTP = toolTip.CreateToolTip(toggleButton, 'Start/Stop the clicking with a button')
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
    #Checkbox stuff for keys
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
    #Settings button stuff
    settingsFrame = Frame(root, bg = '#0F151D')
    settingsFrame.pack(side=TOP)
    settingsButton = Button(settingsFrame, text='Settings', command=settings, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F', width=70)
    settingsButton.pack(side=RIGHT)


    changeclickmode()

    initVars(loadedjsonsettings)

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE)
    is_checked = True
    if (loadedjsonsettings['settings']['general']['runOnStartup']) == True:
        path = sys.executable
        winreg.SetValueEx(key, 'CaptchaCatcher',0, winreg.REG_SZ, path)
    else:
        try:
            winreg.DeleteValue(key, 'CaptchaCatcher')
        except:
            pass
    key.Close()

    if loadedjsonsettings['settings']['general']['startMinimize'] == True:
        root.wm_state('iconic')

    if loadedjsonsettings['settings']['general']['runWithElevatedPrivliges'] == True:
        ASADMIN = 'asadmin'
        if sys.argv[-1] != ASADMIN:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
            shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
            sys.exit(0)

    root.after(1000,lambda: main(loadedjsonsettings))
    root.mainloop()
