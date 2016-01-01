# Diary
每天一篇英语日记<br>
这是一个英语日记写作程序，可以作为英语学习<b>辅助</b>使用。

##功能说明
1.自动创建 'C:\Users\Administrator\MyDiary\年\月\' 目录树及文件。<br>
2.以日为文件名创建txt文件，txt文件开头写入日期、字数。<br>
3.每篇日记要求字数100。<br>
4.查看以往日记点击File-Reflect。<br>
<b>5.查看以往日记不支持再编辑，点击保存会替换当天文件。</b>

##Rules
Rule 1: You must write no less than 100 words.<br>
Rule 2: You can only use one emoji in one day.<br>
Rule 3: You can only write one diary in one day.<br>

##打包说明
1.根目录下的exe文件是用pyinstaller打包。<br>
2.Diary.spec为打包后生成的配置文件。<br>
3.代码中的音频调用使用了一个resource_path(relative_path)函数，在调用文件的地方使用这个函数包裹。<br>
  然后在.spec文件中指向具体的文件地址，打包后即可正常调用。<br>
4.详情见注释。

##待实现功能
1.图形界面；------------☑<br>
2.拼写检查；<br>
3.年底和月底自动总结完成情况，包括篇数，字数，错字数，生成相应的折线图；<br>
4.查词；<br>
5.添加表情；<br>
6.activity calendar。<br>
