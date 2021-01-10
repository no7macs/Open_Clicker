from tkinter import *
import webbrowser, json

global loadedjsonsettings
#Super cool json file
with open('./json_settings.json','r') as settingsfile:
    jsondata = settingsfile.read()
    loadedjsonsettings = json.loads(jsondata)
    settingsfile.close()

def main():
    root = Tk()
    root.title('Open_Clicker ' + loadedjsonsettings['about']['displayVersion'] + ' About')
    root.config(bg = '#0F151D')
    root.resizable(0,0)
    root.geometry('250x100')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./favicon.png'))

    versionLabel = Label(root, text = f"Version {loadedjsonsettings['about']['version']}", bg = '#0F151D', fg = '#C96C00')
    versionLabel.pack(anchor=W)
    dateLabel = Label(root, text = f"Published on {loadedjsonsettings['about']['date']}", bg = '#0F151D', fg = '#C96C00')
    dateLabel.pack(anchor=W)

    scriptBotPhoto=PhotoImage(file="logo.png")
    scriptBotLogo = Button(root, justify=LEFT, command=lambda:webbrowser.open('https://script-bot.netlify.com'), image=scriptBotPhoto, bg='#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    scriptBotLogo.image = scriptBotPhoto
    scriptBotLogo.pack(side=LEFT)
    githubPhoto=PhotoImage(file="github.png")
    githubLink = Button(root, justify=LEFT, command=lambda:webbrowser.open('https://github.com/no7macs/Open_Clicker'), image=githubPhoto, bg='#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    githubLink.image = githubPhoto
    githubLink.pack(side=LEFT)

    root.mainloop()