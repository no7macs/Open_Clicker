from tkinter import *
import json

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


class mainView(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        buttons = Frame(self, bg = '#0F151D')
        buttons.pack(side=LEFT)
        container = Frame(self, bg = '#0F151D')
        container.pack(side=LEFT)

        #hotKeys = hotKeyWindow(self)

        hotKeysButton = Button(buttons, justify = LEFT, command = cancel, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        hotKeyButtonPhoto=PhotoImage(file="logo.png")
        hotKeysButton.config(image=hotKeyButtonPhoto)
        hotKeysButton.pack(anchor = E)
        startupButton = Button(buttons, justify = LEFT, command = cancel, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
        startupButtonImage=PhotoImage(file="logo.png")
        startupButton.config(image=startupButtonImage)
        startupButton.pack(anchor = E)

if __name__ == "__main__":
    root = Tk()

    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' Settings')
    root.config(bg = '#0F151D')
    #root.resizable(0,0)
    #root.geometry('200x100')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    main = mainView(root)
    main.pack(anchor=W)

    root.mainloop()