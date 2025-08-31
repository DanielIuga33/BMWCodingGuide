# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Files\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('data\\\\codes.json', 'data'), ('data\\\\flag_ro.png', 'data'), ('data\\\\flag_en.png', 'data'), ('data\\\\flag_en.png', 'data'), ('data\\\\BMW_welcome.png', 'data'), ('data\\\\icon_bmw.ico', 'data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BMW_Coding_Guide',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['data\\icon_bmw.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BMW_Coding_Guide',
)
