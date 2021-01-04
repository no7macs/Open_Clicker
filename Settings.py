from tkinter import *
import json

#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

root = Tk()

root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'])
root.config(bg = '#0F151D')
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

root.mainloop()