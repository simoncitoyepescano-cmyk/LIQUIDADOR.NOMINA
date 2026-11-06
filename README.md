# 🧾 Liquidador de Nómina - Colombia

## 📌 Descripción del proyecto

Sistema desarrollado en Python para liquidar la nómina mensual de un trabajador en Colombia, teniendo en cuenta conceptos como salario, auxilio de transporte, horas extra, recargos, seguridad social y prestaciones sociales.

El proyecto utiliza una arquitectura **Model - View**, una interfaz gráfica desarrollada con **Kivy** y pruebas unitarias mediante `unittest`.

## 🎯 Objetivo

Automatizar el cálculo del total devengado, las deducciones y el neto a pagar de un trabajador, garantizando la validación de los datos y la precisión de los resultados mediante pruebas unitarias.

## ⚙️ Funcionamiento

El sistema recibe como datos de entrada:

- Salario base mensual.
- Días trabajados.
- Horas extra diurnas, nocturnas y dominicales/festivas.
- Recargos nocturnos y dominicales/festivos.

Con esta información calcula automáticamente:

- Salario proporcional y auxilio de transporte.
- Horas extra y recargos.
- Aportes a salud y pensión.
- Total devengado, deducciones y neto a pagar.
- Provisiones de cesantías, intereses, prima y vacaciones.

## 🧮 Reglas laborales implementadas

| Concepto | Porcentaje |
|---|---:|
| Hora extra diurna | 25% |
| Hora extra nocturna | 75% |
| Hora extra dominical diurna | 100% |
| Hora extra dominical nocturna | 150% |
| Recargo nocturno | 35% |
| Recargo dominical/festivo | 75% |
| Salud y pensión | 4% cada uno |
| Cesantías y prima | 8,33% cada una |
| Intereses de cesantías | 12% anual |
| Vacaciones | 4,17% |

El auxilio de transporte se aplica según los requisitos legales. Los valores del SMMLV y del auxilio se configuran mediante constantes en `logica_nomina.py`.

## 🧪 Pruebas unitarias

Se desarrollaron **23 pruebas con unittest**, incluyendo:

- Pruebas de cálculos de nómina y prestaciones sociales.
- 4 casos de error: salario cero, salario negativo, horas extra negativas y días fuera del rango permitido.
- 3 casos extraordinarios: salario superior a 2 SMMLV, combinación de todos los recargos y horas extra, y cero días trabajados.

## 📂 Estructura del proyecto

```text
LIQUIDADOR.NOMINA-1/
│
├── README.md
├── app.py
│
└── src/
    ├── model/
    │   ├── __init__.py
    │   └── logica_nomina.py
    │
    ├── test/
    │   ├── __init__.py
    │   └── test_nomina.py
    │
    └── view/
        ├── __init__.py
        └── consola_nomina.py
```

- **Model:** contiene los cálculos y validaciones.
- **View:** contiene las interfaces de usuario.
- **Test:** contiene las pruebas unitarias.
- **app.py:** inicia la aplicación gráfica.

## 💻 Tecnologías utilizadas

- Python 3.13.
- Kivy (interfaz gráfica).
- unittest (pruebas unitarias).
- PostgreSQL (base de datos).
- Git y GitHub (control de versiones).

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd LIQUIDADOR.NOMINA-1
```

### 2. Crear el entorno virtual con Python 3.13

Verificar que Python 3.13 esté instalado:

```bash
py -3.13 --version
```

Crear el entorno virtual:

```bash
py -3.13 -m venv kivy_venv313
```

Activarlo en Windows:

```bash
kivy_venv313\Scripts\activate
```

### 3. Instalar las dependencias

```bash
python -m pip install --upgrade pip setuptools
python -m pip install "kivy[base]"
```

### 4. Ejecutar la aplicación gráfica

Desde la carpeta principal del proyecto:

```bash
python app.py
```

### 5. Ejecutar las pruebas unitarias

```bash
python -m unittest discover -s src/test
```

Si todas las pruebas funcionan correctamente, aparecerá:

```text
Ran 23 tests
OK
```

### 6. Desactivar el entorno virtual

```bash
deactivate
```

**Nota:** Cada vez que se quiera ejecutar el proyecto, se debe activar primero el entorno virtual `kivy_venv313`. Si se utilizan otras librerías externas, también deben instalarse dentro de este entorno.

## 🔮 Futuras implementaciones

- Actualización automática de los valores legales.
- Inclusión del Fondo de Solidaridad Pensional y retención en la fuente.
- Generación de desprendibles en PDF o Excel.
- Liquidación de varios trabajadores.
- Gestión de novedades laborales.

## 👥 Autores

**Desarrolladores:** David Ríos Arias y Juan José García.

**Editor:** Simón Yepes Cano.

## 📌 Conclusión

El proyecto automatiza la liquidación de nómina en Colombia mediante una aplicación gráfica que facilita la interacción con el usuario. Su arquitectura modular, validaciones y pruebas unitarias permiten organizar y verificar correctamente los cálculos realizados.
