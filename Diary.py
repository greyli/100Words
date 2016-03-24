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
from PIL import Image, ImageTk
import tempfile

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

from spell import correct
date = time.localtime()
ls = "\n" * 2   # linesep x 2

# hide the 'tk' icon
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


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
    month = r'C:\Users\Administrator\MyDiary\%s\%s' %  (str(date.tm_year), str(date.tm_mon))
    
    if not os.path.exists(filename):
        os.mkdir(filename)
    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(month):
        os.mkdir(month)
    
    # judge user input is 100 words or not.
    data = textPad.get('1.0', Tkinter.END+'-1c')
    # for word in data.split():
    #     if word != correct(word):
    #         print correct(word)

    length = len(data.split())
    if length > 99:

        txt_name = r"C:\Users\Administrator\MyDiary\%s\%s\%s.txt" % (str(date.tm_year),
                                            str(date.tm_mon), str(date.tm_mday))
        file = open(txt_name, 'a')
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
        label = tkMessageBox.showinfo("Sorry", "Too short: Only %d words!" % length)


def analysis_command():
    top = Tkinter.Toplevel()
    top.title("Data Analysis")
    top.geometry("800x200+350+300")
    # Count up the sum of diary.
    Diary_sum = sum([len(files) for root, dirs, files in os.walk(r'C:\Users\Administrator\MyDiary')])
    Year_sum = sum([len(files) for root, dirs, files in os.walk(r'C:\Users\Administrator\MyDiary\%s'
    % str(date.tm_year))])
    Month_sum = len(os.listdir(r'C:\Users\Administrator\MyDiary\%s\%s' % (str(date.tm_year),
                                            str(date.tm_mon))))

    label = Tkinter.Label(top, text="This is an EVIDENCE for your fail or success.", 
        font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="This Year: %d" % Year_sum, font='Purisa 16')
    label2 = Tkinter.Label(top, text="This Month: %d" % Month_sum, font='Purisa 16')
    label3 = Tkinter.Label(top, text="Sum: %d" % Diary_sum, font='Purisa 16')
        
    label.pack(padx=5, pady=5)
    label1.pack(padx=5, pady=5)
    label2.pack(padx=5, pady=5)
    label3.pack(padx=5, pady=5)
    top.mainloop()


def exit_command():
    if tkMessageBox.askokcancel("Quit", "I feel very sorry about your abandonment.\nReally want to QUIT? : ("):
        root.destroy()


def about_command():
    top = Tkinter.Toplevel()
    top.title("About")

    label = Tkinter.Label(top, text="100 Words",
        font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="""v1.1
by Li Hui\nwithlihui@gmail.com""", font="Purisa 16 ")

    label.pack(padx=5, pady=5)
    label1.pack()
    
    img = Image.open(resource_path("resources/me.jpg"))
    me = ImageTk.PhotoImage(img)
    label2 = Tkinter.Label(top, image=me)
    label2.image = me
    label2.pack()


def rule_command():
    top = Tkinter.Toplevel()
    top.title("Rules")
    top.geometry("820x300+400+300")

    label = Tkinter.Label(top, text="Three Rules: ",
                          font='Purisa 20 bold', fg='#1e6823')
    label1 = Tkinter.Label(top, text="Rule 1: You must write no less than 100 words.", font='Purisa 16')
    label2 = Tkinter.Label(top, text="Rule 2: You can only use one emoji in one day (in building...) .", font='Purisa 16')
    label3 = Tkinter.Label(top, text="Rule 3: You can not change the previous diary.", font='Purisa 16')

    label.pack(padx=5, pady=5)
    label1.pack(padx=5, pady=5)
    label2.pack(padx=5, pady=5)
    label3.pack(padx=5, pady=5)
    
    top.mainloop()


def detail_command():
    webbrowser.open("https://github.com/lihuii/Diary")


