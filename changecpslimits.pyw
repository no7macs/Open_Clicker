#from tkinter import *
from tkinter import Tk, Frame, Label, Entry, Button, TOP, END, PhotoImage, LEFT 
import win32api, json

def save(root, minvalueentry, maxvalueentry, loadedjsonsettings):
    if ''.join(i for i in str(minvalueentry.get()) if i.isdigit()) == '' or ''.join(i for i in str(minvalueentry.get()) if i.isdigit()) == '0':
        minvalueentry.delete(0,END)
        minvalueentry.insert(0,1)
    if ''.join(i for i in str(maxvalueentry.get()) if i.isdigit()) == '' or ''.join(i for i in str(maxvalueentry.get()) if i.isdigit()) == '0':
        maxvalueentry.delete(0,END)
        maxvalueentry.insert(0,1000)

    #''.join(i for i in str(minvalueentry.get()) if i.isdigit())

    with open('./json_settings.json', 'w') as writesettingsfile:

        loadedjsonsettings['mincpsval'] = minvalueentry.get()
        loadedjsonsettings['maxcpsval'] = maxvalueentry.get()

        json.dump(loadedjsonsettings, writesettingsfile)

    root.destroy()
    import main

def cancel(root):
    root.destroy()
    import main

def main():
    root = Tk()
    root.title('Change cps limits')
    root.config(bg = '#0F151D')
    root.resizable(0,0)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    entryframe = Frame(root, bg = '#0F151D')
    entryframe.pack(side = TOP)

    saveandcancelframe = Frame(root, bg = '#0F151D')
    saveandcancelframe.pack(side = TOP)

    #Entrys for changing cps

    minvaluelabel = Label(entryframe, text = 'Minimum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
    minvaluelabel.pack(side = TOP)

    minvalueentry = Entry(entryframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
    minvalueentry.pack(side = TOP)

    maxvaluelabel = Label(entryframe, text = 'Maximum Value (in milliseconds)', bg = '#0F151D', fg = '#C96C00')
    maxvaluelabel.pack(side = TOP)

    maxvalueentry = Entry(entryframe, bg = '#2B2D31', fg='#C96C00', insertbackground = '#C96C00')
    maxvalueentry.pack(side = TOP)


    #opening file and setting values
    with open('./json_settings.json','r') as settingsfile:
        jsondata = settingsfile.read()
        loadedjsonsettings = json.loads(jsondata)
        settingsfile.close()

    originalmin = str(loadedjsonsettings['mincpsval'])
    originalmax = str(loadedjsonsettings['maxcpsval'])

    #Inputing current numbers into the entrys
    minvalueentry.delete(0,END)
    minvalueentry.insert(0,str(originalmin))
    maxvalueentry.delete(0,END)
    maxvalueentry.insert(0,str(originalmax))

    #Save and Cancel button

    savebutton = Button(saveandcancelframe, text = 'Save', command = lambda: save(root, minvalueentry, maxvalueentry, loadedjsonsettings), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    savebutton.pack(side = LEFT)

    stopbutton = Button(saveandcancelframe, text = 'Cancel', command = lambda: cancel(root), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    stopbutton.pack(side = LEFT)


    root.mainloop()

print('loaded changecpslimits')
main()