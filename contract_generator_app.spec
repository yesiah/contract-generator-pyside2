# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

# include files
cairocffi_version_path = ("/opt/miniconda3/envs/contract_generator_pyside2/lib/python3.6/site-packages/cairocffi/VERSION", "cairocffi")
#weasyprint_version_path = ("/opt/miniconda3/envs/contract_generator_pyside2/lib/python3.6/site-packages/weasyprint/VERSION", "weasyprint")
pyphen_dir = ("/opt/miniconda3/envs/contract_generator_pyside2/lib/python3.6/site-packages/pyphen/dictionaries", "pyphen/dictionaries")
cairosvg_version_path = ("/opt/miniconda3/envs/contract_generator_pyside2/lib/python3.6/site-packages/cairosvg/VERSION", "cairosvg")
font_path = ("/System/Library/Fonts/Helvetica.ttc", "font")

a = Analysis(['contract_generator.py'],
             pathex=['/Users/yhh/github-repo/contract-generator-pyside2'],
             binaries=[],
             datas=[cairocffi_version_path,
                    #weasyprint_version_path,
                    pyphen_dir,
                    cairosvg_version_path,
                    font_path],
             #hiddenimports=["weasyprint"],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# include the whole directory
a.datas += Tree("/Users/yhh/github-repo/contract-generator-pyside2/templates", prefix="templates")

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
             name='contract_generator.app',
             icon=None,
             bundle_identifier=None)
