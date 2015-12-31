import os
import time
import Tkinter
import ScrolledText
import pygame
from Tkinter import Menu
import ttk
import tkMessageBox
import tkFileDialog

ls = "\n" * 2 # linesep
date = time.localtime()
    
top = Tkinter.Tk(className="Diary")
top.geometry('800x600')
textPad = ScrolledText.ScrolledText(top, font='Helvetica 16', width=100, height=50)

label = Tkinter.Label(top,text='What happened today?', font='Helvetica 20')
label.pack(expand=1, padx=10, pady=10,)

def open_command():
    file = tkFileDialog.askopenfile(parent=top, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()


def save_command():

    filename = r'C:\Users\Administrator\MyDiary'
    year = r'C:\Users\Administrator\MyDiary\%s' %  (str(date.tm_year))
    month = r'C:\Users\Administrator\MyDiary\%s\%s' %  (str(date.tm_year),str(date.tm_mon))
    
    if not os.path.exists(filename):
        os.mkdir(filename)
    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(month):
        os.mkdir(month)
    
    data = textPad.get('1.0',Tkinter.END+'-1c')
    length = len(data.split())
    if length > 99:
        txt_name = r"C:\Users\Administrator\MyDiary\%s\%s\%s.txt" % (str(date.tm_year),
                                            str(date.tm_mon),str(date.tm_mday))
        file = open(txt_name,'w') 
        today = time.asctime()
        
        content = today + ls + data
        file.write(content)
        file.close()
        
        pygame.mixer.init()  
        pygame.mixer.music.load(resource_path('resources/complete.wav'))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
            
        if tkMessageBox.askokcancel("Success", "Mission Complete!\nSee you tomorrow!\n: )"):
            top.destroy()
    else:
        label = tkMessageBox.showinfo("Sorry","Too short: only %d words!" % length)
        
def exit_command():
    pygame.mixer.init()  
    pygame.mixer.music.load(resource_path('resources/fail.wav'))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:  
        continue
    if tkMessageBox.askokcancel("Quit", "I feel very sorry about your abandonment.\n: ("):
        top.destroy()
    
def about_command():
    label = tkMessageBox.showinfo("About", """Name: Diary
Author: Li Hui\nEmail: withlihui@gmail.com""")
    
def rule_command():
    label = tkMessageBox.showinfo("Rules", """Rule 1: You must write no less than 100 words.
Rule 2: You only can use one emoji in one day.\nRule 3: You can only write one diary in one day.""")
    
def detail_command():
    label = tkMessageBox.showinfo("Details", """1. The file was saved in this address: 
    C:\Users\Administrator\MyDiary\...\...\
    \n2.building...""")
    
def text_length():
    data = textPad.get('1.0',Tkinter.END+'-1c')
    length = len(data.split())
    return length

    
def resource_path(relative_path):
    """
    定义一个读取相对路径的函数
    引用文件用如下格式：resource_path('resources/complete.wav')
    然后在生成的.spec文件exe = EXE()中加入下面这行：
    [('resources/complete.wav',r'C:\Users\Administrator\resources\complete.wav','music'),],
    列表中的三项分别为代码中的引用，文件实际的地址，类别
    这样打包后文件会被正确引用
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    
menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Analysis", command=None)
filemenu.add_command(label="Reflect", command=open_command, font='Helvetica 20')

# filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)
helpmenu.add_command(label="Rules", command=rule_command, font='Helvetica 20')
helpmenu.add_command(label="Details", command=detail_command)


# ft = ttk.Frame()
# fb = ttk.Frame()

# ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
# fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

# pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate', maximum=100,
    # value=0, variable=textlength)
# pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

quit = Tkinter.Button(top, text="Quit",     
    font='Helvetica 20 bold', command=exit_command,
        bg="white", fg="black")
quit.pack(fill=Tkinter.X, expand=0, padx=15, pady=15, ipadx=5, ipady=5, side = Tkinter.BOTTOM, anchor='e')

  
save = Tkinter.Button(top, text="Save", 
    font='Helvetica 20 bold', command=save_command,
        bg="black", fg="white")
save.pack(fill=Tkinter.X, expand=0, padx=15, pady=15, ipadx=5, ipady=5, side = Tkinter.BOTTOM, anchor='e' )

textPad.pack(fill=Tkinter.X, expand=1, padx=20, pady=20, side = Tkinter.TOP)
top.mainloop()