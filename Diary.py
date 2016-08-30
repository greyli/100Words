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
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from Tkinter import *

from translate import GetToken, GetTextAndTranslate
#from spell import correct
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

class StopWatch(Tkinter.Frame):
    msec = 50
    def __init__(self, parent=None, **kw):
        Tkinter.Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = Tkinter.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        "make time label"
        time_label = Tkinter.Label(self, textvariable = self.timestr)
        self._setTime(self._elapsedtime)
        time_label.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        "update time label"
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)

    def _setTime(self, elap):
        "set the time format"
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set("%02d: %02d :%02d" % (minutes, seconds, hseconds))

    def Start(self):
        "start the stopwatch"
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True

    def Stop(self):
        "Stop the stopwatch"
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


class WordsCounter(Tkinter.Frame):
    msec = 100
    def __init__(self, parent=None, **kw):
        Tkinter.Frame.__init__(self, parent, kw)
        self._start = 0
        self.length = 0
        self._running = False
        self.wordstr = Tkinter.StringVar()
        self.makeWidgets()
        self.Start()

    def makeWidgets(self):
        "make time label"
        words_label = Tkinter.Label(self, textvariable = self.wordstr, 
                                    font='Purisa 20 bold', fg="#1e6823")
        self._setWords(self.length)
        words_label.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        "update time label"
        self.length = len(textPad.get('1.0', Tkinter.END+'-1c').split())
        self._setWords(self.length)
        self._timer = self.after(self.msec, self._update)

    def _setWords(self, length):
        "set the time format"
        self.wordstr.set("%d" % length)

    def Start(self):
        "start the stopwatch"
        if not self._running:
            self._start = self.length
            self._update()
            self._running = True

       
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
    
    img = PIL.Image.open(resource_path("resources/me.jpg"))
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
    label1 = Tkinter.Label(top, text="Rule 1: If you want save, write more than 100 words.", font='Purisa 16')
    label2 = Tkinter.Label(top, text="Rule 2: If you want save, write more than 100 words.", font='Purisa 16')
    label3 = Tkinter.Label(top, text="Rule 3: If you want save, write more than 100 words.", font='Purisa 16')

    label.pack(padx=5, pady=5)
    label1.pack(padx=5, pady=5)
    label2.pack(padx=5, pady=5)
    label3.pack(padx=5, pady=5)

    top.mainloop()


def detail_command():
    webbrowser.open("https://github.com/lihuii/Diary")


def time_counter():

    counter = Tkinter.Toplevel()
    counter.title("Time")
    counter.geometry("200x100+0+0")
    
    sw = StopWatch(counter)
    sw.pack(side=TOP)
    Button(counter, text="Start", command=sw.Start).pack(side=LEFT)
    Button(counter, text="Stop", command=sw.Stop).pack(side=LEFT)
    Button(counter, text="Reset", command=sw.Reset).pack(side=LEFT)
    Button(counter, text="Quit", command=counter.destroy).pack(side=LEFT)
    
def translate_word():
    global translate_top, word_entry, result_text
    translate_top = Tkinter.Toplevel()
    translate_top.title("Translate")
    translate_top.geometry("200x400+0+200")
    
    frame1 = Tkinter.Frame(translate_top)
    frame1.pack(fill=Tkinter.X)
    
    lbl1 = Tkinter.Label(frame1, text="Enter the words:")
    lbl1.pack(fill=X, padx=5, pady=5)
    
    word_entry= Tkinter.Entry(frame1)
    word_entry.pack(fill=X, padx=5,expand=True)
    word_entry.focus_set()
    
    Button(frame1, text="Submit", command=get_result).pack(fill=X, side=RIGHT, padx=5, pady=5)
    
    frame2 = Tkinter.Frame(translate_top)
    frame2.pack(fill=Tkinter.BOTH, expand=True)
    
    lbl2 = Tkinter.Label(frame2, text="Result:")
    lbl2.pack(fill=X, padx=5, pady=5)
    
    result_text = Tkinter.Text(frame2, font='12')
    result_text.pack(fill=Tkinter.BOTH, pady=5, padx=5, expand=True)
    
