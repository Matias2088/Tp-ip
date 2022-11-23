from principal import *
from configuracion import *
import random
import math

#Elije una palabra al azar
def nuevaPalabra(lista,largo=0):
    numero=random.randrange(len(lista))
    if largo >0:
        while len(lista[numero]) != largo:
            numero=random.randrange(len(lista))
    return lista[numero]

#Lee el archivo 
def lectura(archivo, salida):
    lista=reparar(archivo)
    for i in lista:
        salida.append(i)

#Avisa si el jugador adivino la palabra, ademas verifica las letras de las palabras
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

#Quita los saltos de texto en el archivo
def reparar(archivo):
    datos=archivo.readlines()
    lista=[]
    for i in range(len(datos)):
        lista.append(datos[i][:-1]) 
    return lista

#Cambia el color de las letras del teclado
def cambiarColorLetra(letra,correctas,casi,incorrectas):
    if letra in correctas:
        return COLOR_VERDE
    elif letra in casi:
        return COLOR_AMARILLO
    elif letra in incorrectas:
        return COLOR_ROJO
    else:
        return COLOR_TEXTO

#Tipo y tamaño de letra
def FuenteDelTexto(tamannoDeLaFuente, nombreDeLaFuente = pygame.font.get_default_font()):
    fuente = pygame.font.Font( nombreDeLaFuente , tamannoDeLaFuente )
    return fuente
    #Frase y sus caracteristicas
def EtiquetaDelTexto(texto,tipoDeRenderizado,ColorDelTexto,fuente):
    etiqueta = fuente.render( texto , tipoDeRenderizado , ColorDelTexto )
    return etiqueta
    
    ###--Esto es lo que escribe en pantalla--###
def mostrarTexto(screen,coordenadaX,coordenadaY,etiqueta):
    screen.blit( etiqueta, ( coordenadaX - etiqueta.get_width()//2, coordenadaY))



