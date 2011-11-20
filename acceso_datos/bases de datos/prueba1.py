# -*- coding: utf-8 -*-


import csv

ORIGEN_DATOS ='censo_2010_aragon.csv'
def poblacion_total_municipios():
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        reader.next()
        for fila in reader:
            #print fila[0] + '-->' + fila[1] + fila [2]
            try:
                #print fila
                #print fila[1] + '-->' + fila[2] + fila [3]
                #print "%-30s  %9.3f" % (unicode(fila[1])  , float(fila[2]) + float(fila [3]))
                print "%-30s  %9.3f" % (fila[1]  ,
                                 int(fila[2].replace('.', '')) + int(fila[3].replace('.', '')))
            except IndexError: #pongo indexError porque es el que espero
                print ("FINAL DEL FICHERO")

def poblacion_total_provincias():
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        PROVINCIAS={'2': 'HUESCA',
                    '5': 'ZARAGOZA',
                    '4': 'TERUEL'}
        POBLACION={'2' : 0,
                    '5' : 0,
                    '4' : 0}
        reader.next()
        for linea in reader:
            POBLACION[linea[0][0]]=POBLACION[linea[0][0]] + int(linea[2].replace('.', '')) + int(linea[3].replace('.', ''))
        print "%-15s   %9d" % (PROVINCIAS['2'], POBLACION['2'])
        print "%-15s   %9d" % (PROVINCIAS['5'], POBLACION['5'])
        print "%-15s   %9d" % (PROVINCIAS['4'], POBLACION['4'])

def mayores_total():
    datos={}
    with open(ORIGEN_DATOS) as fin:
       reader = csv.reader(fin, delimiter=",")
       reader.next()
       for linea in reader:
           total=int(linea[2].replace('.', '')) + int(linea[3].replace('.', ''))
           datos[total]=linea[1]
       #print datos
       sorted(datos)
       for key in datos.keys():
           print "%-15s --> %9d"%(datos[key], key)

def poblacion_total_aragon():
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        reader.next()
        total=0
        for linea in reader:
           total=total + int(linea[2].replace('.', '')) + int(linea[3].replace('.', ''))
        print "%-15s   %9d" % ('Aragón:', total)

def num_municipios():
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        PROVINCIAS={'2': 'HUESCA',
                    '5': 'ZARAGOZA',
                    '4': 'TERUEL'}
        POBLACION={'2' : 0,
                    '5' : 0,
                    '4' : 0}
        reader.next()
        for linea in reader:
            POBLACION[linea[0][0]]=POBLACION[linea[0][0]] + 1
        print "%-15s   %9d" % (PROVINCIAS['2'], POBLACION['2'])
        print "%-15s   %9d" % (PROVINCIAS['5'], POBLACION['5'])
        print "%-15s   %9d" % (PROVINCIAS['4'], POBLACION['4'])

if __name__ == '__main__':
    #poblacion_total_municipios()
    #poblacion_total_provincias()
    #poblacion_total_aragon()
    #mayores_total()
    num_municipios()