def get_result():
    word = Tkinter.Entry.get(word_entry)
    finalToken = GetToken()
    result = GetTextAndTranslate(finalToken, word) # get result
    result_text.delete('1.0', 'end') # clear
    result_text.insert('1.0',result)

    
def feedback_command():
    global email_top, name_entry, email_entry, fb_text
    email_top = Tkinter.Toplevel()
    email_top.title("Feedback")
    email_top.geometry("600x600+350+100")
    
    frame1 = Tkinter.Frame(email_top)
    frame1.pack(fill=Tkinter.X)
    
    lbl1 = Tkinter.Label(frame1, text="Your Name", width=9, font='Purisa 11 bold')
    lbl1.pack(side=Tkinter.LEFT, padx=5, pady=5)
    
    
    name_entry= Tkinter.Entry(frame1)
    name_entry.pack(fill=Tkinter.X, padx=5,expand=True)
    name_entry.focus_set()
    
    frame2 = Tkinter.Frame(email_top)
    frame2.pack(fill=Tkinter.X)
    
    lbl2 = Tkinter.Label(frame2, text="Your Email", width=9, font='Purisa 11 bold')
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

def splash():
    root = Tkinter.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print width, height
    root.geometry('%dx%d+%d+%d' % (width*0.4, height*0.8, width*0.3, height*0.1))
    # 保存成gif格式
    # 但是没法显示动图，待解决。
    image_file = os.getcwd() + "/splash.gif"
    # assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = Tkinter.PhotoImage(file=image_file)
    canvas = Tkinter.Canvas(root, height=height*0.8, width=width*0.8, bg="white")
    canvas.create_image(width*0.8/4, height*0.8/2, image=image)
    canvas.pack()
    # 设置splash显示的时间，单位是毫秒（milliseconds）
    root.after(5000, root.destroy)
    root.mainloop()


# todo 将guiclass化，最后实现和spalash的和平相处
root = Tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('900x700+300+50')
root.title("100 Words")
root.protocol('WM_DELETE_WINDOW', exit_command)
root.iconbitmap(default=ICON_PATH)

img1 = PIL.Image.open(resource_path("resources/smile.png"))
smile = PIL.ImageTk.PhotoImage(img1)

label1 = Tkinter.Label(root, image=smile)
label1.image = smile # 为什么要增加这条引用？
label1.pack(pady=10)

label2 = Tkinter.Label(root, text='What happened today?', font='Purisa 20 bold', fg="#1e6823")
label2.pack()

textPad = ScrolledText.ScrolledText(root, font='Purisa 16', width=140, height=100)

wc = WordsCounter(root)
wc.pack(side=TOP)

frame3 = Tkinter.Frame(root)
frame3.pack(fill=Tkinter.X,side=BOTTOM)

img3 = PIL.Image.open(resource_path("resources/save.png"))
save_img = PIL.ImageTk.PhotoImage(img3)
save = Tkinter.Button(frame3, image=save_img, command=save_command)
save.pack(side=RIGHT, expand=0, padx=10, pady=10, ipadx=2, ipady=2,anchor='e')

img4 = PIL.Image.open(resource_path("resources/clock.png"))
clock_img = PIL.ImageTk.PhotoImage(img4)
counter_bt = Tkinter.Button(frame3, image=clock_img, command=time_counter)
counter_bt.pack(side=RIGHT, expand=0, padx=10, pady=10, ipadx=2, ipady=2,anchor='e')

img5 = PIL.Image.open(resource_path("resources/find.png"))
find_img = PIL.ImageTk.PhotoImage(img5)
translate_bt = Tkinter.Button(frame3, image=find_img, command=translate_word)
translate_bt.pack(side=RIGHT, expand=0, padx=10, pady=10, ipadx=2, ipady=2,anchor='e')

# pack textPad in the end
textPad.pack(fill=Tkinter.X, expand=1, padx=20, pady=20, side=Tkinter.TOP)
textPad.focus_set()


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

root.mainloop()


#if __name__ == "__main__":
#    splash()
#    app()