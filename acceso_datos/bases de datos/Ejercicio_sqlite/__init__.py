#-*- coding: utf-8 -*-
'''
Created on 07/09/2011

@author: alumno
'''
"""
vamos a coger todos los estudiantes que hemos creado con shelve y los vamos a guardar en sqlite
"""

import shelve  #se recomienda hacer los import arriba del todo.
import sqlite3 as dbapi

class Estudiante(object):
    def __init__(self, matricula, nombre, direccion, curso):
        self.matricula = matricula
        self.nombre = nombre
        self.direccion = direccion
        self.curso = curso

    def __str__(self):
        return self.matricula + ': ' + self.nombre


if __name__ == '__main__':

# 1. Creamos objeto conexión
    bbdd = dbapi.connect("alumnos_sql.dat")
    almacen = shelve.open('alumnos.dat')

# 2. Creamos un cursor, con el accederemos a nuestras tablas
    cursor = bbdd.cursor()

# 3. Usamos cursor para acceder a la  base de datos
# 3.1. create
    cursor.execute("""drop table alumnos""")
    cursor.execute("""create table alumnos (matricula text,
                  nombre text,
                  direccion text,
                  curso text)""")
    # escribimos
    for matric in almacen:
        print almacen[matric].matricula, almacen[matric].nombre,almacen[matric].direccion, almacen[matric].curso
        SQL = """insert into alumnos
                    values (?, ?, ?, ?)"""
        #cursor.execute(SQL, ('5', 'ddd','ddd','eeee'))
        cursor.execute(SQL, (almacen[matric].matricula, almacen[matric].nombre, almacen[matric].direccion, almacen[matric].curso))

        #ahora vamos a leer la tabla
    cursor.execute('select * from alumnos')
    for est in cursor.fetchall():
        print est  #recogemos como una tupla
    bbdd.commit()
