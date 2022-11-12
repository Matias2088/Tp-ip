from principal import *
from configuracion import *
import random
import math



def nuevaPalabra(lista):
    numero=random.randrange(len(lista))
    return lista[numero]

def lectura(archivo, salida, largo):
    lista=reparar(archivo)
    for i in lista:
        if len(i)==largo:
            salida.append(i)

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    cont=0
    for i in palabra:
        if i in palabraCorrecta:
            if palabraCorrecta[cont]==palabra[cont] and i not in correctas:
                correctas.append(i)
            elif i not in correctas and i not in casi:
                casi.append(i)
        elif i not in incorrectas:
            incorrectas.append(i)
        cont+=1

    if palabraCorrecta==palabra:
        return True
    return False

def largoPalabra(lista,largo):
    lista=[]
    for i in lista:
        if len(i)==largo:
            lista.append(i)
    return lista

def reparar(archivo):
    datos=archivo.readlines()
    lista=[]
    for i in range(len(datos)):
        lista.append(datos[i][:-1])
    return lista

def cambiarColorLetra(letra,correctas,casi,incorrectas):
    if letra in correctas:
        return dameColor("verde")
    elif letra in casi:
        return dameColor("amarillo")
    elif letra in incorrectas:
        return dameColor("rojo")
    else:
        return dameColor("normal")

def dameColor(color):
    if color=="verde":
        pintar=(10,250,10)
        return pintar
    elif color=="amarillo":
        pintar=(250,250,10)
        return pintar
    elif color=="rojo":
        pintar=(250,10,10)
        return pintar
    else:
        pintar=COLOR_TEXTO
        return pintar







