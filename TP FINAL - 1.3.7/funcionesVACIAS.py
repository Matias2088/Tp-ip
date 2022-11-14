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
        return COLOR_VERDE
    elif letra in casi:
        return COLOR_AMARILLO
    elif letra in incorrectas:
        return COLOR_ROJO
    else:
        return COLOR_TEXTO

def mostrarTexto(screen,texto,tipoDeRenderizado,ColorDelTexto,coordenadaX,
                coordenadaY,TamañoDeLaFuente,NombreDeLaFuente = pygame.font.get_default_font()):
    #Tipo y tamaño de letra
    FuenteDelTexto = pygame.font.Font( NombreDeLaFuente , TamañoDeLaFuente )
    #Frase y sus caracteristicas
    EtiquetaDelTexto = FuenteDelTexto.render( texto , tipoDeRenderizado , ColorDelTexto )
    ###--Esto es lo que escribe en pantalla--###
    screen.blit( EtiquetaDelTexto, ( coordenadaX-EtiquetaDelTexto.get_width()//2, coordenadaY))




