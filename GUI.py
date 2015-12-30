import os
import time
import Tkinter
import ScrolledText
import pygame
from Tkinter import Menu
import tkMessageBox
import tkFileDialog

ls = "\n" * 2 # linesep
date = time.localtime()
    
top = Tkinter.Tk(className="Diary")
top.geometry('800x800')
textPad = ScrolledText.ScrolledText(top, width=100, height=50)

label = Tkinter.Label(top,text='What happened today?')
label.pack(expand=2)

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
        pygame.mixer.music.load(r'C:\Users\Administrator\projects\Diary\resources\complete.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:  
            continue
            
        if tkMessageBox.askokcancel("Success", "Mission Complete!\nSee you tomorrow!\n:)"):
            top.destroy()
    else:
        label = tkMessageBox.showinfo("Sorry","Too short: only %d words!" % length)
        
def exit_command():
    pygame.mixer.init()  
    pygame.mixer.music.load(r'C:\Users\Administrator\projects\Diary\resources\fail.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:  
        continue
    if tkMessageBox.askokcancel("Quit", "I feel very sorry about your abandonment.\n:("):
        top.destroy()
    
def about_command():
    label = tkMessageBox.showinfo("About", """Name: Diary
Author: Li Hui\nEmail: withlihui@gmail.com""")
    
def rule_command():
    label = tkMessageBox.showinfo("Rules", """Rule 1: You must write no less than 100 words.
Rule 2: You only can use one emoji in one day.\nRule 3: You can only write one diary in one day.""")
    
def detail_command():
    label = tkMessageBox.showinfo("Details", "Nothing...")
    
    

def dummy():
    print "You fool,I am a fool command!"

menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Analysis", command=dummy)
filemenu.add_command(label="Reflect", command=open_command)

filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)
helpmenu.add_command(label="Rules", command=rule_command)
helpmenu.add_command(label="Details", command=detail_command)


quit = Tkinter.Button(top, text="Save", command=save_command,
        bg="green", fg="white")
quit.pack(expand=1, side = Tkinter.BOTTOM)

quit = Tkinter.Button(top, text="Quit", command=exit_command,
        bg="red", fg="white")
quit.pack(expand=1, side = Tkinter.BOTTOM)

textPad.pack(expand=1)
top.mainloop()



# text = Text(top,)
# text.pack(fill=X,expand=Y)


# scale = Scale(top,from_=10,to=40,
    # orient=HORIZONTAL,command=resize)
# scale.set(12)
# scale.pack(fill=X,expand=1)

# setting = Listbox(top,
    # )
# setting.pack()

# menu = Button(top,text='Menu',
    # command=setting,bg='red',fg='white')
# menu.pack(expand=1)

# setting.insert(END,"a list entry")

# for item in ["Font","Size","About"]:
    # setting.insert(END,item)

# quit = Button(top, text='Exit',
    # command=top.quit,bg='green',fg='white')
# quit.pack(expand=1)



# mainloop()
