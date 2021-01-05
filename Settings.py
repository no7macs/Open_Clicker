from tkinter import *
import json, gc

def save(loadedjsonsettings):
    loadedjsonsettings['settings']['runOnStartup'] = bool()
    loadedjsonsettings['settings']['startMinimize'] = bool()

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

class generalSettingsWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

class mainView(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        buttons = Frame(self, bg = '#0F151D')
        buttons.pack(side=LEFT)
        afterButtonsFrame = Frame(self, bg = '#0F151D')
        afterButtonsFrame.pack(side=TOP)
        currentPageFrame = Frame(afterButtonsFrame, bg = '#0F151D')
        currentPageFrame.pack(side=TOP)
        container = Frame(afterButtonsFrame, bg = '#0F151D')
        container.pack(side=TOP)

        currentPageLabel = Label(currentPageFrame, text='n/a', bg = '#0F151D', fg = '#C96C00')
        currentPageLabel.pack(anchor=W)

        hotKeys = hotKeyWindow(self, bg='#0F151D')
        generalSettings = generalSettingsWindow(self, bg='#0F151D')

        hotKeys.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        generalSettings.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        hotKeys.pack(side='left')
        generalSettings.pack(side='left')

        generalButtonImage=PhotoImage(file="./icons/settings/general.png")
        generalButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'General', generalSettingsWindow), image=generalButtonImage, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        generalButton.image = generalButtonImage
        generalButton.pack(anchor = E)
        hotKeyButtonPhoto=PhotoImage(file="./icons/settings/hotkey.png")
        hotKeysButton = Button(buttons, justify=LEFT, command=lambda:self.change(currentPageLabel, 'HotKeys', hotKeyWindow), image=hotKeyButtonPhoto, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        hotKeysButton.image = hotKeyButtonPhoto
        hotKeysButton.pack(anchor = E)

    def change(self, currentPageLabel, displayName, className):
        currentPageLabel.config(text=displayName)
        root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings ' + displayName)
        className.lift(self)
        return

if __name__ == "__main__":

    root = Tk()

    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings')
    root.config(bg = '#0F151D')
    #root.resizable(0,0)
    #root.geometry('200x100')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    main = mainView(root, bg='#0F151D')
    main.pack(anchor=W)

    root.mainloop()