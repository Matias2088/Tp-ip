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
    pygame.mixer.music.load("Musica/musicafondo.mp3")
    pygame.mixer.music.play(3)
    pygame.mixer.music.set_volume(0.30)
    sonidoAcierto = pygame.mixer.Sound("Musica/oh-yeah.wav")

    #Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    
    #fondo juego
    FONDO = pygame.image.load("Fondos/13.jpg").convert()
    FONDO2 = pygame.image.load("Fondos/12.jpg").convert()
    FONDO3 = pygame.image.load("Fondos/15.jpg").convert()

    #valores de inicio
    inicio = True
    salir = False
    final = False
    moverFigura = False
    guarda = False

    rec7_X1 = REC6_X1 + 169
    rec7_X2 = rec7_X1 + 15
    rec7_X12 = rec7_X2 - rec7_X1
    puntos = 0

    #bucle general
    while not(salir):

        #bucle de inicio
        while inicio:
            #dibujar
            screen.blit(FONDO3,[0,0])
            dibujarInicio(screen,[rec7_X1,rec7_X2,rec7_X12])
            pygame.display.flip()

            #posicion del mouse
            mouseX,mouseY = pygame.mouse.get_pos()

            #saca el evento ocurrido en pygame
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                #Esc para salir
                elif e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        inicio = False
                        pygame.quit()
                        return()

                if pygame.mouse.get_pressed()[0]:
                    #botones de inicio
                    if mouseX in range(REC3_X1,REC3_X2+1):
                        #Jugar
                        if mouseY in range(REC3_Y1,REC3_Y2+1):
                            inicio = False
                        #Salir
                        elif mouseY in range(REC4_Y1,REC4_Y2+1):
                            pygame.quit()
                            return 
                        #Acerca de
                        elif mouseY in range(REC5_Y1,REC5_Y2+1):
                            print("acerca de")

                    #Activa el movimiento del "scrol"
                    if e.type == MOUSEBUTTONDOWN:
                        if mouseX in range(rec7_X1,rec7_X2+1) and mouseY in range(REC7_Y1,REC7_Y2+1):
                            moverFigura = True

                #Mueve el scrol a la par del mouse
                if moverFigura:
                    if mouseX in range(REC6_X1,REC6_X2-12):
                        rec7_X1 = mouseX
                        rec7_X2 = rec7_X1 + rec7_X12
                        
                #Deja de mover el scrol al soltar el clic
                if e.type == MOUSEBUTTONUP:
                    moverFigura = False
                    if int(rec7_X1%160) <=80:
                        rec7_X1 -= int(rec7_X1%160 +6)
                    else:
                        rec7_X1 += int(154-rec7_X1%160)
                    rec7_X2 = rec7_X1 + rec7_X12
                    
        #Reiniciar valores
        if not(final):
            #tiempo total del juego
            gameClock = pygame.time.Clock()
            totaltime = 0
            fps = FPS_inicial

            #Define la cantidad de segundos segun la dificultad
            if rec7_X2 <= 310:
                segundos = TIEMPO_BASE*2
            elif rec7_X2 <= 470:
                segundos = TIEMPO_BASE
            elif rec7_X2 <= 630:
                segundos = TIEMPO_BASE//2
            else:
                segundos = TIEMPO_BASE//4

            #valores basicos
            nombre = ""
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
   
        #bucle del juego
        while segundos > fps/1000 and intentos > 0 and not gano:
            # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            #contador de segundos
            tiempoReal = pygame.time.get_ticks()/1000
            if tiempoReal// 1 == contador + 1:
                contador += 1
                segundos -= 1

            #Define los cuadros por segundo del juego
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

                            gano = revision(palabraCorrecta.lower(), palabraUsuario, correctas, incorrectas, casi)
                            ListaDePalabrasUsuario.append(palabraUsuario)
                            palabraUsuario = ""
                            intentos -= 1
                            
            #agregar sonido
            if gano:
                puntos+=1
                #sonido ganador
                sonidoAcierto.play()
                pygame.mixer.music.set_volume(0.30)

            if intentos==0 or  int(segundos)==0 :
                pygame.mixer.music.load("Musica/game over.mp3")
                pygame.mixer.music.play() 
                pygame.mixer.music.set_volume(0.30)

            #Limpiar pantalla anterior            
            screen.blit(FONDO,[0,0])

            #Dibujar de nuevo todo
            dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano,
                    correctas, incorrectas, casi,error,palabraCorrecta, intentos)
            pygame.display.flip()
        
        #bucle Final
        final = True
        while final and not(salir):
            #dibujar
            screen.blit(FONDO2,[0,0])
            dibujarFinal(screen,gano,palabraCorrecta,intentos,segundos)
            pygame.display.flip()

            #posicion del mouse
            mouseX,mouseY = pygame.mouse.get_pos()

            #saca el evento ocurrido en pygame           
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

                elif e.type == KEYDOWN:
                    #Esc para salir
                    if e.key == K_ESCAPE:
                        salir = True
                        final = False
                        pygame.quit()
                        return()

                if pygame.mouse.get_pressed()[0]:
                    #botones
                    if mouseY in range(REC1_Y1,REC1_Y2+1):
                        #Reiniciar
                        if mouseX in range(REC1_X1,REC1_X2+1):
                            final = False
                        #Menu
                        elif mouseX in range(REC8_X1,REC8_X2+1):
                            final = False
                            inicio = True
                    elif mouseY in range(REC2_Y1,REC2_Y2+1):
                        #Salir
                        if mouseX in range(REC2_X1,REC2_X2+1):
                            salir = True
                            final = False
                            pygame.quit()
                            return
                        #GUARDAR
                        elif mouseX in range(REC9_X1,REC9_X2+1):
                            print("GUARDAR")
                            final= False
                            guarda= True
        while guarda and not salir:
            screen.blit(FONDO2,[0,0])
            dibujarGuardar(screen,nombre)
            pygame.display.flip()
           

            #posicion del mouse
            mouseX,mouseY = pygame.mouse.get_pos()

            #saca el evento ocurrido en pygame           
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

                elif e.type == KEYDOWN:
                    #Esc para salir
                    if e.key == K_ESCAPE:
                        salir = True
                        final = False
                        pygame.quit()
                        return()
                    letra = dameLetraApretada(e.key)
                    nombre += letra 
                    #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        nombre = nombre[0:len(nombre)-1]
                    #Salir del juego presionando el ESC
                    if e.key == K_ESCAPE:
                        pygame.quit()
                        return
                    if e.key == K_RETURN:
                        puntaje=[(nombre,puntos)]
                        guardar_puntajes(puntaje) 
                        guarda = False
                        inicio = True
            if pygame.mouse.get_pressed()[0]:
                if mouseY in range(REC10_Y1,REC10_Y2+1):
                        #Salir
                        if mouseX in range(REC10_X1,REC10_X2+1):
                            salir = True
                            final = False
                            pygame.quit()
                            return                

    #cierre del juego si se rompe el bucle
    pygame.quit()
    return        

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
