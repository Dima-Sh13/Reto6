import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def select_all():
    conect = Conexion("SELECT * from movement ORDER By date DESC;")
    filas = conect.res.fetchall()#datos de columnas (2025-09-01, Nomina,1800),(2025-09-05,Mercado,-100)
    columnas = conect.res.description#nombre de columnas en las primeras filas (id,0000),(date,000)

    lista_diccionario= []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] =  f[posicion]
            posicion+=1
        lista_diccionario.append(diccionario)

    conect.con.close()
    
    return lista_diccionario

def insert(registroForm):
    conectInsert = Conexion("INSERT INTO movement (date, concept, quantity) VALUES (?,?,?);",registroForm)
    conectInsert.con.commit()#funcion para validar el registro antes de guardarlo
    conectInsert.con.close()


def select_by(id):
    conectSelectBy= Conexion(f"SELECT * from movement WHERE id={id};")
    result = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()

    return result[0]


def delete_by(id):
    conectDelete= Conexion(f"DELETE FROM movement WHERE id={id};")
    conectDelete.con.commit()#funcion para validar borrado
    conectDelete.con.close()


def update_by(id,registros):
    conectUpdate = Conexion(f"UPDATE movement SET date=?,concept=?, quantity=? WHERE id={id};",registros)    
    conectUpdate.con.commit()#funcion para validar update
    conectUpdate.con.close()
 
def select_ingreso():
    conectIngreso=Conexion("select SUM(quantity) from movement where quantity>0;")
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso=Conexion("select SUM(quantity) from movement where quantity<0;")
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]


def select_by_date(date):
    conectSelectBy= Conexion(f"SELECT * from movement WHERE date={date};")
    result = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()

    return result

def ByConcept(concept):
    concectCon =Conexion("SELECT concept FROM movement ")
    result = concectCon.res.fetchall()
    concectCon.con.close()
    listConcept = list(concept)
    strike = 0
    strike_indx = {}
    for i in result:                                           #Reccoremos todos los conceptos de la lista uno a uno
        for x in range(len(concept)):                          #Un for para recorrer incrementar un indice de busqueda por posicion de las str  
            if i[x] == concept[x]:                             #Recorremos los conceptos de la lista letra por letra y los comparamos a la misma posicion del concepto buscado, si es igual se suma strike
                strike += 1
        strike_indx[i] = strike                                #Añadimos el resultado del strike y la palabra a la que pertenece a un diccionario
        strike = 0                                             #Volvemos a dejar el strike en 0 y pasamos a la proxima palabra.