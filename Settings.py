from tkinter import *
import json, webbrowser, keyboard, multiprocessing, win32api, win32con
import toolTip

def cancel(): 
    return

global loadedjsonsettings
#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

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

class hotKeyWindow(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self,*args,**kwargs)
        #Top frame used because tkinter is the mega super uber gay
        hotKeyWindowFrame = Frame(self, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1)
        hotKeyWindowFrame.pack(side=LEFT)
        #Other actually useful frames
        hotKeyLabelFrame = Frame(hotKeyWindowFrame, bg = '#0F151D')
        hotKeyLabelFrame.pack(side=LEFT, expand=False)
        currentHotKeyFrame = Frame(hotKeyWindowFrame, bg = '#0F151D')
        currentHotKeyFrame.pack(side=LEFT)
        setChangeButtonFrame = Frame(hotKeyWindowFrame, bg = '#0F151D')
        setChangeButtonFrame.pack(side=LEFT)
        cancelResetButtonFrame = Frame(hotKeyWindowFrame, bg = '#0F151D')
        cancelResetButtonFrame.pack(side=LEFT)

        self.activeChange = int(0)

        self.widgetsInfo = {
                        'toggleHotKey':{'name':'toggleHotKey', 'displayName':'start/stop hotkey:', 'labels':['',''], 'buttons':['',''], 'jsonData':'toggleHotKey'},
                        'lcbHotKey':{'name':'lcbHotKey', 'displayName':'toggle lcb hotkey:', 'labels':['',''], 'buttons':['',''], 'jsonData':'lcbHotKey'},
                        'mcbHotKey':{'name':'mcbHotKey', 'displayName':'toggle mcb hotkey:', 'labels':['',''], 'buttons':['',''], 'jsonData':'mcbHotKey'},
                        'rcbHotKey':{'name':'rcbHotKey', 'displayName':'toggle rcb hotkey:', 'labels':['',''], 'buttons':['',''], 'jsonData':'rcbHotKey'}
                        }  
        for a in self.widgetsInfo:
            self.widgetsInfo[a]['labels'][0] = Label(hotKeyLabelFrame, text=self.widgetsInfo[a]['displayName'], bg = '#0F151D', fg = '#C96C00', pady=3)
            self.widgetsInfo[a]['labels'][0].pack(anchor=W)
            self.widgetsInfo[a]['labels'][1] = Label(currentHotKeyFrame, text=loadedjsonsettings['settings']['hotKeys'][self.widgetsInfo[a]['jsonData']], bg = '#2B2D31', fg='#C96C00', relief='ridge', width=25, pady=3)
            self.widgetsInfo[a]['labels'][1].pack(anchor=W)
            self.widgetsInfo[a]['buttons'][0] = self.initSetButton(a, self.widgetsInfo)
            self.widgetsInfo[a]['buttons'][0], self.widgetsInfo = self.widgetsInfo[a]['buttons'][0].create(setChangeButtonFrame, text='Change', changeText='Set')
            self.widgetsInfo[a]['buttons'][0].pack(anchor=W)
            #self.widgetsInfo[a]['buttons'][1] = Button(cancelResetButtonFrame, text = 'Reset', command=lambda:self.change(a), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F', width=8)
            #self.widgetsInfo[a]['buttons'][1].pack(anchor=W)

    def save(self):
        for a in self.widgetsInfo:
            loadedjsonsettings['settings']['hotKeys'][self.widgetsInfo[a]['jsonData']] = (self.widgetsInfo[a]['labels'][1]).cget('text')  
        with open('./json_settings.json','w') as settingsfile:
            json.dump(loadedjsonsettings, settingsfile, indent=4)
            settingsfile.close()
        return

    class initSetButton():
        def __init__(self, a, widgetsInfo):
            self.a = a
            self.widgetsInfo = widgetsInfo
            return

        def create(self, frame, text='n/a', changeText='n/a'):
            b = Button(frame, text=text, command=lambda:self.change(self.a, text=text, changedText=changeText), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F', width=8)
            return(b, self.widgetsInfo)

        buttonToggle = False
        def change(self, selected, text='n/a', changedText='n/a'):
            #selectedInfo = self.changeInfo.get(selected)
            p = multiprocessing.Process(target=self.listen())
            print(selected)
            if self.buttonToggle == False:
                for b in self.widgetsInfo:               
                    if self.widgetsInfo[b]['name'] == selected:
                        (self.widgetsInfo[b]['buttons'][0])['state'] = NORMAL
                        (self.widgetsInfo[b]['buttons'][0]).config(text=changedText)
                    elif self.widgetsInfo[b]['name'] != selected:
                        (self.widgetsInfo[b]['buttons'][0])['state'] = DISABLED
                        (self.widgetsInfo[b]['buttons'][0]).config(text=text)
                self.buttonToggle = True
            elif self.buttonToggle == True:
                for b in self.widgetsInfo:   
                    if self.widgetsInfo[b]['name'] == selected:
                        (self.widgetsInfo[b]['buttons'][0])['state'] = NORMAL
                        (self.widgetsInfo[b]['buttons'][0]).config(text=text)
                    elif self.widgetsInfo[b]['name'] != selected:
                        (self.widgetsInfo[b]['buttons'][0])['state'] = NORMAL
                        (self.widgetsInfo[b]['buttons'][0]).config(text=text)
                self.buttonToggle = False

        charList = []
        def listen(self):
            #while True:
            for a in VK_CODE:
                key = win32api.GetAsyncKeyState(VK_CODE[a])
                if key != 0:
                    if not a in self.charList:
                        self.charList.append(a)
                        (self.widgetsInfo[self.a]['labels'][1]).config(text='+'.join(self.charList))

class generalSettingsWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        generalSettingsWindowFrame = Frame(self, bg = '#0F151D')
        generalSettingsWindowFrame.pack(side=LEFT)
        #Change cps limits
        changeCPSLimitFrame = Frame(generalSettingsWindowFrame, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1, width=190, height=120)
        changeCPSLimitFrame.pack(side=TOP, expand=False)
        changeCPSLimitFrame.pack_propagate(0)
        changeCPSLimitLabel = Label(changeCPSLimitFrame, text='change CPS slider limits', bg = '#0F151D', fg = '#C96C00')
        changeCPSLimitLabel.pack(side=TOP)
        minValueLabel = Label(changeCPSLimitFrame, text = 'Minimum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
        minValueLabel.pack(side=TOP)
        self.minValueEntry = Entry(changeCPSLimitFrame, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
        self.minValueEntry.pack(side=TOP)
        maxValueLabel = Label(changeCPSLimitFrame, text = 'Maximum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
        maxValueLabel.pack(side=TOP)
        self.maxValueEntry = Entry(changeCPSLimitFrame, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
        self.maxValueEntry.pack(side=TOP)
        #Startup and running stuff
        runningStuffFrame = Frame(generalSettingsWindowFrame, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1, width=190, height=75)
        runningStuffFrame.pack(side=TOP, expand=False)
        runningStuffFrame.pack_propagate(0)
        runningTitlesFrame = Frame(runningStuffFrame, bg='#0F151D')
        runningTitlesFrame.pack(side=LEFT)
        runningInputsFrame = Frame(runningStuffFrame, bg='#0F151D')
        runningInputsFrame.pack(side=LEFT)
        #Labels
        runOnStartupLabel = Label(runningTitlesFrame, text='run on startup: ', bg = '#0F151D', fg = '#C96C00')
        runOnStartupLabel.pack(anchor=E)
        startMinimizedLabel = Label(runningTitlesFrame, text='start minimized: ', bg = '#0F151D', fg = '#C96C00')
        startMinimizedLabel.pack(anchor=E)
        runWithElevatedPrivligesLabel = Label(runningTitlesFrame, text='run with elevated privliges: ', bg = '#0F151D', fg = '#C96C00')
        runWithElevatedPrivligesLabel.pack(anchor=E)
        #Checkboxes
        self.runOnStartupVar = IntVar()
        runOnStartupCheckbox = Checkbutton(runningInputsFrame, variable=self.runOnStartupVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        runOnStartupCheckbox.pack(anchor=W)
        self.startMinimizedVar = IntVar()
        startMinimizedCheckbox = Checkbutton(runningInputsFrame, variable=self.startMinimizedVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        startMinimizedCheckbox.pack(anchor=W)
        self.runWithElevatedPrivligesVar = IntVar()
        runWithElevatedPrivligesCheckbox = Checkbutton(runningInputsFrame, variable=self.runWithElevatedPrivligesVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        runWithElevatedPrivligesCheckbox.pack(anchor=W)
        #Insert saves 
        self.runOnStartupVar.set(loadedjsonsettings['settings']['general']['runOnStartup'])
        self.startMinimizedVar.set(loadedjsonsettings['settings']['general']['startMinimize'])
        self.runWithElevatedPrivligesVar.set(loadedjsonsettings['settings']['general']['runWithElevatedPrivliges'])
        self.minValueEntry.delete(0,END)
        self.minValueEntry.insert(0,loadedjsonsettings["settings"]['general']["mincpsval"])
        self.maxValueEntry.delete(0,END)
        self.maxValueEntry.insert(0,loadedjsonsettings["settings"]['general']["maxcpsval"])

    def save(self):
        loadedjsonsettings['settings']['general']['runOnStartup'] = bool(self.runOnStartupVar.get())
        loadedjsonsettings['settings']['general']['startMinimize'] = bool(self.startMinimizedVar.get())
        loadedjsonsettings['settings']['general']['runWithElevatedPrivliges'] = bool(self.runWithElevatedPrivligesVar.get())
        loadedjsonsettings['settings']['general']['mincpsval'] = int(self.minValueEntry.get())
        loadedjsonsettings['settings']['general']['maxcpsval'] = int(self.maxValueEntry.get())
        with open('./json_settings.json','w') as settingsfile:
            json.dump(loadedjsonsettings, settingsfile, indent=4)
            settingsfile.close()
        return

class mainView(Frame):
    def __init__(self, *args, **kwargs):
        multiprocessing.freeze_support()

        Frame.__init__(self, *args, **kwargs)
        buttons = Frame(self, bg = '#0F151D', height=250, width=60)
        buttons.pack(side=LEFT)
        buttons.pack_propagate(0)
        afterButtonsFrame = Frame(self, bg='#0F151D', height=250, width=500)
        afterButtonsFrame.pack(side=LEFT)
        afterButtonsFrame.pack_propagate(0)
        currentPageFrame = Frame(afterButtonsFrame, bg = '#0F151D')
        currentPageFrame.pack(side=TOP)
        container = Frame(afterButtonsFrame, bg = '#0F151D')
        container.pack(anchor=W)
        settingOptionsFrame = Frame(afterButtonsFrame, bg = '#0F151D', width=500, height=28)
        settingOptionsFrame.pack(side=BOTTOM)
        settingOptionsFrame.pack_propagate(0)

        currentPageLabel = Label(currentPageFrame, text='n/a', bg = '#0F151D', fg = '#C96C00')
        currentPageLabel.pack(side=TOP)

        generalSettings = generalSettingsWindow(self, bg='#0F151D', height=200, width=400)
        generalSettings.pack_propagate(0)
        hotKeys = hotKeyWindow(self, bg='#0F151D', height=200, width=400)
        hotKeys.pack_propagate(0)

        generalSettings.place(in_=container, x=0, y=0)
        hotKeys.place(in_=container, x=0, y=0)

        generalButtonImage=PhotoImage(file="./icons/settings/general.png")
        generalButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'General', generalSettings), image=generalButtonImage, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        generalButton.image = generalButtonImage
        generalButton.pack(side=TOP)
        generalButtonTTP = toolTip.CreateToolTip(generalButton, 'General settings')
        hotKeyButtonPhoto=PhotoImage(file="./icons/settings/hotkey.png")
        hotKeysButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'HotKeys',hotKeys), image=hotKeyButtonPhoto, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        hotKeysButton.image = hotKeyButtonPhoto
        hotKeysButton.pack(side=TOP)
        hotKeysButtonTTP = toolTip.CreateToolTip(hotKeysButton, 'HotKey settings')
        scriptBotPhoto=PhotoImage(file="logo.png")
        scriptBotLogo = Button(buttons, justify=LEFT, command=lambda:webbrowser.open('https://script-bot.netlify.com'), image=scriptBotPhoto, bg='#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        scriptBotLogo.image = scriptBotPhoto
        scriptBotLogo.pack(side=TOP)
        version = Label(buttons, text = 'Ver ' + loadedjsonsettings['about']['version'], bg='#0F151D', fg='#C96C00')
        version.pack(side=TOP)

        doneButton = Button(settingOptionsFrame, text='Done', command=self.done, bg='#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        doneButton.pack(side=RIGHT)
        doneButtonTTP = toolTip.CreateToolTip(doneButton, 'Exit settings')
        applyButton = Button(settingOptionsFrame, text='Apply', command=lambda:self.apply(generalSettings, hotKeys), bg='#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        applyButton.pack(side=RIGHT)
        applyButtonTTP = toolTip.CreateToolTip(applyButton, 'Save current settings')

        self.change(currentPageLabel, 'General', generalSettings)

    def apply(self, generalSettings, hotKeys):
        generalSettings.save()
        hotKeys.save()

    def change(self, currentPageLabel, displayName, className):
        currentPageLabel.config(text=displayName)
        #root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings ' + displayName)
        className.lift()
        return

    def done(self):
        sys.exit()

if __name__ == "__main__":

    global root

    root = Tk()

    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings')
    root.config(bg = '#0F151D')
    root.resizable(0,0)
    root.geometry('500x250')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    main = mainView(root, bg='#0F151D')
    main.pack(anchor=W)

    root.mainloop()