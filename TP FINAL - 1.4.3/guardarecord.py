#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from principal import *

#crear funcion puntajes para guardar
def guardar_puntajes(puntajes):
    archivo = open("resultados.cvs", "a")
    for nombre, puntos,  in puntajes:
        archivo.write(nombre+","+str(puntos)+"\n")
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    lista = []
    archivo = open(nombre_archivo, "r")
    for línea in archivo:
        nombre, puntos = línea.rstrip("\\n").split(",")
        lista.append((nombre,int(puntos)))
    archivo.close()
    return lista


def ordenar(lista):
    ordenados=sorted(lista)
    return ordenados

def mejores10(lista):
    mejores=[]
    x=0
    for i in range(len(lista)):
        if x<10:
            mejores.append(lista[i])
            x+=1
    return mejores

def devoluciones10():
    nombre_archivo="resultados.cvs"
    lista=mejores10(ordenar(recuperar_puntajes(nombre_archivo)))
    return lista
