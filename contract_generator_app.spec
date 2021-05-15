# -*- mode: python ; coding: utf-8 -*-

# ------------ Modify here! -------------
app_name = "Contract.app"
project_dir = "/Users/yhh/github-repo/contract-generator-pyside2"
templates_dir = "/Users/yhh/github-repo/contract-generator-pyside2/templates"
font_file_path = "/System/Library/Fonts/Helvetica.ttc"
# ---------------------------------------

block_cipher = None

# include files
font_path = (font_file_path, "font")

a = Analysis(['contract_generator.py'],
             pathex=[project_dir],
             binaries=[],
             datas=[font_path],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# include the whole directory
a.datas += Tree(templates_dir, prefix="templates")

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='contract_generator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name=app_name,
             icon=None,
             bundle_identifier=None)
