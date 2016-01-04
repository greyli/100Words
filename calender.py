# -*- coding: utf-8 -*-
import os
import time
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, RIGHT, RAISED, Text, N, TOP, LEFT, X, W, E
from ttk import Button, Frame, Style, Entry

# color: 1e6823 #8cc665 #d6e685


class Example(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        
        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Activity Calender")
        
        style = Style()
        style.configure("TButton", padding=(0,5,0,5),
            font='serif 10', background='red')
        style.theme_use('clam')
            
        self.columnconfigure(0,pad=3)
        self.columnconfigure(1,pad=3)
        self.columnconfigure(2,pad=3)
        self.columnconfigure(3,pad=3)
        self.columnconfigure(4,pad=3)
        self.columnconfigure(5,pad=3)
        self.columnconfigure(6,pad=3)
        
        self.rowconfigure(0,pad=3)
        self.rowconfigure(1,pad=3)
        self.rowconfigure(2,pad=3)
        self.rowconfigure(3,pad=3)
        self.rowconfigure(4,pad=3)
        self.rowconfigure(5,pad=3)
  
        now = time.localtime()
        label = Label(self, text="%s/%s" % (now.tm_year, now.tm_mon), font='serif 20 ')
        label.grid(row=0, columnspan=4, sticky=W+E)
        
        b1 = Button(self, text="1")
        b1.grid(row=1, column=0)
        
        b2 = Button(self, text="2")
        b2.grid(row=1, column=1)
        
        b3 = Button(self, text="3")
        b3.grid(row=1, column=2)
        
        b4 = Button(self, text="4")
        b4.grid(row=1, column=3)
        
        b5 = Button(self, text="5")
        b5.grid(row=1, column=4)
        
        b6 = Button(self, text="6")
        b6.grid(row=1, column=5)
        
        b7 = Button(self, text="7")
        b7.grid(row=1, column=6)
        
        b8 = Button(self, text="8")
        b8.grid(row=2, column=0)
        
        b9 = Button(self, text="9")
        b9.grid(row=2, column=1)
        
        b10 = Button(self, text="10")
        b10.grid(row=2, column=2)
        
        b11 = Button(self, text="11")
        b11.grid(row=2, column=3)
        
        b12 = Button(self, text="12")
        b12.grid(row=2, column=4)
        
        b13 = Button(self, text="13")
        b13.grid(row=2, column=5)
        
        b14 = Button(self, text="14")
        b14.grid(row=2, column=6)
        
        b14 = Button(self, text="14")
        b14.grid(row=2, column=6)
        
        b14 = Button(self, text="14")
        b14.grid(row=2, column=6)
        
        b15 = Button(self, text="15")
        b15.grid(row=3, column=0)
        
        b16 = Button(self, text="16")
        b16.grid(row=3, column=1)
        
        b17 = Button(self, text="17")
        b17.grid(row=3, column=2)
        
        b18 = Button(self, text="18")
        b18.grid(row=3, column=3)
        
        b19 = Button(self, text="19")
        b19.grid(row=3, column=4)
        
        b20 = Button(self, text="20")
        b20.grid(row=3, column=5)
        
        b21 = Button(self, text="21")
        b21.grid(row=3, column=6)
        
        b22 = Button(self, text="22")
        b22.grid(row=4, column=0)
        
        b23 = Button(self, text="23")
        b23.grid(row=4, column=1)
        
        b24 = Button(self, text="24")
        b24.grid(row=4, column=2)
        
        b25 = Button(self, text="25")
        b25.grid(row=4, column=3)
        
        b26 = Button(self, text="26")
        b26.grid(row=4, column=4)
        
        b27 = Button(self, text="27")
        b27.grid(row=4, column=5)
        
        b28 = Button(self, text="28")
        b28.grid(row=4, column=6)
        
        b29 = Button(self, text="29")
        b29.grid(row=5, column=0)
        
        b30 = Button(self, text="30")
        b30.grid(row=5, column=1)
        
        b31 = Button(self, text="31")
        b31.grid(row=5, column=2)
        

        self.pack()
        
def main():
    
    root = Tk()
    app = Example(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()