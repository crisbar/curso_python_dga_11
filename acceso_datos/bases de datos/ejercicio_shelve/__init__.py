#-*- coding: utf-8 -*-
'''
Created on 07/09/2011

@author: alumno
'''
"""
    Crea una clase Estudiante que almacene su código (código de matrícula), nombre, dirección y curso.
    Después crea un almacén persistente (base de datos shelve) para almacenar los estudiantes.
    Como clave usarás el código del alumno. Almacena diez estudiantes en el almacén.
    Crea un programa que recorrra el fichero shelve creado y muestre los nombres de los alumno,
    ordenados por curso / nombre.
"""
import shelve  #se recomienda hacer los import arriba del todo.

class Estudiante(object):
    def __init__(self, matricula, nombre, direccion, curso):
        self.matricula = matricula
        self.nombre = nombre
        self.direccion = direccion
        self.curso = curso

    def __str__(self):
        return self.matricula + ': ' + self.nombre

    #si queremos hacer un método para que guarde el objeto directamente:
    def guardar(self, almacen):
        almacen[self.matricula] = self


def almacena(alumno):
    almacen = shelve.open('alumnos.dat') #si no existe, lo creará
     #manejamos los datos como un diccionario
     #importante, las claves tienen que ser cadenas de caracteres.
    almacen[alumno.matricula] = alumno #ponemos como identificador el numero de matricula del estudiante
    almacen.sync() #para guardar lo que haya en memoria
    almacen.close()

def listado():
    almacen = shelve.open('alumnos.dat')
    for matric in almacen:
        print almacen[matric]

def dame_estudiante(matric):
    almacen = shelve.open('alumnos.dat')
    return almacen[matric]



if __name__ == '__main__':
    """
    creamos los datos

    est1 = Estudiante('2', 'Juan', 'C/ luna', '1SMR')
    est2 = Estudiante('3', 'Ana', 'C/ Jupiter', '1SMR')
    est3 = Estudiante('4', 'Jorge', 'C/ luna', '1DAI')
    est4 = Estudiante('5', 'Ivan', 'C/ luna', '2DAI')
    est5 = Estudiante('6', 'Eva', 'C/ luna', '1DAM')
    est6 = Estudiante('7', 'David', 'C/ luna', '1SMR')

    for est in [est1, est2, est3, est4, est5, est6]:
        almacena(est)
    """
    listado()
