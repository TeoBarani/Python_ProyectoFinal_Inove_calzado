import numpy as np
import matplotlib.pyplot as plt

def graficar_ventas_totales(dic):
    x = list(dic.keys())
    y = list(dic.values())
    
    fuente_titulo = {'family': 'helvetica',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

    fig, ax = plt.subplots()
    ax.bar(x, y, color=['darkblue', 'red', 'green'])
    ax.set_xlabel('Paises/Countries')
    ax.set_ylabel('Ventas/Sales')
    ax.set_title('Ventas totales por país', fontdict=fuente_titulo)

    plt.show()

def graficar_ventas_genero(dic, genero):
    x = list(dic.keys())
    y = list(dic.values())
    
    fuente_titulo = {'family': 'helvetica',
        'color':  'white',
        'weight': 'normal',
        'size': 16,
        'backgroundcolor': 'black'
        }

    fig, ax = plt.subplots()
    ax.bar(x, y, color=['darkblue', 'red', 'green'])
    ax.set_xlabel('Paises/Countries')
    ax.set_ylabel('Ventas/Sales')
    ax.set_title(f'Ventas del género {genero} por país', fontdict=fuente_titulo)

    plt.show()

