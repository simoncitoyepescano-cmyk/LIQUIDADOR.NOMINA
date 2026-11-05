# IMPORTACIONES DE KIVY
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

import sys

sys.path.append("src")

# Lógica de la nómina
from model import logica_nomina
from model.logica_nomina import liquidar_nomina

class Nominapp(App):
    def build(self):
        #Layout
        layout = BoxLayout(orientation="vertical")
        with layout.canvas.before:
            Color(0, 0, 0, 0)
            rect = Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda instance, value: setattr(rect, "pos", value),size=lambda instance, value: setattr(rect, "size", value))
        titulo = Label(text="NOMINAPP",color=(1, 1, 1, 1),font_size=30,bold=True)
        layout.add_widget(titulo)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #segundo_lay
        segundo_lay = BoxLayout(orientation="horizontal")
        with segundo_lay.canvas.before:
            Color(0, 0, 1, 1)
            rect_segundo_lay = Rectangle(pos=segundo_lay.pos, size=segundo_lay.size)
        segundo_lay.bind(pos=lambda instance, value: setattr(rect_segundo_lay, "pos", value),size=lambda instance, value: setattr(rect_segundo_lay, "size", value))
        nombre = Label(text="Nombre:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        nombre.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        segundo_lay.add_widget(nombre)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #tercer_lay
        tercer_lay = BoxLayout(orientation="horizontal")
        with tercer_lay.canvas.before:
            Color(0, 1, 1, 1)
            rect_tercer_lay = Rectangle(pos=tercer_lay.pos, size=tercer_lay.size)
        tercer_lay.bind(pos=lambda instance, value: setattr(rect_tercer_lay, "pos", value),size=lambda instance, value: setattr(rect_tercer_lay, "size", value))
        texto_nombre = TextInput(hint_text="Ingrese su usuario",multiline=False,halign="center")
        tercer_lay.add_widget(texto_nombre)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #cuarto_lay
        cuarto_lay = BoxLayout(orientation="horizontal")
        with cuarto_lay.canvas.before:
            Color(0, 1, 1, 1)
            rect_cuarto_lay = Rectangle(pos=cuarto_lay.pos, size=cuarto_lay.size)
        cuarto_lay.bind(pos=lambda instance, value: setattr(rect_cuarto_lay, "pos", value),size=lambda instance, value: setattr(rect_cuarto_lay, "size", value))
        salario_base = Label(text="Salario Base:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        salario_base.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        cuarto_lay.add_widget(salario_base)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #quinto_lay
        quinto_lay = BoxLayout(orientation="horizontal")
        with quinto_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_quinto_lay = Rectangle(pos=quinto_lay.pos, size=quinto_lay.size)
        quinto_lay.bind(pos=lambda instance, value: setattr(rect_quinto_lay, "pos", value),size=lambda instance, value: setattr(rect_quinto_lay, "size", value))
        valor_salario_base = TextInput(hint_text="Ingrese su salario base",input_filter="int",multiline=False,halign="center")
        quinto_lay.add_widget(valor_salario_base)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #sexto_lay
        sexto_lay = BoxLayout(orientation="horizontal")
        with sexto_lay.canvas.before:
            Color(0, 1, 0, 1)
            rect_sexto_lay = Rectangle(pos=sexto_lay.pos, size=sexto_lay.size)
        sexto_lay.bind(pos=lambda instance, value: setattr(rect_sexto_lay, "pos", value),size=lambda instance, value: setattr(rect_sexto_lay, "size", value))
        dias_trabajados = Label(text="Dias Trabajados:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        dias_trabajados.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        sexto_lay.add_widget(dias_trabajados)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #septimo_lay
        septimo_lay = BoxLayout(orientation="horizontal")
        with septimo_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_septimo_lay = Rectangle(pos=septimo_lay.pos, size=septimo_lay.size)
        septimo_lay.bind(pos=lambda instance, value: setattr(rect_septimo_lay, "pos", value),size=lambda instance, value: setattr(rect_septimo_lay, "size", value))
        valor_dias_trabajados = TextInput(hint_text="Ingrese los dias trabajados",input_filter="int",multiline=False,halign="center")
        septimo_lay.add_widget(valor_dias_trabajados)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #Contenedor para segundo_lay y tercer_lay
        contenedores_2_3 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_2_3.add_widget(segundo_lay)
        contenedores_2_3.add_widget(tercer_lay)

        #Contenedor para cuarto_lay y quinto_lay
        contenedores_4_5 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_4_5.add_widget(cuarto_lay)
        contenedores_4_5.add_widget(quinto_lay)

        #Contenedor para sexto_lay y septimo_lay
        contenedores_6_7 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_6_7.add_widget(sexto_lay)
        contenedores_6_7.add_widget(septimo_lay)

        #Tamaños
        layout.size_hint = (1 , 1)
        segundo_lay.size_hint = (0.5, 1)
        tercer_lay.size_hint = (0.5, 1)
        cuarto_lay.size_hint = (0.5, 1)
        quinto_lay.size_hint = (0.5, 1)
        sexto_lay.size_hint = (0.5, 1)
        septimo_lay.size_hint = (0.5, 1)
        contenedores_2_3.size_hint = (1, 0.5)
        contenedores_4_5.size_hint = (1, 0.5)
        contenedores_6_7.size_hint = (1, 0.5)

        #Meter contenedores a layout
        layout.add_widget(contenedores_2_3)
        layout.add_widget(contenedores_4_5)
        layout.add_widget(contenedores_6_7)


        return layout


Nominapp().run()
