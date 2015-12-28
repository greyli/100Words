# _*_ coding:utf-8 _*_ 
import time
import os
import sys

import pygame

date = time.localtime()
ls = "\n" * 2 # linesep
os.chdir = (r'D:\Documents') # change dir

def main():
    # if folder isn't exist. 
    # create folder tree 'D:\Documents\MyDiary\year\month\'
    filename = r'D:\Documents\MyDiary'
    year = r'D:\Documents\MyDiary\%s' %  (str(date.tm_year))
    month = r'D:\Documents\MyDiary\%s\%s' %  (str(date.tm_year),str(date.tm_mon))
    
    if not os.path.exists(filename):
        os.mkdir(filename)
    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(month):
        os.mkdir(month)
        
    write()
    
def resource_path(relative_path):
    """
    定义一个读取相对路径的函数
    引用文件用如下格式：resource_path('resources/complete.wav')
    然后在生成的.spec文件exe = EXE()中加入下面这行：
    [('resources/complete.wav',r'C:\Users\Administrator\resources\complete.wav','music'),],
    这样打包后文件会被正确引用
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

    
def write():
    
    today_diary = []
  
    part1 = raw_input('Good>>>')
    print
    part2 = raw_input('Bad>>>')
    print
    part3 = raw_input('Other>>>') + ls
    print
    
    length = len(part1.split())+len(part2.split())+len(part3.split())
    
    while length < 100:
        print "\aOnly %d words!" % length
        print
        add_content = raw_input("Add>>>")
        print
        length += len(add_content.split())
        part3 += (add_content+ls)
    # write date    
    today = time.asctime()
    
    
    content = today + ls + part1 + ls + part2 + ls + part3
    # create file 'D:\Documents\MyDiary\year\month\day.txt'
    filename = r"D:\Documents\MyDiary\%s\%s\%s.txt" % (str(date.tm_year),
                                        str(date.tm_mon),str(date.tm_mday))
    f = open(filename,'w')
    f.write(content)
    f.close()
    
    pygame.mixer.init()  
    pygame.mixer.music.load(resource_path('resources/complete.wav'))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:  
        continue
    print
    print "MISSION COMPLETE!"
    print
    print "See you tomorrow =^_^="
    print
    raw_input("Enter to exit >>>")
    
if __name__ == "__main__":
    print "What happened today?"
    print
    main()