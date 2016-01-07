# _*_ coding:utf-8 _*_ 
import os
import sys
import time
import Tkinter
import ScrolledText
import tkMessageBox
import tkFileDialog
import webbrowser

import pygame
import PIL
from PIL import Image, ImageTk
import tempfile

date = time.localtime()
ls = "\n" * 2 # linesep x 2

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

       
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

os.chdir(r'C:\Users\Administrator\projects\Diary')

def open_command():
    os.chdir(r'C:\Users\Administrator\MyDiary')
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
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
    
    # judge user input is 100 words or not.
    data = textPad.get('1.0',Tkinter.END+'-1c')
    length = len(data.split())
    if length > 99:
        txt_name = r"C:\Users\Administrator\MyDiary\%s\%s\%s.txt" % (str(date.tm_year),
                                            str(date.tm_mon),str(date.tm_mday))
        file = open(txt_name,'a')
        today = time.asctime()
        
        content = today + ls + data + ls
        file.write(content)
        file.close()
        
        pygame.mixer.init()  
        pygame.mixer.music.load(resource_path('resources/complete.wav'))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
            
        if tkMessageBox.askokcancel("Success", "Mission Complete!\nSee you tomorrow!\n: )"):
            root.destroy()
    else:
        label = tkMessageBox.showinfo("Sorry","Too short: only %d words!" % length)
        
def analysis_command():
    top = Tkinter.Toplevel()
    top.title("Data Analysis")
    top.geometry("800x200+400+300")
    # Count up the sum of diary.
    Diary_sum = sum([len(files) for root,dirs,files in os.walk(r'C:\Users\Administrator\MyDiary')])
    Year_sum = sum([len(files) for root,dirs,files in os.walk(r'C:\Users\Administrator\MyDiary\%s' % str(date.tm_year))])
    Month_sum = len(os.listdir(r'C:\Users\Administrator\MyDiary\%s\%s' % (str(date.tm_year),
                                            str(date.tm_mon))))

    label = Tkinter.Label(top, text="An Evidence. A Transcript. A Hope.", 
        font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="This Year: %d" % Year_sum, font='Purisa 16')
    label2 = Tkinter.Label(top, text="This Month: %d" % Month_sum, font='Purisa 16')
    label3 = Tkinter.Label(top, text="Sum: %d" % Diary_sum, font='Purisa 16')
        
    label.pack(padx=5,pady=5)
    label1.pack(padx=5,pady=5)
    label2.pack(padx=5,pady=5)
    label3.pack(padx=5,pady=5)
    top.mainloop()

def exit_command():
    # pygame.mixer.init()  
    # pygame.mixer.music.load(resource_path('resources/fail.wav'))
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy() == True:  
        # continue
    if tkMessageBox.askokcancel("Quit", "I feel very sorry about your abandonment.\n: ("):
        root.destroy()
    
def about_command():
    top = Tkinter.Toplevel()
    top.title("About")
    
    label = Tkinter.Label(top, text="100 Words", 
        font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="""v1.1
by Li Hui\nwithlihui@gmail.com""", font="Purisa 16 ")
    
    label.pack(padx=5,pady=5)
    label1.pack()
    
    img = Image.open(resource_path("resources/me.jpg"))
    me = ImageTk.PhotoImage(img)
    label2 = Tkinter.Label(top,image=me)
    label2.image = me
    label2.pack()
    
    top.mainloop()
    
def rule_command():
    
    top = Tkinter.Toplevel()
    top.title("Rules")
    top.geometry("620x300+400+300")
    
    label = Tkinter.Label(top, text="Three Rules: ", 
    font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="Rule 1: You must write no less than 100 words.", font='Purisa 16')
    label2 = Tkinter.Label(top, text="Rule 2: You can only use one emoji in one day.", font='Purisa 16')
    label3 = Tkinter.Label(top, text="Rule 3: You can not change the previous diary.", font='Purisa 16')
        
    label.pack(padx=5,pady=5)
    label1.pack(padx=5,pady=5)
    label2.pack(padx=5,pady=5)
    label3.pack(padx=5,pady=5)
    
    top.mainloop()


def detail_command():
    webbrowser.open("https://github.com/lihuii/Diary")
    

def text_length():
    data = textPad.get('1.0',Tkinter.END+'-1c')
    length = len(data.split())
    while length > 0:
        data = textPad.get('1.0',Tkinter.END+'-1c')
        length = len(data.split())
        time.sleep(1)
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
        

root = Tkinter.Tk()
root.geometry('850x650+300+50')
root.title("100 Words")
root.iconbitmap(default=ICON_PATH)

root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)

img = Image.open(resource_path("resources/smile.png"))
smile = ImageTk.PhotoImage(img)

label1 = Tkinter.Label(root,image=smile)
label1.image = smile
label1.grid(row=0, column=0)      

label2 = Tkinter.Label(root, text='What happened today?', font='Purisa 20 bold', fg="#1e6823")
label2.grid(row=0, column=4)      

label1.pack()
label2.pack()

textPad = ScrolledText.ScrolledText(root, font='Purisa 16', width=100, height=80)

quit = Tkinter.Button(root, text="Quit",     
font='Purisa 20 bold', command=exit_command,
bg="#80b3ff", fg="red")        
quit.pack(expand=0, padx=10, pady=10, ipadx=2, ipady=2, side=Tkinter.BOTTOM, anchor='e')

save = Tkinter.Button(root, text="Save", font='Purisa 20 bold', 
command=save_command,bg="#ccff66", fg="black")
save.pack(expand=0, padx=10, pady=10, ipadx=2, ipady=2, side=Tkinter.BOTTOM, anchor='e' )

menubar = Tkinter.Menu(root)
root.config(menu=menubar)
filemenu = Tkinter.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Analysis", command=analysis_command, font='Helvetica 20')
filemenu.add_separator()
filemenu.add_command(label="Reflect", command=open_command)

helpmenu = Tkinter.Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Rules", command=rule_command, font='Helvetica 20')
helpmenu.add_separator()
helpmenu.add_command(label="About", command=about_command)
helpmenu.add_command(label="100 Words Help", command=detail_command)

textPad.pack(fill=Tkinter.X, expand=1, padx=20, pady=20, side=Tkinter.TOP)
root.mainloop()