![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

# ¡Proyecto Calzados! [Python]
En este repositorio contiene todos los materiales e instrucciones para poder realizar el proyecto de calzado de programador python.

Este proyecto se acerca al tipo de trabajo y de desafios que tendrán en el curso de Python Analytics.

Para este proyecto ya cuenta con una base de datos SQL para consumir y hacer análisis de datos.


## Objetivo
El objetivo es analizar los datos de ventas de calzados deportivos, obtener métricas por pais, génerico y talle del calzado. Deberá:
- Levantar el dataset en numpy, filtrando información inválida.
- Crear una serie de funciones que se detallarán más adelante, la cual cada una tiene un objetivo de análisis.

## Recursos
- Contará con un archivo "ventas_calzados.db", una base de datos SQL con toda la información necesaria.
- Tenga en cuenta que en esa base de datos hay datos faltantes.


## Como comenzar
- Deberá crear un archivo "main.py" en el cual colocará todo el código necesario para realizar el proyecto.
- Dentro de ese archivo deberá importar las librerías que crea necesarias para la realización del proyecto.
- Luego deberá crear el bloque principal `if __name__ == "__main__":`. Dentro del bloque principal invocará sus funciones y desarrollará el proyecto.
- Entre el lugar donde usted importo las librerías y generó el bloque pincipal, ahí irá creando sus funciones que se detallan.


## Base de datos
Deberá consumir la base de datos SQL "ventas_calzados.db". Utilizar SQLAlchemy para crear una clase que responda a la tabla "ventas". Dicha tabla "ventas" debe contener las siguientes columnas:
- id --> número (Integer) (autoincremental, primary_key)
- fecha --> texto (String) (fecha en la cual se efectuó la venta)
- producto_id --> número (Integer) (id del producto vendido)
- pais --> texto (String) (país en donde se efectuó la venta)
- genero --> texto (String) (si el calzado era "Female", "Male" o "Unix")
- talle --> texto (String) (talle del calzado)
- precio --> texto (String) (precio, viene con el símbolo $ adelante)


## Funciones del sistema
Dentro del archivo __main.py__ deberá implementar las siguientes funciones que utilizará luego el bloque main para armar el proyecto:

### Funcion "read_db"
Encabezado de la función:
```python
def read_db():
```

Entrada (argumentos):
- Esta función no recibe parámetros.

Objetivo:
- La función deberá leer la base de datos y recorrer todas la filas. Deberá ir almacenando los datos de las siguientes columnas en 4 array numpy separados:
    - paises
    - generos
    - talles
    - precios
- Tip: Crear 4 listas para almacenar los datos solicitados, luego cada una de esas listas las puede transformar en arrays numpy con:
```python
mi_array = np.array(mi_lista)
```
- El array de numpy "precios" debe contener los precios en tipo de dato "float". Para ello, primero usted debe quitar del precio el símbolo "$" para poder transformarlo a float.

Salida (return):
- La función deberá retornar todos los array numpy creados, en el siguiente orden:
```python
return paises, generos, talles, precios
```

### Funcion "obtener_paises_unicos"
Encabezado de la función:
```python
def obtener_paises_unicos(paises):
```

Entrada (argumentos):
- Esta función recibe por parámetro el array numpy creado de paises.

Objetivo:
- Deberá obtener una lista de paises únicos de ese array numpy (es decir, que paises realizaron ventas en el dataset).
- Recomendamos investigar la función "np.unique" que lo ayudará a resolver este problema de manera fácil y óptima.

Salida (return):
- La función deberá retornar lista/array de paises únicos.

Ejemplo:
- paises --> ["Canada", "Canada", "Germany", "Argentina", "USA", "Canada"]
- salida --> ["Canada", "Germany", "Argentina", "USA"]

### Funcion "obtener_ventas_por_pais"
Encabezado de la función:
```python
def obtener_ventas_por_pais(paises_objetivo, paises, precios):
```

Ejemplo (a modo de referencia):
- Esta función recibe por parámetro:
    - paises_objetivo --> Lista de nombres de paises que se desea analizar
    - paises --> array numpy de paises de ventas del dataset
    - precios --> array numpy de precios de ventas del dataset

Objetivo:
- Deberá armar un diccionario cuyas claves sean los nombres de los paises solicitados a analizar (detallados en paises_objetivo).
- En cada clave deberá almacenar cuanto dinero total recaudó cada país a analizar en sus ventas (recorriendo el array numpy de paises y precios).
- Para poder obtener las ventas que realizó cada país del array numpy "precios", puede utilizar el concepto de máscaras (mask) para otener todos los elementos de un array vinculados a un país (ver archivo numpy_mask.py como referencia).

Salida (return):
- La función deberá retornar el diccionario con el monto/dinero que cada país acumuló en sus ventas.

Ejemplo (a modo de referencia):
- paises_objetivo --> ["Canada", "Germany"]
- paises --> ["Canada", "Canada", "Canada", "Germany", "Argentina"]
- precios --> [250, 250, 100, 120, 50]
- salida --> {"Canada": 600, "Germany": 120}


### Funcion "obtener_calzado_mas_vendido_por_pais"
Encabezado de la función:
```python
def obtener_calzado_mas_vendido_por_pais(paises_objetivo, paises, talles):
```
Entrada (argumentos):
- Esta función recibe por parámetro:
    - paises_objetivo --> Lista de nombres de paises que se desea analizar
    - paises --> array numpy de paises de ventas del dataset
    - talles --> array numpy de talles de calzados vendidos

Objetivo:
- Deberá armar un diccionario cuyas claves sean los nombres de los paises solicitados a analizar (detallados en paises_objetivo).
- En cada clave deberá almacenar cual fue el talle de calzado que más se vendió de ese país (recorriendo el array numpy de paises y talles).
- Para poder obtener que cantidad se vendió de cada talle de calzado puede investigar la función np.unique con el parámetro return_counts=True.

Salida (return):
- La función deberá retornar el diccionario con el talle del calzado más vendido en cada país en sus ventas.

Ejemplo (a modo de referencia):
- paises_objetivo --> ["Canada", "Germany"]
- paises --> ["Canada", "Canada", "Canada", "Germany", "Argentina"]
- talles --> ["10.5", "9", "10.5", "11", "9"]
- salida --> {"Canada": "10.5", "Germany": "11"}


### Funcion "obtener_ventas_por_genero_pais"
Encabezado de la función:
```python
def obtener_ventas_por_genero_pais(paises_objetivo, genero_objetivo, paises, generos):
```

Entrada (argumentos):
- Esta función recibe por parámetro:
    - paises_objetivo --> Lista de nombres de paises que se desea analizar
    - genero_objetivo --> El género de calzado que se desea analizar
    - paises --> array numpy de paises de ventas del dataset
    - generos --> array numpy de genero de calzado en cada venta del dataset

Objetivo:
- Deberá armar un diccionario cuyas claves sean los nombres de los paises solicitados a analizar (detallados en paises_objetivo).
- En cada clave deberá almacenar cuantos calzados del género a analizar (genero_objetivo) se vendió en cada país (recorriendo el array numpy de paises y generos).
- Para poder filtrar los calzados por país y luego por género también puede utilizar mascaras de numpy (una máscara para cada criterio de búsqueda/filtrado).

Salida (return):
- La función deberá retornar el diccionario con la cantidad de calzados vendidos en el género solicitado por cada país en sus ventas.

Ejemplo (a modo de referencia):
- paises_objetivo --> ["Canada", "Germany"]
- genero_objetivo --> "Female"
- paises --> ["Canada", "Canada", "Canada", "Germany", "Argentina"]
- generos --> ["Female", "Unix", "Female", "Male", "Male"]
- salida --> {"Canada": 2, "Germany": 0}


## Bloque principal del programa
Dentro del bloque principal del programa deberá invocar las funciones que usted haya creado para ponerlas a prueba. La función "read_db" le dará los datos que necesita para probar las otras funciones:
```python
if __name__ == "__main__":
    print("\n¡Aquí utilizo mis funciones!\n")
```

## Milla extra
Crear otro archivo llamado "graficos.py" como copia del archivo "main.py". En en archivo graficos utilice plots de matplotlib o seaborn para ilustrar el output de cada función.
