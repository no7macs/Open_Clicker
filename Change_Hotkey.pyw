<<<<<<< HEAD
from tkinter import *
import win32api, win32con, win32gui
import os

def main(root, currentbuttonlist, Hotkey):

    currentbutton = str()

    #Keyboard
    if win32api.GetAsyncKeyState(ord('A')) != 0: currentbutton = 'a'
    if win32api.GetAsyncKeyState(ord('B')) != 0: currentbutton = 'b'
    if win32api.GetAsyncKeyState(ord('C')) != 0: currentbutton = 'c'
    if win32api.GetAsyncKeyState(ord('D')) != 0: currentbutton = 'd'
    if win32api.GetAsyncKeyState(ord('E')) != 0: currentbutton = 'e'
    if win32api.GetAsyncKeyState(ord('F')) != 0: currentbutton = 'f'
    if win32api.GetAsyncKeyState(ord('G')) != 0: currentbutton = 'g'
    if win32api.GetAsyncKeyState(ord('H')) != 0: currentbutton = 'h'
    if win32api.GetAsyncKeyState(ord('I')) != 0: currentbutton = 'i'
    if win32api.GetAsyncKeyState(ord('J')) != 0: currentbutton = 'j'
    if win32api.GetAsyncKeyState(ord('K')) != 0: currentbutton = 'k'
    if win32api.GetAsyncKeyState(ord('L')) != 0: currentbutton = 'l'
    if win32api.GetAsyncKeyState(ord('M')) != 0: currentbutton = 'm'
    if win32api.GetAsyncKeyState(ord('N')) != 0: currentbutton = 'n'
    if win32api.GetAsyncKeyState(ord('O')) != 0: currentbutton = 'o'
    if win32api.GetAsyncKeyState(ord('P')) != 0: currentbutton = 'p'
    if win32api.GetAsyncKeyState(ord('Q')) != 0: currentbutton = 'q'
    if win32api.GetAsyncKeyState(ord('R')) != 0: currentbutton = 'r'
    if win32api.GetAsyncKeyState(ord('S')) != 0: currentbutton = 's'
    if win32api.GetAsyncKeyState(ord('T')) != 0: currentbutton = 't'
    if win32api.GetAsyncKeyState(ord('U')) != 0: currentbutton = 'u'
    if win32api.GetAsyncKeyState(ord('V')) != 0: currentbutton = 'v'
    if win32api.GetAsyncKeyState(ord('W')) != 0: currentbutton = 'w'
    if win32api.GetAsyncKeyState(ord('X')) != 0: currentbutton = 'x'
    if win32api.GetAsyncKeyState(ord('Y')) != 0: currentbutton = 'y'
    if win32api.GetAsyncKeyState(ord('Z')) != 0: currentbutton = 'z'
    if win32api.GetAsyncKeyState(ord('1')) != 0: currentbutton = '1'
    if win32api.GetAsyncKeyState(ord('2')) != 0: currentbutton = '2'
    if win32api.GetAsyncKeyState(ord('3')) != 0: currentbutton = '3'
    if win32api.GetAsyncKeyState(ord('4')) != 0: currentbutton = '4'
    if win32api.GetAsyncKeyState(ord('5')) != 0: currentbutton = '5'
    if win32api.GetAsyncKeyState(ord('6')) != 0: currentbutton = '6'
    if win32api.GetAsyncKeyState(ord('7')) != 0: currentbutton = '7'
    if win32api.GetAsyncKeyState(ord('8')) != 0: currentbutton = '8'
    if win32api.GetAsyncKeyState(ord('9')) != 0: currentbutton = '9'
    if win32api.GetAsyncKeyState(ord('0')) != 0: currentbutton = '0'
    if win32api.GetAsyncKeyState(win32con.VK_BACK) != 0: currentbutton = 'back'
    if win32api.GetAsyncKeyState(win32con.VK_TAB) != 0: currentbutton = 'tab'
    if win32api.GetAsyncKeyState(win32con.VK_CLEAR) != 0: currentbutton = 'clear'
    if win32api.GetAsyncKeyState(win32con.VK_RETURN) != 0: currentbutton = 'enter'
    if win32api.GetAsyncKeyState(win32con.VK_SHIFT) != 0: currentbutton = 'shift'
    if win32api.GetAsyncKeyState(win32con.VK_CONTROL) != 0: currentbutton = 'ctrl'
    if win32api.GetAsyncKeyState(win32con.VK_MENU) != 0: currentbutton = 'alt'
    if win32api.GetAsyncKeyState(win32con.VK_PAUSE) != 0: currentbutton = 'pause'
    if win32api.GetAsyncKeyState(win32con.VK_CAPITAL) != 0: currentbutton = 'caps'
    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0: currentbutton = 'esc'
    if win32api.GetAsyncKeyState(win32con.VK_SPACE) != 0: currentbutton = 'space'
    if win32api.GetAsyncKeyState(win32con.VK_PRIOR) != 0: currentbutton = 'pg_up'
    if win32api.GetAsyncKeyState(win32con.VK_NEXT) != 0: currentbutton = 'pg_dwn'
    if win32api.GetAsyncKeyState(win32con.VK_END) != 0: currentbutton = 'end'
    if win32api.GetAsyncKeyState(win32con.VK_HOME) != 0: currentbutton = 'home'
    if win32api.GetAsyncKeyState(win32con.VK_LEFT) != 0: currentbutton = 'left'
    if win32api.GetAsyncKeyState(win32con.VK_UP) != 0: currentbutton = 'up'
    if win32api.GetAsyncKeyState(win32con.VK_RIGHT) != 0: currentbutton = 'right'
    if win32api.GetAsyncKeyState(win32con.VK_DOWN) != 0: currentbutton = 'down'
    if win32api.GetAsyncKeyState(win32con.VK_SELECT) != 0: currentbutton = 'select'
    if win32api.GetAsyncKeyState(win32con.VK_PRINT) != 0: currentbutton = 'print'
    if win32api.GetAsyncKeyState(win32con.VK_EXECUTE) != 0: currentbutton = 'execute'
    if win32api.GetAsyncKeyState(win32con.VK_SNAPSHOT) != 0: currentbutton = 'prnt_scrn'
    if win32api.GetAsyncKeyState(win32con.VK_INSERT) != 0: currentbutton = 'insert'
    if win32api.GetAsyncKeyState(win32con.VK_DELETE) != 0: currentbutton = 'delete'
    if win32api.GetAsyncKeyState(win32con.VK_HELP) != 0: currentbutton = 'help'
    if win32api.GetAsyncKeyState(win32con.VK_LWIN) != 0: currentbutton = 'left_win'
    if win32api.GetAsyncKeyState(win32con.VK_RWIN) != 0: currentbutton = 'right_win'
    if win32api.GetAsyncKeyState(win32con.VK_APPS) != 0: currentbutton = 'app_key'
    #if win32api.GetAsyncKeyState(win32con.VK_SLEEP) != 0: currentbutton = 'sleep'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) != 0: currentbutton = 'num_pad_1'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) != 0: currentbutton = 'num_pad_2'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) != 0: currentbutton = 'num_pad_3'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) != 0: currentbutton = 'num_pad_4'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD5) != 0: currentbutton = 'num_pad_5'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD6) != 0: currentbutton = 'num_pad_6'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD7) != 0: currentbutton = 'num_pad_7'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD8) != 0: currentbutton = 'num_pad_8'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD9) != 0: currentbutton = 'num_pad_9'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD0) != 0: currentbutton = 'num_pad_0'
    #if win32api.GetAsyncKeyState(win32con.VK_MULTIPLY) != 0: currentbutton = 'multiply'
    #if win32api.GetAsyncKeyState(win32con.VK_ADD) != 0: currentbutton = 'add'
    #if win32api.GetAsyncKeyState(win32con.VK_SEPERATOR) != 0: currentbutton = 'seperator'
    if win32api.GetAsyncKeyState(win32con.VK_SUBTRACT) != 0: currentbutton = 'subtract'
    if win32api.GetAsyncKeyState(win32con.VK_DECIMAL) != 0: currentbutton = 'decimal'
    if win32api.GetAsyncKeyState(win32con.VK_DIVIDE) != 0: currentbutton = 'divide'
    if win32api.GetAsyncKeyState(win32con.VK_F1) != 0: currentbutton = 'f1'
    if win32api.GetAsyncKeyState(win32con.VK_F2) != 0: currentbutton = 'f2'
    if win32api.GetAsyncKeyState(win32con.VK_F3) != 0: currentbutton = 'f3'
    if win32api.GetAsyncKeyState(win32con.VK_F4) != 0: currentbutton = 'f4'
    if win32api.GetAsyncKeyState(win32con.VK_F5) != 0: currentbutton = 'f5'
    if win32api.GetAsyncKeyState(win32con.VK_F6) != 0: currentbutton = 'f6'
    if win32api.GetAsyncKeyState(win32con.VK_F7) != 0: currentbutton = 'f7'
    if win32api.GetAsyncKeyState(win32con.VK_F8) != 0: currentbutton = 'f8'
    if win32api.GetAsyncKeyState(win32con.VK_F9) != 0: currentbutton = 'f9'
    if win32api.GetAsyncKeyState(win32con.VK_F10) != 0: currentbutton = 'f10'
    if win32api.GetAsyncKeyState(win32con.VK_F11) != 0: currentbutton = 'f11'
    if win32api.GetAsyncKeyState(win32con.VK_F12) != 0: currentbutton = 'f12'
    if win32api.GetAsyncKeyState(win32con.VK_F13) != 0: currentbutton = 'f13'
    if win32api.GetAsyncKeyState(win32con.VK_F14) != 0: currentbutton = 'f14'
    if win32api.GetAsyncKeyState(win32con.VK_F15) != 0: currentbutton = 'f15'
    if win32api.GetAsyncKeyState(win32con.VK_F16) != 0: currentbutton = 'f16'
    if win32api.GetAsyncKeyState(win32con.VK_F17) != 0: currentbutton = 'f17'
    if win32api.GetAsyncKeyState(win32con.VK_F18) != 0: currentbutton = 'f18'
    if win32api.GetAsyncKeyState(win32con.VK_F19) != 0: currentbutton = 'f19'
    if win32api.GetAsyncKeyState(win32con.VK_F20) != 0: currentbutton = 'f20'
    if win32api.GetAsyncKeyState(win32con.VK_F21) != 0: currentbutton = 'f21'
    if win32api.GetAsyncKeyState(win32con.VK_F22) != 0: currentbutton = 'f22'
    if win32api.GetAsyncKeyState(win32con.VK_F23) != 0: currentbutton = 'f23'
    if win32api.GetAsyncKeyState(win32con.VK_F24) != 0: currentbutton = 'f24'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_PLUS) != 0: currentbutton = 'plus'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_COMMA) != 0: currentbutton = 'comma'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_MINUS) != 0: currentbutton = 'minus'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_PERIOD) != 0: currentbutton = 'period'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_2) != 0: currentbutton = '/'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_3) != 0: currentbutton = '~'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_4) != 0: currentbutton = '[{'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_5) != 0: currentbutton = '\|'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_6) != 0: currentbutton = ']}'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_7) != 0: currentbutton = 'comma'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_8) != 0: currentbutton = 'miscellaneous'
    #Mouse
    #if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) != 0: currentbutton = 'mouse_lcb'
    #if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) != 0: currentbutton = 'mouse_rcb'
    #if win32api.GetAsyncKeyState(win32con.VK_MBUTTON) != 0: currentbutton = 'mouse_mcb'
    #if win32api.GetAsyncKeyState(win32con.VK_XBUTTON1) != 0: currentbutton = 'mouse_xb1'
    #if win32api.GetAsyncKeyState(win32con.VK_XBUTTON2) != 0: currentbutton = 'mouse_xb2'

    if currentbutton != '':
        if (currentbutton + '+') not in currentbuttonlist:
            currentbuttonlist.append(currentbutton + '+')

    Hotkey.config(text = ''.join(currentbuttonlist))

    print(currentbuttonlist)

    root.after(100, lambda: main(root, currentbuttonlist, Hotkey))

