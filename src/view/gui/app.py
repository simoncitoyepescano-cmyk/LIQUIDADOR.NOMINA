# IMPORTACIONES DE KIVY
from kivy.app import App
from kivy.core.audio import SoundLoader
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
    sonido_click = SoundLoader.load("click.mp3") #FUNCIONALIDAD NUEVA
    sonido_lobby = SoundLoader.load("jazz.mp3")
    sonido_exito = SoundLoader.load("exito.mp3")
   
    def build(self):
        self.sonido_lobby.play()
        "----------------------------------------------------------------------------------------------------------------------------------"
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

        #tercer_lay
        tercer_lay = BoxLayout(orientation="horizontal")
        with tercer_lay.canvas.before:
            Color(0, 1, 1, 1)
            rect_tercer_lay = Rectangle(pos=tercer_lay.pos, size=tercer_lay.size)
        tercer_lay.bind(pos=lambda instance, value: setattr(rect_tercer_lay, "pos", value),size=lambda instance, value: setattr(rect_tercer_lay, "size", value))
        self.texto_nombre = TextInput(hint_text="Ingrese su usuario",multiline=False,halign="center")
        tercer_lay.add_widget(self.texto_nombre)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #cuarto_lay
        cuarto_lay = BoxLayout(orientation="horizontal")
        with cuarto_lay.canvas.before:
            Color(0, 0, 0, 0)
            rect_cuarto_lay = Rectangle(pos=cuarto_lay.pos, size=cuarto_lay.size)
        cuarto_lay.bind(pos=lambda instance, value: setattr(rect_cuarto_lay, "pos", value),size=lambda instance, value: setattr(rect_cuarto_lay, "size", value))
        salario_base = Label(text="Salario Base:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        salario_base.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        cuarto_lay.add_widget(salario_base)

        #quinto_lay
        quinto_lay = BoxLayout(orientation="horizontal")
        with quinto_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_quinto_lay = Rectangle(pos=quinto_lay.pos, size=quinto_lay.size)
        quinto_lay.bind(pos=lambda instance, value: setattr(rect_quinto_lay, "pos", value),size=lambda instance, value: setattr(rect_quinto_lay, "size", value))
        self.valor_salario_base = TextInput(hint_text="Ingrese su salario base",input_filter="int",multiline=False,halign="center")
        quinto_lay.add_widget(self.valor_salario_base)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #sexto_lay
        sexto_lay = BoxLayout(orientation="horizontal")
        with sexto_lay.canvas.before:
            Color(0, 0, 1, 1)
            rect_sexto_lay = Rectangle(pos=sexto_lay.pos, size=sexto_lay.size)
        sexto_lay.bind(pos=lambda instance, value: setattr(rect_sexto_lay, "pos", value),size=lambda instance, value: setattr(rect_sexto_lay, "size", value))
        dias_trabajados = Label(text="Dias Trabajados:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        dias_trabajados.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        sexto_lay.add_widget(dias_trabajados)

        #septimo_lay
        septimo_lay = BoxLayout(orientation="horizontal")
        with septimo_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_septimo_lay = Rectangle(pos=septimo_lay.pos, size=septimo_lay.size)
        septimo_lay.bind(pos=lambda instance, value: setattr(rect_septimo_lay, "pos", value),size=lambda instance, value: setattr(rect_septimo_lay, "size", value))
        self.valor_dias_trabajados = TextInput(hint_text="Ingrese los dias trabajados",input_filter="int",multiline=False,halign="center")
        septimo_lay.add_widget(self.valor_dias_trabajados)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #octavo_lay
        octavo_lay = BoxLayout(orientation="horizontal")
        with octavo_lay.canvas.before:
            Color(0, 0, 0, 0)
            rect_octavo_lay = Rectangle(pos=octavo_lay.pos, size=octavo_lay.size)
        octavo_lay.bind(pos=lambda instance, value: setattr(rect_octavo_lay, "pos", value),size=lambda instance, value: setattr(rect_octavo_lay, "size", value))
        horas_extra_diurnas = Label(text="Horas Extra Diurnas:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_extra_diurnas.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        octavo_lay.add_widget(horas_extra_diurnas)

        #noveno_lay
        noveno_lay = BoxLayout(orientation="horizontal")
        with noveno_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_noveno_lay = Rectangle(pos=noveno_lay.pos, size=noveno_lay.size)
        noveno_lay.bind(pos=lambda instance, value: setattr(rect_noveno_lay, "pos", value),size=lambda instance, value: setattr(rect_noveno_lay, "size", value))
        self.valor_horas_extra_diurnas = TextInput(hint_text="Ingrese las horas extra diurnas",input_filter="float",multiline=False,halign="center")
        noveno_lay.add_widget(self.valor_horas_extra_diurnas)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #decimo_lay
        decimo_lay = BoxLayout(orientation="horizontal")
        with decimo_lay.canvas.before:
            Color(0, 0, 1, 1)
            rect_decimo_lay = Rectangle(pos=decimo_lay.pos, size=decimo_lay.size)
        decimo_lay.bind(pos=lambda instance, value: setattr(rect_decimo_lay, "pos", value),size=lambda instance, value: setattr(rect_decimo_lay, "size", value))
        horas_extra_nocturnas = Label(text="Horas Extra Nocturnas:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_extra_nocturnas.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        decimo_lay.add_widget(horas_extra_nocturnas)

        #undecimo_lay
        undecimo_lay = BoxLayout(orientation="horizontal")
        with undecimo_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_undecimo_lay = Rectangle(pos=undecimo_lay.pos, size=undecimo_lay.size)
        undecimo_lay.bind(pos=lambda instance, value: setattr(rect_undecimo_lay, "pos", value),size=lambda instance, value: setattr(rect_undecimo_lay, "size", value))
        self.valor_horas_extra_nocturnas = TextInput(hint_text="Ingrese las horas extra nocturnas",input_filter="float",multiline=False,halign="center")
        undecimo_lay.add_widget(self.valor_horas_extra_nocturnas)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #duodecimo_lay
        duodecimo_lay = BoxLayout(orientation="horizontal")
        with duodecimo_lay.canvas.before:
            Color(0, 0, 0, 0)
            rect_duodecimo_lay = Rectangle(pos=duodecimo_lay.pos, size=duodecimo_lay.size)
        duodecimo_lay.bind(pos=lambda instance, value: setattr(rect_duodecimo_lay, "pos", value),size=lambda instance, value: setattr(rect_duodecimo_lay, "size", value))
        horas_extra_dominicales_diurnas = Label(text="Horas Extra Dominicales Diurnas:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_extra_dominicales_diurnas.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        duodecimo_lay.add_widget(horas_extra_dominicales_diurnas)

        #decimotercero_lay
        decimotercero_lay = BoxLayout(orientation="horizontal")
        with decimotercero_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_decimotercero_lay = Rectangle(pos=decimotercero_lay.pos, size=decimotercero_lay.size)
        decimotercero_lay.bind(pos=lambda instance, value: setattr(rect_decimotercero_lay, "pos", value),size=lambda instance, value: setattr(rect_decimotercero_lay, "size", value))
        self.valor_horas_extra_dominicales_diurnas = TextInput(hint_text="Ingrese las horas extra dominicales diurnas",input_filter="float",multiline=False,halign="center")
        decimotercero_lay.add_widget(self.valor_horas_extra_dominicales_diurnas)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #decimocuarto_lay
        decimocuarto_lay = BoxLayout(orientation="horizontal")
        with decimocuarto_lay.canvas.before:
            Color(0, 0, 1, 1)
            rect_decimocuarto_lay = Rectangle(pos=decimocuarto_lay.pos, size=decimocuarto_lay.size)
        decimocuarto_lay.bind(pos=lambda instance, value: setattr(rect_decimocuarto_lay, "pos", value),size=lambda instance, value: setattr(rect_decimocuarto_lay, "size", value))
        horas_extra_dominicales_nocturnas = Label(text="Horas Extra Dominicales Nocturnas:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_extra_dominicales_nocturnas.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        decimocuarto_lay.add_widget(horas_extra_dominicales_nocturnas)

        #decimoquinto_lay
        decimoquinto_lay = BoxLayout(orientation="horizontal")
        with decimoquinto_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_decimoquinto_lay = Rectangle(pos=decimoquinto_lay.pos, size=decimoquinto_lay.size)
        decimoquinto_lay.bind(pos=lambda instance, value: setattr(rect_decimoquinto_lay, "pos", value),size=lambda instance, value: setattr(rect_decimoquinto_lay, "size", value))
        self.valor_horas_extra_dominicales_nocturnas = TextInput(hint_text="Ingrese las horas extra dominicales nocturnas",input_filter="float",multiline=False,halign="center")
        decimoquinto_lay.add_widget(self.valor_horas_extra_dominicales_nocturnas)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #decimosexto_lay
        decimosexto_lay = BoxLayout(orientation="horizontal")
        with decimosexto_lay.canvas.before:
            Color(0, 0, 0, 0)
            rect_decimosexto_lay = Rectangle(pos=decimosexto_lay.pos, size=decimosexto_lay.size)
        decimosexto_lay.bind(pos=lambda instance, value: setattr(rect_decimosexto_lay, "pos", value),size=lambda instance, value: setattr(rect_decimosexto_lay, "size", value))
        horas_recargo_nocturno = Label(text="Horas Recargo Nocturno:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_recargo_nocturno.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        decimosexto_lay.add_widget(horas_recargo_nocturno)

        #decimoseptimo_lay
        decimoseptimo_lay = BoxLayout(orientation="horizontal")
        with decimoseptimo_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_decimoseptimo_lay = Rectangle(pos=decimoseptimo_lay.pos, size=decimoseptimo_lay.size)
        decimoseptimo_lay.bind(pos=lambda instance, value: setattr(rect_decimoseptimo_lay, "pos", value),size=lambda instance, value: setattr(rect_decimoseptimo_lay, "size", value))
        self.valor_horas_recargo_nocturno = TextInput(hint_text="Ingrese las horas de recargo nocturno",input_filter="float",multiline=False,halign="center")
        decimoseptimo_lay.add_widget(self.valor_horas_recargo_nocturno)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #decimooctavo_lay
        decimooctavo_lay = BoxLayout(orientation="horizontal")
        with decimooctavo_lay.canvas.before:
            Color(0, 0, 1, 1)
            rect_decimooctavo_lay = Rectangle(pos=decimooctavo_lay.pos, size=decimooctavo_lay.size)
        decimooctavo_lay.bind(pos=lambda instance, value: setattr(rect_decimooctavo_lay, "pos", value),size=lambda instance, value: setattr(rect_decimooctavo_lay, "size", value))
        horas_recargo_dominical_festivo = Label(text="Horas Recargo Dominical/Festivo:",color=(1, 1, 1, 1),font_size=20,bold=True,halign="center",valign="middle")
        horas_recargo_dominical_festivo.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        decimooctavo_lay.add_widget(horas_recargo_dominical_festivo)

        #decimonoveno_lay
        decimonoveno_lay = BoxLayout(orientation="horizontal")
        with decimonoveno_lay.canvas.before:
            Color(1, 1, 1, 1)
            rect_decimonoveno_lay = Rectangle(pos=decimonoveno_lay.pos, size=decimonoveno_lay.size)
        decimonoveno_lay.bind(pos=lambda instance, value: setattr(rect_decimonoveno_lay, "pos", value),size=lambda instance, value: setattr(rect_decimonoveno_lay, "size", value))
        self.valor_horas_recargo_dominical_festivo = TextInput(hint_text="Ingrese las horas de recargo dominical/festivo",input_filter="float",multiline=False,halign="center")
        decimonoveno_lay.add_widget(self.valor_horas_recargo_dominical_festivo)

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

        #Contenedor para octavo_lay y noveno_lay
        contenedores_8_9 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_8_9.add_widget(octavo_lay)
        contenedores_8_9.add_widget(noveno_lay)

        #Contenedor para decimo_lay y undecimo_lay
        contenedores_10_11 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_10_11.add_widget(decimo_lay)
        contenedores_10_11.add_widget(undecimo_lay)

        #Contenedor para duodecimo_lay y decimotercero_lay
        contenedores_12_13 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_12_13.add_widget(duodecimo_lay)
        contenedores_12_13.add_widget(decimotercero_lay)

        #Contenedor para decimocuarto_lay y decimoquinto_lay
        contenedores_14_15 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_14_15.add_widget(decimocuarto_lay)
        contenedores_14_15.add_widget(decimoquinto_lay)

        #Contenedor para decimosexto_lay y decimoseptimo_lay
        contenedores_16_17 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_16_17.add_widget(decimosexto_lay)
        contenedores_16_17.add_widget(decimoseptimo_lay)

        #Contenedor para decimooctavo_lay y decimonoveno_lay
        contenedores_18_19 = BoxLayout(orientation="horizontal",spacing=0,padding=0)
        contenedores_18_19.add_widget(decimooctavo_lay)
        contenedores_18_19.add_widget(decimonoveno_lay)

        "----------------------------------------------------------------------------------------------------------------------------------"

        #Tamaños layout
        layout.size_hint = (1 , 1)
        segundo_lay.size_hint = (0.5, 1)
        tercer_lay.size_hint = (0.5, 1)
        cuarto_lay.size_hint = (0.5, 1)
        quinto_lay.size_hint = (0.5, 1)
        sexto_lay.size_hint = (0.5, 1)
        septimo_lay.size_hint = (0.5, 1)
        octavo_lay.size_hint = (0.5, 1)
        noveno_lay.size_hint = (0.5, 1)
        decimo_lay.size_hint = (0.5, 1)
        undecimo_lay.size_hint = (0.5, 1)
        duodecimo_lay.size_hint = (0.5, 1)
        decimotercero_lay.size_hint = (0.5, 1)
        decimocuarto_lay.size_hint = (0.5, 1)
        decimoquinto_lay.size_hint = (0.5, 1)
        decimosexto_lay.size_hint = (0.5, 1)
        decimoseptimo_lay.size_hint = (0.5, 1)
        decimooctavo_lay.size_hint = (0.5, 1)
        decimonoveno_lay.size_hint = (0.5, 1)

        #Tamaños contenedores
        contenedores_2_3.size_hint = (1, 0.5)
        contenedores_4_5.size_hint = (1, 0.5)
        contenedores_6_7.size_hint = (1, 0.5)
        contenedores_8_9.size_hint = (1, 0.5)
        contenedores_10_11.size_hint = (1, 0.5)
        contenedores_12_13.size_hint = (1, 0.5)
        contenedores_14_15.size_hint = (1, 0.5)
        contenedores_16_17.size_hint = (1, 0.5)
        contenedores_18_19.size_hint = (1, 0.5)

        #Meter contenedores a layout
        layout.add_widget(contenedores_2_3)
        layout.add_widget(contenedores_4_5)
        layout.add_widget(contenedores_6_7)
        layout.add_widget(contenedores_8_9)
        layout.add_widget(contenedores_10_11)
        layout.add_widget(contenedores_12_13)
        layout.add_widget(contenedores_14_15)
        layout.add_widget(contenedores_16_17)
        layout.add_widget(contenedores_18_19)

        #Boton Para Calcular Nomina
        boton_calcular = Button(text="CALCULAR NÓMINA",font_size=20,bold=True)
        boton_calcular.bind(on_press=self.calcular_nomina)

        #Meter boton a layout
        layout.add_widget(boton_calcular)

        return layout

    def calcular_nomina(self, boton):    
        try:
            nombre = (self.texto_nombre.text)
            if nombre.strip() == "":
                raise ValueError("Por favor ingrese el nombre del trabajador")
            
            salario_base = float(self.valor_salario_base.text)
            if salario_base <= 0:
                raise logica_nomina.SalarioInvalido()

            dias_trabajados = int(self.valor_dias_trabajados.text or 0)
            if dias_trabajados < 0 or dias_trabajados > 30:
                raise logica_nomina.DiasInvalidos()
            
            horas_extra_diurnas = float(self.valor_horas_extra_diurnas.text or 0)
            if horas_extra_diurnas < 0:
                raise logica_nomina.HorasInvalidas("Horas extra diurnas")

            horas_extra_nocturnas = float(self.valor_horas_extra_nocturnas.text or 0)
            if horas_extra_nocturnas < 0:
                raise logica_nomina.HorasInvalidas("Horas extra nocturnas")

            horas_extra_dominicales_diurnas = float(self.valor_horas_extra_dominicales_diurnas.text or 0)
            if horas_extra_dominicales_diurnas < 0:
                raise logica_nomina.HorasInvalidas("Horas extra dominicales diurnas")

            horas_extra_dominicales_nocturnas = float(self.valor_horas_extra_dominicales_nocturnas.text or 0)
            if horas_extra_dominicales_nocturnas < 0:
                raise logica_nomina.HorasInvalidas("Horas extra dominicales nocturnas")

            horas_recargo_nocturno = float(self.valor_horas_recargo_nocturno.text or 0)
            if horas_recargo_nocturno < 0:
                raise logica_nomina.HorasInvalidas("Horas de recargo nocturno")

            horas_recargo_dominical_festivo = float(self.valor_horas_recargo_dominical_festivo.text or 0)
            if horas_recargo_dominical_festivo < 0:
                raise logica_nomina.HorasInvalidas("Horas de recargo dominical/festivo")
    

            nomina = liquidar_nomina(salario_base,dias_trabajados,horas_extra_diurnas,horas_extra_nocturnas,horas_extra_dominicales_diurnas,horas_extra_dominicales_nocturnas,horas_recargo_nocturno,horas_recargo_dominical_festivo)

            #Mostrar resultado ordenado
            texto_resultados = ""
            for concepto, valor in nomina.items():

                if isinstance(valor, dict):
                    texto_resultados += f"\n{concepto}:\n"
                    for sub_concepto, sub_valor in valor.items():
                        sub_valor = str(sub_valor).replace("$", "").replace(",", "").strip()
                        texto_resultados += f"{sub_concepto} = ${float(sub_valor):,.2f}\n"

                else:
                    valor = str(valor).replace("$", "").replace(",", "").strip()
                    texto_resultados += f"{concepto} = ${float(valor):,.2f}\n"

            resultados = Label(text=texto_resultados,halign="left",valign="top")

            ventana = Popup(title="RESULTADO DE LA NÓMINA",content=resultados,size_hint=(0.8, 0.8))
            ventana.open()

            self.sonido_exito.play()

            print(nomina)
           
        except logica_nomina.SalarioInvalido:
            self.sonido_click.play()
            mensaje = "El salario debe ser mayor que cero."
            #Ventana si surge error
            ventana_error = Popup(title="ERROR EN LOS DATOS",content=Label(text=mensaje),size_hint=(0.7, 0.4))
            ventana_error.open()

        except logica_nomina.DiasInvalidos:
            self.sonido_click.play()
            mensaje = "Los días trabajados deben estar entre 0 y 30."
            #Ventana si surge error
            ventana_error = Popup(title="ERROR EN LOS DATOS",content=Label(text=mensaje),size_hint=(0.7, 0.4))
            ventana_error.open()

        except logica_nomina.HorasInvalidas as error:
            self.sonido_click.play()
            mensaje = str(error)
            #Ventana si surge error
            ventana_error = Popup(title="ERROR EN LOS DATOS",content=Label(text=mensaje),size_hint=(0.7, 0.4))
            ventana_error.open()

        except ValueError as error:
            self.sonido_click.play()
            mensaje = str(error)
            #Ventana si surge error
            ventana_error = Popup(title="ERROR EN LOS DATOS",content=Label(text=mensaje),size_hint=(0.7, 0.4))
            ventana_error.open()

Nominapp().run()
