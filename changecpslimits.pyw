from tkinter import *
import win32api

def save(root, hotkeys, minvalueentry, maxvalueentry):
    writesettingsfile = open('./Settings.txt','w')
    writesettingsfile.write(hotkeys + '|' + minvalueentry.get() + '|' + maxvalueentry.get())
    writesettingsfile.close()

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
    readsettingsfile = open('Settings.txt','r')
    readsettingsfilelines = readsettingsfile.readlines()
    readsettingsline = readsettingsfilelines[0]

    hotkeys = str(readsettingsline.split('|')[0]+'|'+readsettingsline.split('|')[1]+'|'+readsettingsline.split('|')[2]+'|'+readsettingsline.split('|')[3]+'|'+readsettingsline.split('|')[4])

    originalmin = str(readsettingsline.split('|')[5])
    originalmax = str(readsettingsline.split('|')[6])

    readsettingsfile.close()

    #Inputing current numbers into the entrys
    minvalueentry.delete(0,END)
    minvalueentry.insert(0,str(originalmin))
    maxvalueentry.delete(0,END)
    maxvalueentry.insert(0,str(originalmax))

    #Save and Cancel button

    savebutton = Button(saveandcancelframe, text = 'Save', command = lambda: save(root, hotkeys, minvalueentry, maxvalueentry), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    savebutton.pack(side = LEFT)

    stopbutton = Button(saveandcancelframe, text = 'Cancel', command = lambda: cancel(root), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    stopbutton.pack(side = LEFT)


    root.mainloop()

print('loaded changecpslimits')
main()