"""
Punto de entrada para el ejecutable (.exe) de NOMINAPP (interfaz Kivy).

La aplicación carga los sonidos con rutas relativas ("click.mp3", "jazz.mp3",
"exito.mp3") y busca el código en la carpeta "src". Dentro del .exe esos
archivos se desempaquetan en una carpeta temporal, así que este lanzador se
ubica en esa carpeta antes de abrir la aplicación.
"""
import os
import sys

if getattr(sys, "frozen", False):
    # Ejecutándose como .exe: los archivos empaquetados están en sys._MEIPASS
    os.chdir(sys._MEIPASS)
    # Sin consola, Kivy no debe intentar escribir el log en pantalla
    os.environ.setdefault("KIVY_NO_CONSOLELOG", "1")
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("KIVY_NO_ARGS", "1")
sys.path.insert(0, os.path.abspath("src"))

# Al importar este módulo se abre la aplicación (Nominapp().run() está al final de app.py)
import view.gui.app  # noqa: E402,F401
