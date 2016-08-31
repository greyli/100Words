# -*- mode: python -*-

block_cipher = None


a = Analysis(['100Words.py'],
             pathex=['C:\\Users\\Administrator\\Projects\\100Words'],
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
          [('resources/complete.wav', r'D:\Projects\100Words\resources\complete.wav','music'),
          ('resources/smile.png', r'D:\Projects\100Words\resources\smile.png','music'),
          ('resources/me.jpg', r'D:\Projects\100Words\resources\me.jpg','music'),
          ('resources/save.png', r'D:\Projects\100Words\resources\save.png','music'),
          ('resources/clock.png', r'D:\Projects\100Words\resources\clock.png','music'),
          ('resources/find.png', r'D:\Projects\100Words\resources\find.png','music')],
          name='100Words',
          icon='icon.ico',
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
