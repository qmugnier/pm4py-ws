# -*- mode: python -*-

import sys
sys.setrecursionlimit(5000)

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\berti\\pm4py-ws'],
             binaries=[],
             datas=[('event_logs.db','.'),('users.db','.'),('logs/','logs/')],
             hiddenimports=["sklearn.neighbors.typedefs", "sklearn.utils._cython_blas", "scipy._lib.messagestream", "sklearn.tree", "sklearn.neighbors.quad_tree", "sklearn.tree._utils"],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
