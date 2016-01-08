# Diary
每天一篇英语日记<br>
这是一个英语日记写作程序，可以作为英语学习<b>辅助</b>使用。

![UI](https://raw.github.com/lihui/100Words/master/resources/me.jpg)

##功能说明
1.自动创建 'C:\Users\Administrator\MyDiary\年\月\' 目录树及文件。<br>
2.以日为文件名创建txt文件，txt文件开头写入日期与时间。<br>
3.每篇日记要求字数100。<br>
4.查看以往日记点击File-Reflect。<br>
<b>5.查看以往日记不支持再编辑，点击保存会添加到当天内容。</b><br>
6.数据统计。<br>

##使用说明
1.点击Download ZIP下载文件。<br>
2.解压取出可执行文件（100 Words.exe）和字体文件（Purisa.ttf），其他可删除；<br>
3.双击安装字体文件。<br>
4.然后就可以打开程序了。<br>

##Rules
Rule 1: You must write no less than 100 words.<br>
Rule 2: You can only use one emoji in one day.<br>
Rule 3: You can not change the previous diary.<br>

##打包说明
1.根目录下的exe文件是用pyinstaller打包。<br>
2.Diary.spec为打包后生成的配置文件。<br>
3.代码中的音频调用使用了一个resource_path(relative_path)函数，在调用文件的地方使用这个函数包裹。<br>
  然后在.spec文件中指向具体的文件地址，打包后即可正常调用。<br>
4.详情见注释。

##待实现功能
1.图形界面；------------☑<br>
2.拼写检查；<br>
3.年底自动总结完成情况，包括每月完成量，生成折线图；<br>
4.添加表情；<br>
5.activity calendar。<br>
6.图标问题。<br>
7.反馈。<br>