def sethotkey(root, buttontype, currentbuttonlist, Hotkeyfile, Hotkeyline, Hotkeylistread): 

    os.remove('./Settings.txt')

    Hotkeyfile = open('./Settings.txt','w+')
    Hotkeyline = Hotkeyfile.readlines()
    Hotkeylist = ''.join(Hotkeyline).split('|')
    #print(str(Hotkeyline).split('|'))
    print(''.join(Hotkeyline).split('|'))

    #Hotkeyfile = open('./Settings.txt','w')
    #Hotkeyline = Hotkeyfile.readlines()
    print('--Hotkeyline--' + str(Hotkeyline))
    print(Hotkeylist)
    Hotkeylistread[1] = ''.join(currentbuttonlist)
    #'|'.join(Hotkeylist)
    #Hotkeyfile.write(Hotkeylist[0] + '|' + Hotkeylist[1] + '|' + Hotkeylist[2] + '|' + Hotkeylist[3] + '|' + Hotkeylist[4] + '|')
    print(Hotkeyline)
    print(Hotkeyfile.readlines())

def done(root):
    root.destroy()
    import main

def start(buttontype):

    currentbuttonlist = []

    Hotkeyfile = open('./Settings.txt','r')
    Hotkeyline = Hotkeyfile.readlines()
    Hotkeylistread = ''.join(Hotkeyline).split('|')
    #print(str(Hotkeyline).split('|'))
    print(''.join(Hotkeyline).split('|'))
    print(Hotkeylistread[buttontype])
    Changehotkey = Hotkeylistread[buttontype]
    Hotkeyfile.close()

    root = Tk()
    root.title('Change Hotkey')
    root.config(bg = '#0F151D')

    Hotkey = Label(root, text = 'Hotkey: ', bg = '#0F151D', fg = '#C96C00')
    Hotkey.pack(anchor = W)

    buttonframe = Frame(root)
    buttonframe.pack(anchor = W)

    sethotkeybutton = Button(buttonframe, text = 'SET', command = lambda: sethotkey(root, buttontype, currentbuttonlist, Hotkeyfile, Hotkeyline, Hotkeylistread), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    sethotkeybutton.pack(side = LEFT)

    cancel = Button(buttonframe, text = 'CANCEL', command = lambda: done(root), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    cancel.pack(side = LEFT)

    root.after(1, lambda: main(root, currentbuttonlist, Hotkey))
    root.mainloop()

=======
from tkinter import *
import win32api, win32con, win32gui
import os

def main(root, currentbuttonlist, Hotkey):

    currentbutton = str()

    #Keyboard
    if win32api.GetAsyncKeyState(ord('A')) != 0: currentbutton = 'a'
    if win32api.GetAsyncKeyState(ord('B')) != 0: currentbutton = 'b'
    if win32api.GetAsyncKeyState(ord('C')) != 0: currentbutton = 'c'
    if win32api.GetAsyncKeyState(ord('D')) != 0: currentbutton = 'd'
    if win32api.GetAsyncKeyState(ord('E')) != 0: currentbutton = 'e'
    if win32api.GetAsyncKeyState(ord('F')) != 0: currentbutton = 'f'
    if win32api.GetAsyncKeyState(ord('G')) != 0: currentbutton = 'g'
    if win32api.GetAsyncKeyState(ord('H')) != 0: currentbutton = 'h'
    if win32api.GetAsyncKeyState(ord('I')) != 0: currentbutton = 'i'
    if win32api.GetAsyncKeyState(ord('J')) != 0: currentbutton = 'j'
    if win32api.GetAsyncKeyState(ord('K')) != 0: currentbutton = 'k'
    if win32api.GetAsyncKeyState(ord('L')) != 0: currentbutton = 'l'
    if win32api.GetAsyncKeyState(ord('M')) != 0: currentbutton = 'm'
    if win32api.GetAsyncKeyState(ord('N')) != 0: currentbutton = 'n'
    if win32api.GetAsyncKeyState(ord('O')) != 0: currentbutton = 'o'
    if win32api.GetAsyncKeyState(ord('P')) != 0: currentbutton = 'p'
    if win32api.GetAsyncKeyState(ord('Q')) != 0: currentbutton = 'q'
    if win32api.GetAsyncKeyState(ord('R')) != 0: currentbutton = 'r'
    if win32api.GetAsyncKeyState(ord('S')) != 0: currentbutton = 's'
    if win32api.GetAsyncKeyState(ord('T')) != 0: currentbutton = 't'
    if win32api.GetAsyncKeyState(ord('U')) != 0: currentbutton = 'u'
    if win32api.GetAsyncKeyState(ord('V')) != 0: currentbutton = 'v'
    if win32api.GetAsyncKeyState(ord('W')) != 0: currentbutton = 'w'
    if win32api.GetAsyncKeyState(ord('X')) != 0: currentbutton = 'x'
    if win32api.GetAsyncKeyState(ord('Y')) != 0: currentbutton = 'y'
    if win32api.GetAsyncKeyState(ord('Z')) != 0: currentbutton = 'z'
    if win32api.GetAsyncKeyState(ord('1')) != 0: currentbutton = '1'
    if win32api.GetAsyncKeyState(ord('2')) != 0: currentbutton = '2'
    if win32api.GetAsyncKeyState(ord('3')) != 0: currentbutton = '3'
    if win32api.GetAsyncKeyState(ord('4')) != 0: currentbutton = '4'
    if win32api.GetAsyncKeyState(ord('5')) != 0: currentbutton = '5'
    if win32api.GetAsyncKeyState(ord('6')) != 0: currentbutton = '6'
    if win32api.GetAsyncKeyState(ord('7')) != 0: currentbutton = '7'
    if win32api.GetAsyncKeyState(ord('8')) != 0: currentbutton = '8'
    if win32api.GetAsyncKeyState(ord('9')) != 0: currentbutton = '9'
    if win32api.GetAsyncKeyState(ord('0')) != 0: currentbutton = '0'
    if win32api.GetAsyncKeyState(win32con.VK_BACK) != 0: currentbutton = 'back'
    if win32api.GetAsyncKeyState(win32con.VK_TAB) != 0: currentbutton = 'tab'
    if win32api.GetAsyncKeyState(win32con.VK_CLEAR) != 0: currentbutton = 'clear'
    if win32api.GetAsyncKeyState(win32con.VK_RETURN) != 0: currentbutton = 'enter'
    if win32api.GetAsyncKeyState(win32con.VK_SHIFT) != 0: currentbutton = 'shift'
    if win32api.GetAsyncKeyState(win32con.VK_CONTROL) != 0: currentbutton = 'ctrl'
    if win32api.GetAsyncKeyState(win32con.VK_MENU) != 0: currentbutton = 'alt'
    if win32api.GetAsyncKeyState(win32con.VK_PAUSE) != 0: currentbutton = 'pause'
    if win32api.GetAsyncKeyState(win32con.VK_CAPITAL) != 0: currentbutton = 'caps'
    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0: currentbutton = 'esc'
    if win32api.GetAsyncKeyState(win32con.VK_SPACE) != 0: currentbutton = 'space'
    if win32api.GetAsyncKeyState(win32con.VK_PRIOR) != 0: currentbutton = 'pg_up'
    if win32api.GetAsyncKeyState(win32con.VK_NEXT) != 0: currentbutton = 'pg_dwn'
    if win32api.GetAsyncKeyState(win32con.VK_END) != 0: currentbutton = 'end'
    if win32api.GetAsyncKeyState(win32con.VK_HOME) != 0: currentbutton = 'home'
    if win32api.GetAsyncKeyState(win32con.VK_LEFT) != 0: currentbutton = 'left'
    if win32api.GetAsyncKeyState(win32con.VK_UP) != 0: currentbutton = 'up'
    if win32api.GetAsyncKeyState(win32con.VK_RIGHT) != 0: currentbutton = 'right'
    if win32api.GetAsyncKeyState(win32con.VK_DOWN) != 0: currentbutton = 'down'
    if win32api.GetAsyncKeyState(win32con.VK_SELECT) != 0: currentbutton = 'select'
    if win32api.GetAsyncKeyState(win32con.VK_PRINT) != 0: currentbutton = 'print'
    if win32api.GetAsyncKeyState(win32con.VK_EXECUTE) != 0: currentbutton = 'execute'
    if win32api.GetAsyncKeyState(win32con.VK_SNAPSHOT) != 0: currentbutton = 'prnt_scrn'
    if win32api.GetAsyncKeyState(win32con.VK_INSERT) != 0: currentbutton = 'insert'
    if win32api.GetAsyncKeyState(win32con.VK_DELETE) != 0: currentbutton = 'delete'
    if win32api.GetAsyncKeyState(win32con.VK_HELP) != 0: currentbutton = 'help'
    if win32api.GetAsyncKeyState(win32con.VK_LWIN) != 0: currentbutton = 'left_win'
    if win32api.GetAsyncKeyState(win32con.VK_RWIN) != 0: currentbutton = 'right_win'
    if win32api.GetAsyncKeyState(win32con.VK_APPS) != 0: currentbutton = 'app_key'
    #if win32api.GetAsyncKeyState(win32con.VK_SLEEP) != 0: currentbutton = 'sleep'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) != 0: currentbutton = 'num_pad_1'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) != 0: currentbutton = 'num_pad_2'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) != 0: currentbutton = 'num_pad_3'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) != 0: currentbutton = 'num_pad_4'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD5) != 0: currentbutton = 'num_pad_5'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD6) != 0: currentbutton = 'num_pad_6'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD7) != 0: currentbutton = 'num_pad_7'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD8) != 0: currentbutton = 'num_pad_8'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD9) != 0: currentbutton = 'num_pad_9'
    #if win32api.GetAsyncKeyState(win32con.VK_NUMPAD0) != 0: currentbutton = 'num_pad_0'
    #if win32api.GetAsyncKeyState(win32con.VK_MULTIPLY) != 0: currentbutton = 'multiply'
    #if win32api.GetAsyncKeyState(win32con.VK_ADD) != 0: currentbutton = 'add'
    #if win32api.GetAsyncKeyState(win32con.VK_SEPERATOR) != 0: currentbutton = 'seperator'
    if win32api.GetAsyncKeyState(win32con.VK_SUBTRACT) != 0: currentbutton = 'subtract'
    if win32api.GetAsyncKeyState(win32con.VK_DECIMAL) != 0: currentbutton = 'decimal'
    if win32api.GetAsyncKeyState(win32con.VK_DIVIDE) != 0: currentbutton = 'divide'
    if win32api.GetAsyncKeyState(win32con.VK_F1) != 0: currentbutton = 'f1'
    if win32api.GetAsyncKeyState(win32con.VK_F2) != 0: currentbutton = 'f2'
    if win32api.GetAsyncKeyState(win32con.VK_F3) != 0: currentbutton = 'f3'
    if win32api.GetAsyncKeyState(win32con.VK_F4) != 0: currentbutton = 'f4'
    if win32api.GetAsyncKeyState(win32con.VK_F5) != 0: currentbutton = 'f5'
    if win32api.GetAsyncKeyState(win32con.VK_F6) != 0: currentbutton = 'f6'
    if win32api.GetAsyncKeyState(win32con.VK_F7) != 0: currentbutton = 'f7'
    if win32api.GetAsyncKeyState(win32con.VK_F8) != 0: currentbutton = 'f8'
    if win32api.GetAsyncKeyState(win32con.VK_F9) != 0: currentbutton = 'f9'
    if win32api.GetAsyncKeyState(win32con.VK_F10) != 0: currentbutton = 'f10'
    if win32api.GetAsyncKeyState(win32con.VK_F11) != 0: currentbutton = 'f11'
    if win32api.GetAsyncKeyState(win32con.VK_F12) != 0: currentbutton = 'f12'
    if win32api.GetAsyncKeyState(win32con.VK_F13) != 0: currentbutton = 'f13'
    if win32api.GetAsyncKeyState(win32con.VK_F14) != 0: currentbutton = 'f14'
    if win32api.GetAsyncKeyState(win32con.VK_F15) != 0: currentbutton = 'f15'
    if win32api.GetAsyncKeyState(win32con.VK_F16) != 0: currentbutton = 'f16'
    if win32api.GetAsyncKeyState(win32con.VK_F17) != 0: currentbutton = 'f17'
    if win32api.GetAsyncKeyState(win32con.VK_F18) != 0: currentbutton = 'f18'
    if win32api.GetAsyncKeyState(win32con.VK_F19) != 0: currentbutton = 'f19'
    if win32api.GetAsyncKeyState(win32con.VK_F20) != 0: currentbutton = 'f20'
    if win32api.GetAsyncKeyState(win32con.VK_F21) != 0: currentbutton = 'f21'
    if win32api.GetAsyncKeyState(win32con.VK_F22) != 0: currentbutton = 'f22'
    if win32api.GetAsyncKeyState(win32con.VK_F23) != 0: currentbutton = 'f23'
    if win32api.GetAsyncKeyState(win32con.VK_F24) != 0: currentbutton = 'f24'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_PLUS) != 0: currentbutton = 'plus'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_COMMA) != 0: currentbutton = 'comma'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_MINUS) != 0: currentbutton = 'minus'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_PERIOD) != 0: currentbutton = 'period'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_2) != 0: currentbutton = '/'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_3) != 0: currentbutton = '~'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_4) != 0: currentbutton = '[{'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_5) != 0: currentbutton = '\|'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_6) != 0: currentbutton = ']}'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_7) != 0: currentbutton = 'comma'
    #if win32api.GetAsyncKeyState(win32con.VK_OEM_8) != 0: currentbutton = 'miscellaneous'
    #Mouse
    #if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) != 0: currentbutton = 'mouse_lcb'
    #if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) != 0: currentbutton = 'mouse_rcb'
    #if win32api.GetAsyncKeyState(win32con.VK_MBUTTON) != 0: currentbutton = 'mouse_mcb'
    #if win32api.GetAsyncKeyState(win32con.VK_XBUTTON1) != 0: currentbutton = 'mouse_xb1'
    #if win32api.GetAsyncKeyState(win32con.VK_XBUTTON2) != 0: currentbutton = 'mouse_xb2'

    if currentbutton != '':
        if (currentbutton + '+') not in currentbuttonlist:
            currentbuttonlist.append(currentbutton + '+')

    Hotkey.config(text = ''.join(currentbuttonlist))

    print(currentbuttonlist)

    root.after(100, lambda: main(root, currentbuttonlist, Hotkey))

