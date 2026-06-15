Trabajo Práctico Integrador - Programación 1

Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

Integrantes

- Tomás Aguirre
- Morena Lis Sonnleitner

Comisión

Programación 1 - Tecnicatura Universitaria en Programación - UTN

---

Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de países realizado en Python.

La aplicación permite administrar información de distintos países mediante el uso de estructuras de datos, funciones, archivos CSV, validaciones, filtros, ordenamientos y estadísticas.

Los datos son cargados desde un archivo CSV y luego procesados por el programa para que el usuario pueda realizar diferentes operaciones desde un menú interactivo en consola.

El objetivo principal fue aplicar los conceptos aprendidos durante la materia Programación 1, utilizando programación estructurada y modular.

---

Objetivos

- Aplicar listas y diccionarios.
- Utilizar funciones para modularizar el código.
- Implementar estructuras condicionales y repetitivas.
- Leer y escribir archivos CSV.
- Realizar búsquedas y filtros.
- Implementar ordenamientos.
- Generar estadísticas a partir de los datos almacenados.
- Validar entradas y manejar errores.

---

Tecnologías Utilizadas

- Python 3.x
- Librería csv
- Visual Studio Code

---

Estructura del Proyecto

Proyecto_TPI/
│
├── tp.py
├── paises.csv
├── README.md
├── Documentacion.pdf
└── Video_Demostracion

---

Estructuras de Datos Utilizadas

Lista

Todos los países se almacenan dentro de una lista.

Ejemplo:

paises = []

Esta estructura permite recorrer fácilmente todos los registros para realizar búsquedas, filtros, ordenamientos y estadísticas.

---

Diccionarios

Cada país se almacena mediante un diccionario.

Ejemplo:

{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}

Los diccionarios permiten acceder rápidamente a cada dato mediante una clave.

---

Funcionamiento General

Al iniciar el programa se realiza la lectura del archivo CSV mediante la función cargar_paises().

Posteriormente se muestran las opciones del menú principal para que el usuario pueda interactuar con el sistema.

Durante la ejecución los datos permanecen almacenados en memoria dentro de una lista de diccionarios.

Cuando el usuario decide finalizar el programa, los cambios realizados son guardados nuevamente en el archivo CSV.

---

Funcionalidades Implementadas

1. Agregar País

Permite incorporar un nuevo país ingresando:

- Nombre
- Población
- Superficie
- Continente

Se validan campos vacíos y tipos de datos incorrectos.

---

2. Actualizar País

Permite modificar:

- Población
- Superficie

de un país ya existente.

---

3. Buscar País

Permite localizar países por nombre.

La búsqueda admite coincidencias parciales o exactas.

---

4. Filtrar por Continente

Muestra únicamente los países pertenecientes al continente seleccionado.

---

5. Filtrar por Población

Permite mostrar países dentro de un rango determinado de población.

---

6. Filtrar por Superficie

Permite mostrar países dentro de un rango determinado de superficie.

---

7. Ordenamiento

Los países pueden ordenarse por:

- Nombre
- Población
- Superficie

en forma ascendente o descendente.

---

8. Estadísticas

El sistema genera información estadística:

- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.

---

Manejo de Archivos CSV

Los datos son almacenados en un archivo llamado:

paises.csv

Al iniciar el programa:

- Se abre el archivo en modo lectura.
- Se convierten las filas en diccionarios.
- Se almacenan en una lista.

Al finalizar:

- Se guardan los cambios realizados.
- Se actualiza automáticamente el archivo CSV.

---

Validaciones Implementadas

Durante el desarrollo se incorporaron controles para evitar errores:

- Campos vacíos.
- Ingreso de texto donde se esperan números.
- Países inexistentes.
- Errores de lectura del CSV.
- Opciones inválidas del menú.

Estas validaciones permiten que el sistema continúe funcionando sin interrumpirse.

---

Decisiones Técnicas

Se eligió Python por ser un lenguaje claro, simple y adecuado para aplicaciones de consola.

El programa fue desarrollado utilizando una estructura modular basada en funciones.

Cada función posee una única responsabilidad, lo que mejora la organización del código y facilita futuras modificaciones.

---

Dificultades Encontradas

Durante el desarrollo surgieron distintas dificultades.

Una de las principales fue la lectura correcta de los datos almacenados en el archivo CSV y la conversión de valores numéricos.

También se presentaron inconvenientes relacionados con la validación de datos ingresados por el usuario.

Estas situaciones fueron resueltas mediante el uso de validaciones, estructuras condicionales y bloques try-except.

Además fue necesario reorganizar el código en funciones independientes para mejorar la legibilidad y el mantenimiento del sistema.

---

Conclusiones

Este proyecto permitió integrar y aplicar los conceptos fundamentales desarrollados durante la materia Programación 1.

A través de la implementación de listas, diccionarios, funciones, estructuras condicionales, ciclos, archivos CSV y estadísticas, se logró desarrollar una aplicación funcional capaz de gestionar información de países de manera eficiente.

La experiencia también permitió reforzar habilidades relacionadas con la organización de código, validación de datos, resolución de problemas y trabajo en equipo.

---

Bibliografía

- https://docs.python.org/es/3/
- https://www.w3schools.com/python/
- https://www.programiz.com/python-programming

---

Enlaces

Repositorio GitHub

(https://github.com/lisslilies/TPI_Programacion.git)

Video Demostración

(https://drive.google.com/file/d/1cZ4XJ0ZwszvjW7iYcePuLaxhEDAZ5kXC/view?usp=drivesdk)
