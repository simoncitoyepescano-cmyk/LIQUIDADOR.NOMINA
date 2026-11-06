# -*- mode: python ; coding: utf-8 -*-
# Configuración de PyInstaller para generar Nominapp.exe (interfaz Kivy)
# Uso:  pyinstaller Nominapp.spec
import sys
from PyInstaller.utils.hooks import collect_submodules
from kivy.tools.packaging.pyinstaller_hooks import hookspath, runtime_hooks, kivy_modules

# Módulos internos de Kivy que usa la app (ventana, texto, imágenes, portapapeles y audio).
# Se escriben a mano para que Kivy NO intente abrir una ventana al compilar.
modulos_kivy = kivy_modules + collect_submodules("kivy.graphics") + [
    "kivy.core.window", "kivy.core.window.window_sdl2",
    "kivy.core.text", "kivy.core.text.text_sdl2",
    "kivy.core.image", "kivy.core.image.img_tex", "kivy.core.image.img_dds", "kivy.core.image.img_sdl2",
    "kivy.core.clipboard", "kivy.core.clipboard.clipboard_winctypes",
    "kivy.core.clipboard.clipboard_sdl2", "kivy.core.clipboard.clipboard_dummy",
    "kivy.core.audio", "kivy.core.audio.audio_sdl2",
]

# Librerías gráficas y de sonido que Kivy necesita en Windows (SDL2, GLEW, ANGLE)
dependencias_kivy = []
if sys.platform == "win32":
    from kivy_deps import sdl2, glew
    carpetas = sdl2.dep_bins + glew.dep_bins
    try:
        from kivy_deps import angle
        carpetas += angle.dep_bins
    except ImportError:
        pass
    dependencias_kivy = [Tree(p) for p in carpetas]

a = Analysis(
    ["lanzador_exe.py"],
    pathex=[".", "src"],
    datas=[
        ("click.mp3", "."),
        ("jazz.mp3", "."),
        ("exito.mp3", "."),
    ],
    hiddenimports=[
        "view.gui.app",
        "model.logica_nomina",
    ] + modulos_kivy,
    hookspath=hookspath(),
    runtime_hooks=runtime_hooks(),
    excludes=["tkinter"],
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *dependencias_kivy,
    name="Nominapp",
    console=False,   # Solo la ventana de Kivy, sin consola negra
    upx=False,
)
