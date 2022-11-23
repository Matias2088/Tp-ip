#! /usr/bin/env python

from pygame.locals import *
from configuracion import *
from principal import *

#crear funcion puntajes para guardar
def guardar_puntajes(puntajes):
    archivo = open("resultados.txt", "a")
    for nombre, puntos, in puntajes:
        archivo.write("\n"+nombre+","+str(puntos))
    archivo.close()

#devuelve los nombres y puntos en una lista
def recuperar_puntajes(nombre_archivo):
    lista = []
    archivo = open(nombre_archivo, "r")
    for línea in archivo:
        nombre,puntos = línea.rstrip("\\n").split(",")
        lista.append((nombre,int(puntos)))
    archivo.close()
    return lista
# toma el elemento numero para ordenar
def take_second(elem):
    return elem[1]

#devuelve la lista con los elementos ordenados de mayor a menor
def ordenar(lista):
    ordenados=sorted(lista,key=take_second,reverse=True)
    return ordenados

#devuelve una lista con los 10 primeros numeros
def mejores10(lista):
    mejores=[]
    x=0
    for i in range(len(lista)):
        if x<10:
            mejores.append(lista[i])
            x+=1
    return mejores

#devuelve una lista con los mejores 10 puntajes
def devoluciones10():
    nombre_archivo="resultados.txt"
    lista=mejores10(ordenar(recuperar_puntajes(nombre_archivo)))
    return lista