def sethotkey(root, buttontype, currentbuttonlist, Hotkeyfile, Hotkeyline, Hotkeylistread): 

    os.remove('./Settings.txt')

    Hotkeyfile = open('./Settings.txt','w+')
    Hotkeyline = Hotkeyfile.readlines()
    Hotkeylist = ''.join(Hotkeyline).split('|')
    #print(str(Hotkeyline).split('|'))
    print(''.join(Hotkeyline).split('|'))

    #Hotkeyfile = open('./Settings.txt','w')
    #Hotkeyline = Hotkeyfile.readlines()
    print('--Hotkeyline--' + str(Hotkeyline))
    print(Hotkeylist)
    Hotkeylistread[1] = ''.join(currentbuttonlist)
    #'|'.join(Hotkeylist)
    #Hotkeyfile.write(Hotkeylist[0] + '|' + Hotkeylist[1] + '|' + Hotkeylist[2] + '|' + Hotkeylist[3] + '|' + Hotkeylist[4] + '|')
    print(Hotkeyline)
    print(Hotkeyfile.readlines())

def done(root):
    root.destroy()
    import main

def start(buttontype):

    currentbuttonlist = []

    Hotkeyfile = open('./Settings.txt','r')
    Hotkeyline = Hotkeyfile.readlines()
    Hotkeylistread = ''.join(Hotkeyline).split('|')
    #print(str(Hotkeyline).split('|'))
    print(''.join(Hotkeyline).split('|'))
    print(Hotkeylistread[buttontype])
    Changehotkey = Hotkeylistread[buttontype]
    Hotkeyfile.close()

    root = Tk()
    root.title('Change Hotkey')
    root.config(bg = '#0F151D')

    Hotkey = Label(root, text = 'Hotkey: ', bg = '#0F151D', fg = '#C96C00')
    Hotkey.pack(anchor = W)

    buttonframe = Frame(root)
    buttonframe.pack(anchor = W)

    sethotkeybutton = Button(buttonframe, text = 'SET', command = lambda: sethotkey(root, buttontype, currentbuttonlist, Hotkeyfile, Hotkeyline, Hotkeylistread), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    sethotkeybutton.pack(side = LEFT)

    cancel = Button(buttonframe, text = 'CANCEL', command = lambda: done(root), bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    cancel.pack(side = LEFT)

    root.after(1, lambda: main(root, currentbuttonlist, Hotkey))
    root.mainloop()

>>>>>>> 0fc482b7ca6dc28bff516e6e1a72022ebae82dd4
start(1)