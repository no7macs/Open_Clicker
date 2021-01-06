from tkinter import *
import json, gc

def save(loadedjsonsettings, minValueEntry, maxValueEntry):
    loadedjsonsettings['settings']['runOnStartup'] = bool()
    loadedjsonsettings['settings']['startMinimize'] = bool()
    loadedjsonsettings['mincpsval'] = int(minValueEntry.get())
    loadedjsonsettings['maxcpsval'] = int(maxValueEntry.get())

    with open('./json_settings.json','w') as settingsfile:
        json.dump(loadedjsonsettings, settingsfile, indent=4)
        settingsfile.close()

    return

def cancel(): 
    return

#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

class hotKeyWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self,*args,**kwargs)

        hotKeyWindowFrame = Frame(self, bg = '#0F151D')
        hotKeyWindowFrame.pack(side=LEFT)

        hotKeyLabelFrame = Frame(hotKeyWindowFrame, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1, width=190, height=120)
        hotKeyLabelFrame.pack(side=TOP, expand=False)

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
        
        self.runOnStartupVar.set(loadedjsonsettings['settings']['runOnStartup'])
        self.startMinimizedVar.set(loadedjsonsettings['settings']['startMinimize'])
        self.runWithElevatedPrivligesVar.set(loadedjsonsettings['settings']['runWithElevatedPrivliges'])
        self.minValueEntry.delete(0,END)
        self.minValueEntry.insert(0,loadedjsonsettings["saveState"]["mincpsval"])
        self.maxValueEntry.delete(0,END)
        self.maxValueEntry.insert(0,loadedjsonsettings["saveState"]["maxcpsval"])

    def save(self):
        loadedjsonsettings['settings']['runOnStartup'] = bool(self.runOnStartupVar.get)
        loadedjsonsettings['settings']['startMinimize'] = bool(self.startMinimizedVar.get)
        loadedjsonsettings['settings']['runWithElevatedPrivliges'] = bool(self.runWithElevatedPrivligesVar.get)
        loadedjsonsettings['mincpsval'] = int(self.minValueEntry.get())
        loadedjsonsettings['maxcpsval'] = int(self.maxValueEntry.get())
        with open('./json_settings.json','w') as settingsfile:
            json.dump(loadedjsonsettings, settingsfile, indent=4)
            settingsfile.close()

class mainView(Frame):
    def __init__(self, *args, **kwargs):
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

        currentPageLabel = Label(currentPageFrame, text='n/a', bg = '#0F151D', fg = '#C96C00')
        currentPageLabel.pack(side=TOP)

        generalSettings = generalSettingsWindow(self, bg='#0F151D', height=200, width=400)
        generalSettings.pack_propagate(0)
        hotKeys = hotKeyWindow(self, bg='#0F151D', height=200, width=400, highlightbackground="#C96C00", highlightthicknes=1)
        hotKeys.pack_propagate(0)

        generalSettings.place(in_=container, x=0, y=0)
        hotKeys.place(in_=container, x=0, y=0)

        generalButtonImage=PhotoImage(file="./icons/settings/general.png")
        generalButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'General', generalSettings), image=generalButtonImage, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        generalButton.image = generalButtonImage
        generalButton.pack(side=TOP)
        hotKeyButtonPhoto=PhotoImage(file="./icons/settings/hotkey.png")
        hotKeysButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'HotKeys',hotKeys), image=hotKeyButtonPhoto, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        hotKeysButton.image = hotKeyButtonPhoto
        hotKeysButton.pack(side=TOP)

        self.change(currentPageLabel, 'General', generalSettings)

    def change(self, currentPageLabel, displayName, className):
        currentPageLabel.config(text=displayName)
        root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings ' + displayName)
        className.lift()
        return

if __name__ == "__main__":

    root = Tk()

    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings')
    root.config(bg = '#0F151D')
    root.resizable(0,0)
    root.geometry('500x250')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    main = mainView(root, bg='#0F151D')
    main.pack(anchor=W)

    root.mainloop()