def feedback_command():
    global email_top, name_entry, email_entry, fb_text
    email_top = Tkinter.Toplevel()
    email_top.title("Feedback")
    email_top.geometry("600x600+350+100")
    
    frame1 = Tkinter.Frame(email_top)
    frame1.pack(fill=Tkinter.X)
    
    lbl1 = Tkinter.Label(frame1, text="Name", width=7, font='Purisa 11 bold')
    lbl1.pack(side=Tkinter.LEFT, padx=5, pady=5)
    
    
    name_entry= Tkinter.Entry(frame1)
    name_entry.pack(fill=Tkinter.X, padx=5,expand=True)
    name_entry.focus_set()
    
    frame2 = Tkinter.Frame(email_top)
    frame2.pack(fill=Tkinter.X)
    
    lbl2 = Tkinter.Label(frame2, text="Email", width=7, font='Purisa 11 bold')
    lbl2.pack(side=Tkinter.LEFT, padx=5, pady=5)
    
    email_entry= Tkinter.Entry(frame2)
    email_entry.pack(fill=Tkinter.X, padx=5,expand=True)
    
    frame3 = Tkinter.Frame(email_top)
    frame3.pack(fill=Tkinter.BOTH, expand=True)
    
    lbl3 = Tkinter.Label(frame3, text="Feedback", width=7, font='Purisa 11 bold')
    lbl3.pack(side=Tkinter.LEFT, anchor=Tkinter.N, padx=5, pady=5)
    
    fb_text = Tkinter.Text(frame3, font='12')
    fb_text.pack(fill=Tkinter.BOTH, pady=5, padx=5, expand=True)

    button = Tkinter.Button(email_top, text='Send', command=send_feedback, font='Purisa 12 bold',
bg="white", fg="red")
    button.pack(side=Tkinter.BOTTOM, anchor=Tkinter.E, padx=50, pady=10)
    
    
def send_feedback():
    
    name = Tkinter.Entry.get(name_entry)
    email = Tkinter.Entry.get(email_entry)
    content = fb_text.get('1.0', Tkinter.END)
    feedback = name + ls + email + ls + content

    if len(feedback) < 6:
        label = tkMessageBox.showinfo("Error!", "You wrote nothing.\n*_*")
        email_top.destroy()
        return None
            
    sender = "mimi_19@sina.com"
    receiver = ["withlihui@qq.com"]
    subject = "feedback"
    smtpserver = "smtp.sina.com"
    username = "mimi_19@sina.com"
    password = "december"

    msg = MIMEMultipart()
    content = MIMEText(feedback, 'plain', 'utf-8')

    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ",".join(receiver)
    msg.attach(content)

    smtp = smtplib.SMTP(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    
    if tkMessageBox.askokcancel("Success!", "Thanks for your suggestions or feedback."):
        email_top.destroy()
            

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
root.geometry('900x700+300+50')
root.title("100 Words")
root.iconbitmap(default=ICON_PATH)

img = Image.open(resource_path("resources/smile.png"))
smile = ImageTk.PhotoImage(img)

label1 = Tkinter.Label(root, image=smile)
label1.image = smile      

label2 = Tkinter.Label(root, text='What happened today?', font='Purisa 20 bold', fg="#1e6823")  

label1.pack()
label2.pack()

textPad = ScrolledText.ScrolledText(root, font='Purisa 16', width=140, height=100)

quit_bt = Tkinter.Button(root, text="Quit", font='Purisa 20 bold',
                      command=exit_command, bg="#80b3ff", fg="red")
quit_bt.pack(fill=Tkinter.X, expand=0, padx=10, pady=10, side=Tkinter.BOTTOM, anchor='e')

save = Tkinter.Button(root, text="Save", font='Purisa 20 bold',
                      command=save_command, bg="#ccff66", fg="black")
save.pack(fill=Tkinter.X, expand=0, padx=10, pady=10, ipadx=2, ipady=2, side=Tkinter.BOTTOM, anchor='e')

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
helpmenu.add_command(label="Feedback", command=feedback_command)
helpmenu.add_command(label="100 Words Help", command=detail_command)

textPad.pack(fill=Tkinter.X, expand=1, padx=20, pady=20, side=Tkinter.TOP)
textPad.focus_set()
root.mainloop()
