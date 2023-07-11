import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np
import graficar 

engine = sqlalchemy.create_engine("sqlite:///ventas_calzados.db")
base = declarative_base()

class Ventas(base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    producto_id = Column(Integer)
    pais = Column(String)
    genero = Column(String)
    talle = Column(String)
    precio = Column(String)

def crear_tabla():
    base.metadata.create_all(engine)


def read_db():
    paises = []
    generos = []
    talles = []
    precios = []

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Ventas)
    data = query.all()

    for row in data:
        paises.append(row.pais)
        generos.append(row.genero)
        talles.append(row.talle)
        precios.append(float(row.precio.replace('$', '')))

    
    paises = np.array(paises)
    generos = np.array(generos)
    talles = np.array(talles)
    precios = np.array(precios)

    return paises, generos, talles, precios

def obtener_paises_unicos(paises):
    paises_unicos = np.unique(paises)

    return paises_unicos

def obtener_ventas_por_pais(paises_objetivo, paises, precios):
    dic_paises = {}

    for pais in paises_objetivo:
        mask = paises == pais
        ventas_pais = precios[mask]
        dic_paises[pais] = float(sum(ventas_pais))

    return dic_paises

def obtener_calzado_mas_vendido_por_pais(paises_objetivo, paises, talles):
    dic_paises_talles = {}

    for pais in paises_objetivo:
        mask = paises == pais
        talles_pais = np.unique(talles[mask], return_counts=True)
        talle_mayor_cantidad = np.where(talles_pais[1] == np.max(talles_pais[1]))
        dic_paises_talles[pais] = talles_pais[0][int(talle_mayor_cantidad[0])]

    return dic_paises_talles

def obtener_ventas_por_genero_pais(paises_objetivo, genero_objetivo, paises, generos):
    dic_paises_genero = {}

    for pais in paises_objetivo:
        mask = paises == pais 
        generos_pais = np.unique(generos[mask], return_counts=True)
        calzado_genero = np.where(generos_pais[0] == genero_objetivo)
        dic_paises_genero[pais] = generos_pais[1][int(calzado_genero[0])]
    
    return dic_paises_genero


if __name__ == "__main__":
    crear_tabla()
    db = read_db()
    obtener_paises_unicos(db[0])
    paises_objetivo = ['United States', 'United Kingdom', 'Canada']
    genero_objetivo = 'Male'
    ventas_por_pais = obtener_ventas_por_pais(paises_objetivo, db[0], db[3])
    obtener_calzado_mas_vendido_por_pais(paises_objetivo, db[0], db[2])
    ventas_por_genero = obtener_ventas_por_genero_pais(paises_objetivo, genero_objetivo, db[0], db[1])
    graficar.graficar_ventas_totales(ventas_por_pais)
    graficar.graficar_ventas_genero(ventas_por_genero, genero_objetivo)
