# -*- mode: python -*-

block_cipher = None


a = Analysis(['GUI.py'],
             pathex=['C:\\Users\\Administrator\\projects\\Diary'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('resources/complete.wav',r'C:\Users\Administrator\projects\Diary\resources\complete.wav','music'),
          ('resources/fail.wav',r'C:\Users\Administrator\projects\Diary\resources\fail.wav','music'),
          ('resources/smile.png',r'C:\Users\Administrator\projects\Diary\resources\smile.png','music'),
          ('resources/me.jpg',r'C:\Users\Administrator\projects\Diary\resources\me.jpg','music'),],
          name='100Words',
          icon='diary.ico',
          debug=False,
          strip=None,
          upx=True,
          console=False )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='100Words')
