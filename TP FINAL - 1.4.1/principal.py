#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *

#Funcion principal
def main():
    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    #pygame.mixer.init()
    pygame.mixer.music.load("Musica/competition.mp3")
    pygame.mixer.music.play(2)

    #Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    
    #fondo juego
    FONDO = pygame.image.load("Fondos/13.jpg").convert()
    FONDO2 = pygame.image.load("Fondos/12.jpg").convert()

    
    salir = False
    final = False

    while not(salir):

        if not(final):
            #tiempo total del juego
            gameClock = pygame.time.Clock()
            totaltime = 0
            segundos = TIEMPO_MAX
            fps = FPS_inicial

            puntos = 0
            palabraUsuario = ""
            listaPalabrasDiccionario=[]
            ListaDePalabrasUsuario = []
            correctas = []
            incorrectas = []
            casi = []
            gano = False
            error = ""
            intentos = 5
            contador = (pygame.time.get_ticks()/1000)//1

            archivo= open("lemario.txt","r")
            #lectura del diccionario
            lectura(archivo, listaPalabrasDiccionario)

            #elige una al azar
            #quitar ,LARGO para obtener una palabra aleatoria
            palabraCorrecta=nuevaPalabra(listaPalabrasDiccionario,LARGO)

            print(palabraCorrecta)
            archivo.close()
   
        while segundos > fps/1000 and intentos > 0 and not gano:
            # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            #contador de segundos
            tiempoReal = pygame.time.get_ticks()/1000
            if tiempoReal// 1 == contador + 1:
                contador += 1
                segundos -= 1

            if True:
                fps = 10

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra 
                    #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    #Salir del juego presionando el ESC
                    if e.key == K_ESCAPE:
                        pygame.quit()
                        return
                    if e.key == K_RETURN:
                            error = ""
                            #Controles:
                            #Avisa si la palabra no esta en el diccionario
                            if palabraUsuario not in listaPalabrasDiccionario:
                                error = "palabra desconocida"
                                palabraUsuario = ""
                                continue

                            #Avisa si la palabra no tiena la longitud deseada
                            if len(palabraUsuario)!=len(palabraCorrecta):
                                error = "logitud erronea"
                                palabraUsuario = ""
                                continue
                            #avisa que la palabra ya fue ingresada
                            if palabraUsuario in ListaDePalabrasUsuario:
                                error ="ya ingresada"
                                palabraUsuario = ""
                                continue
                            #vaciar las listas, para no acumular las letras
                            correctas = []
                            incorrectas = []
                            casi = []

                            gano = revision(palabraCorrecta.lower(), palabraUsuario, correctas, incorrectas, casi)
                            ListaDePalabrasUsuario.append(palabraUsuario)
                            palabraUsuario = ""
                            intentos -= 1
                            

            if gano:
                puntos+=1
                #sonido ganador
                pygame.mixer.music.load("Musica/win.mp3")
                pygame.mixer.music.play()

            if intentos==0 or  int(segundos)==0 :
                pygame.mixer.music.load("Musica/game over.mp3")
                pygame.mixer.music.play() 

            #Limpiar pantalla anterior
            
            screen.blit(FONDO,[0,0])

            #Dibujar de nuevo todo
            dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano,
                    correctas, incorrectas, casi,error,palabraCorrecta, intentos)

            pygame.display.flip()
        

        final = True
        while final:
            screen.fill(COLOR_FONDO)
            screen.blit(FONDO2,[0,0])
            dibujarFinal(screen,gano,palabraCorrecta,intentos,segundos)
            pygame.display.flip()

            mouseX,mouseY = pygame.mouse.get_pos()
            
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

                elif e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        salir = True
                        final = False

                if pygame.mouse.get_pressed()[0]:
                    if mouseY in range(REC1_Y1,REC1_Y2+1):
                        if mouseX in range(REC1_X1,REC1_X2+1):
                            print("REINICIAR")
                            final = False
                        elif mouseX in range(REC2_X1,REC2_X2+1):
                            print("SALIR")
                            final = False
                            salir = True

    pygame.quit()
    return        

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
