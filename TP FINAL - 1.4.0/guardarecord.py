#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *
from principal import *

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *
from principal import *

#falta modificar para que guarde el nombre y los puntos
def guardar(nombre, puntos):
    archivo= open("record.txt","a")
    archivo.write("nombre\n")
    archivo.write("puntos\n")
    archivo.close()

archivo= open("record.txt","r")
lista=reparar(archivo)
archivo.close()

#separa el archivo en nombre y puntos
def separar(lista):
    li1=[]
    li2=[]
    for i in range(len(lista)):
        if i%2==0:
            li1.append(lista[i]) 
        else:
            li2.append(lista[i])  
    
    return (li1,li2)

listamatriz=separar(lista)
lNombres=listamatriz[0]
lPuntos=listamatriz[1]

#devuelve el inice del maximo valor
def maximoIndice(lista):
    valor = lista[0]
    maxI = 0
    for i in range(len(lista)):
        if(valor < lista[i]):
            valor = lista[i]
            maxI = i
    return maxI 

def topPlayers(lista1,lista2):
    lisnombres=[]
    lisnumeros=[]

