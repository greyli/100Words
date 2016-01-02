# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, RIGHT, RAISED
from ttk import Button, Frame, Style

os.chdir(r'D:\checkfile\girls\douban')
class Example(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        
        
        self.initUI()
        
    def initUI(self):
        
        label = Label(self,text='What happened today?', font='Helvetica 15')
        label.pack(padx=10, pady=10,)
    
        self.parent.title("Quit")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="#d6e685") # #1e6823 #8cc665 #d6e685
        
        frame = Frame(self,relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        
        
       
        quitButton = Button(self, text="Quit",
            command=self.quit)
        
        quitButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
        
def main():
    
    root = Tk()
    app = Example(root)
    root.geometry("500x600+400+100")
    root.mainloop()
    
if __name__ == "__main__":
    main()