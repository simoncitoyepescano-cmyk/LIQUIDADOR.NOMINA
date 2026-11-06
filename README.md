# 🧾 Liquidador de Nómina - Colombia

## 📌 Descripción del proyecto

Sistema desarrollado en Python para liquidar la nómina mensual de un trabajador en Colombia, considerando conceptos como salario, auxilio de transporte, horas extra, recargos, seguridad social y prestaciones sociales.

El proyecto utiliza una arquitectura modular basada en el patrón **Model - View** y pruebas unitarias mediante `unittest`.

## 🎯 Objetivo

Automatizar el cálculo del total devengado, las deducciones y el neto a pagar de un trabajador, validando los datos ingresados y comprobando los resultados mediante pruebas unitarias.

## ⚙️ Funcionamiento

El sistema recibe:

- Salario base mensual.
- Días trabajados.
- Horas extra diurnas, nocturnas y dominicales/festivas.
- Recargos nocturnos y dominicales/festivos.

Calcula automáticamente:

- Salario proporcional y auxilio de transporte.
- Horas extra y recargos.
- Aportes a salud y pensión.
- Total devengado, deducciones y neto a pagar.
- Provisiones de cesantías, intereses, prima y vacaciones.

## 🧮 Porcentajes y parámetros implementados

Los siguientes porcentajes corresponden a los parámetros utilizados actualmente en la lógica del proyecto:

| Concepto                      | Porcentaje     |
| ----------------------------- | -------------- |
| Hora extra diurna             | 25%            |
| Hora extra nocturna           | 75%            |
| Hora extra dominical diurna   | 100%           |
| Hora extra dominical nocturna | 150%           |
| Recargo nocturno              | 35%            |
| Recargo dominical/festivo     | 75%            |
| Salud y pensión               | 4% cada uno    |
| Cesantías y prima             | 8,33% cada una |
| Intereses de cesantías        | 12% anual      |
| Vacaciones                    | 4,17%          |

El auxilio de transporte se calcula según los requisitos establecidos en la lógica del programa. Los valores del SMMLV, auxilio de transporte y horas mensuales se configuran mediante constantes en `logica_nomina.py`.

**Nota:** Los porcentajes y parámetros deben revisarse y actualizarse de acuerdo con la normativa laboral colombiana vigente y el periodo que se desea liquidar. Los valores presentados describen la implementación actual del proyecto y no constituyen una certificación de cumplimiento legal.

## 🧪 Pruebas unitarias

Se desarrollaron **23 pruebas con unittest**, incluyendo:

- Cálculos de nómina y prestaciones sociales.
- 4 casos de error: salario cero, salario negativo, horas extra negativas y días fuera del rango permitido.
- 3 casos extraordinarios: salario superior a 2 SMMLV, combinación de todos los recargos y horas extra, y cero días trabajados.

## 📂 Estructura del proyecto

```text
LIQUIDADOR.NOMINA/
│
├── README.md
│
├── src/
│   ├── model/
│   │   ├── __init__.py
│   │   └── logica_nomina.py
│   │
│   └── view/
│       ├── __init__.py
│       └── consola_nomina.py
│
└── test/
    ├── __init__.py
    └── test_nomina.py
```

**Componentes principales:**

- **Model:** contiene los cálculos, validaciones y excepciones.
- **View:** contiene la interfaz de consola para interactuar con el sistema.
- **Test:** contiene las pruebas unitarias.
- **README:** documenta el proyecto y sus instrucciones de ejecución.

## 💻 Tecnologías utilizadas

- Python 3.13.
- `unittest` para pruebas unitarias.
- Git y GitHub para control de versiones.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/simoncitoyepescano-cmyk/LIQUIDADOR.NOMINA.git
```

Ingresar a la carpeta:

```bash
cd LIQUIDADOR.NOMINA
```

### 2. Configurar Python 3.13

Verificar que Python 3.13 esté instalado:

```bash
py -3.13 --version
```

Crear el entorno virtual:

```bash
py -3.13 -m venv venv
```

Activarlo en Windows:

```powershell
venv\Scripts\activate
```

### 3. Ejecutar las pruebas unitarias

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python -m unittest discover -s test -t .
```

Este comando busca las pruebas dentro de la carpeta `test` y utiliza la raíz del proyecto como directorio principal de importación.

Si todas las pruebas funcionan correctamente, aparecerá un resultado similar a:

```text
Ran 23 tests

OK
```

### 4. Ejecutar la aplicación de consola

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python -m src.view.consola_nomina
```

El programa solicitará el nombre del trabajador, salario base y días trabajados. Posteriormente permitirá seleccionar entre una liquidación básica o una liquidación completa con horas extra y recargos.

### 5. Desactivar el entorno virtual

Al finalizar, ejecutar:

```bash
deactivate
```

**Nota:** El proyecto actualmente cuenta con una interfaz de consola. No se incluye una interfaz gráfica (GUI) en esta versión.

## 🔮 Futuras implementaciones

- Desarrollo de una interfaz gráfica.
- Generación de desprendibles de nómina en PDF o Excel.
- Liquidación simultánea de varios trabajadores.
- Inclusión del Fondo de Solidaridad Pensional y retención en la fuente.
- Gestión de novedades laborales.

## 👥 Autores

**Desarrolladores:** David Ríos Arias y Juan José García.

**Editor:** Simón Yepes Cano.

## 📌 Conclusión

El proyecto permite automatizar la liquidación de nómina de un trabajador en Colombia mediante una estructura modular que facilita el mantenimiento y la comprobación de los resultados.

Las validaciones y pruebas unitarias permiten verificar los cálculos y controlar el comportamiento del sistema ante datos inválidos y situaciones extraordinarias.
