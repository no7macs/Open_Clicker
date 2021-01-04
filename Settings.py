from tkinter import *
import json

def save():
    pass

def cancel():
    pass

#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

root = Tk()

root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'])
root.config(bg = '#0F151D')
root.geometry('200x100')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

#Run on startup stuff                    
runOnStartupFrame = Frame(root, bg = '#0F151D')
runOnStartupFrame.pack(anchor = S)

runOnStartupLabel = Label(runOnStartupFrame, text = 'run on startup', bg = '#0F151D', fg = '#C96C00')
runOnStartupLabel.pack(side = LEFT)

runOnStartupVar = IntVar()
runOnStartupCehckBox = Checkbutton(runOnStartupFrame, variable = runOnStartupVar, onvalue = True, offvalue = False, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
runOnStartupCehckBox.pack(side = LEFT)

#Start minimized stuff
startMinimizedFrame = Frame(root, bg = '#0F151D')
startMinimizedFrame.pack(anchor = S)

startMinimizedLabel = Label(startMinimizedFrame, text = 'start minimized', bg = '#0F151D', fg = '#C96C00')
startMinimizedLabel.pack(side = LEFT)

startMinimizedVar = IntVar()
startMinimizedCheckBox = Checkbutton(startMinimizedFrame, variable = startMinimizedVar, onvalue = True, offvalue = False, bg = '#0F151D', fg = '#C96C00', highlightbackground = '#0F151D', highlightcolor = '#1E1D1D', selectcolor = '#0F151D', activebackground = '#0F151D', activeforeground = '#066D9F')
startMinimizedCheckBox.pack(side = LEFT)

#Save and cancel
saveAndCancel = Frame(root)
saveAndCancel.pack(anchor = S)

saveButton = Button(saveAndCancel, text = 'save', command = save, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
saveButton.pack(side = LEFT)

cancelButton = Button(saveAndCancel, text = 'cancel', command = cancel, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
cancelButton.pack(side = LEFT)

root.mainloop()