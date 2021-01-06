from tkinter import *
import json, gc

def save(loadedjsonsettings, minValueEntry, maxValueEntry):
    loadedjsonsettings['settings']['runOnStartup'] = bool()
    loadedjsonsettings['settings']['startMinimize'] = bool()
    loadedjsonsettings['mincpsval'] = int(minValueEntry.get())
    loadedjsonsettings['maxcpsval'] = int(maxValueEntry.get())

    with open('./json_settings.json','w') as settingsfile:
        json.dump(loadedjsonsettings, settingsfile, indent=4)

    return

def cancel(): 
    return

def initVars(loadedjsonsettings, runOnStartupVar, startMinimizedVar):
    runOnStartupVar.set(loadedjsonsettings['settings']['runOnStartup'])
    startMinimizedVar.set(loadedjsonsettings['settings']['startMinimize'])
    return

#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

class hotKeyWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self,*args,**kwargs)

        testLabel = Label(self, text='kekekekektestetstetst')
        testLabel.pack(side=TOP)

class generalSettingsWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        #Change cps limits
        changeCPSLimitFrame = Frame(self, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1)
        changeCPSLimitFrame.pack(side=TOP)
        changeCPSLimitLabel = Label(changeCPSLimitFrame, text='change CPS slider limits', bg = '#0F151D', fg = '#C96C00')
        changeCPSLimitLabel.pack(side=TOP)
        minValueLabel = Label(changeCPSLimitFrame, text = 'Minimum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
        minValueLabel.pack(side=TOP)
        minValueEntry = Entry(changeCPSLimitFrame, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
        minValueEntry.pack(side=TOP)
        maxValueLabel = Label(changeCPSLimitFrame, text = 'Maximum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
        maxValueLabel.pack(side=TOP)
        maxValueEntry = Entry(changeCPSLimitFrame, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
        maxValueEntry.pack(side=TOP)

        #Startup and running stuff
        runningStuffFrame = Frame(self, bg = '#0F151D', highlightbackground="#C96C00", highlightthicknes=1)
        runningStuffFrame.pack(side=TOP)
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
        runOnStartupVar = IntVar()
        runOnStartupCheckbox = Checkbutton(runningInputsFrame, variable=runOnStartupVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        runOnStartupCheckbox.pack(anchor=W)
        startMinimizedVar = IntVar()
        startMinimizedCheckbox = Checkbutton(runningInputsFrame, variable=startMinimizedVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        startMinimizedCheckbox.pack(anchor=W)
        runWithElevatedPrivligesVar = IntVar()
        runWithElevatedPrivligesCheckbox = Checkbutton(runningInputsFrame, variable=runWithElevatedPrivligesVar, onvalue=True, offvalue=False, bg='#0F151D', fg='#C96C00', highlightbackground='#0F151D', highlightcolor='#1E1D1D', selectcolor='#0F151D', activebackground='#0F151D', activeforeground='#066D9F')
        runWithElevatedPrivligesCheckbox.pack(anchor=W)

class mainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        buttons = Frame(self, bg = '#0F151D')
        buttons.pack(side=LEFT)
        afterButtonsFrame = Frame(self, bg = '#0F151D')
        afterButtonsFrame.pack(side=LEFT)
        currentPageFrame = Frame(afterButtonsFrame, bg = '#0F151D')
        currentPageFrame.pack(side=TOP)
        container = Frame(afterButtonsFrame, bg = '#0F151D', width=200, height=200)
        container.pack(side=TOP)

        currentPageLabel = Label(currentPageFrame, text='n/a', bg = '#0F151D', fg = '#C96C00')
        currentPageLabel.pack(side=TOP)

        generalSettings = generalSettingsWindow(self, bg='#0F151D')
        hotKeys = hotKeyWindow(self, bg='#0F151D')

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

    def all_children(self, window) :
        _list = window.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list

if __name__ == "__main__":

    root = Tk()

    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings')
    root.config(bg = '#0F151D')
    #root.resizable(0,0)
    #root.geometry('500x500')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    main = mainView(root, bg='#0F151D')
    main.pack(anchor=W)

    root.mainloop()