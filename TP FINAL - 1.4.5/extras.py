import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
from guardarecord import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key ==241:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

#Primera funcion dibujar
def dibujarInicio(screen,rectangulo7):

    #Dibuja las figuras
    #rectangulo Jugar
    REC3 = pygame.Rect(REC3_X1,REC3_Y1,REC3_X12,REC3_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC3,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC3,7,30)
    #rectangulo Salir
    REC4 = pygame.Rect(REC4_X1,REC4_Y1,REC4_X12,REC4_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC4,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC4,7,30)
    #Rectangulo acerca de
    REC5 = pygame.Rect(REC5_X1,REC5_Y1,REC5_X12,REC5_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC5,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC5,7,30)


    #Poner en una funcion
    #Pone la linea de dificultad en colores
    cont = rojo = 0
    verde = 255
    while cont <=510:
        pygame.draw.line(screen,(rojo,verde,0),(REC6_X1+cont,REC6_Y1),(REC6_X1+cont,REC6_Y2))
        cont +=1
        if cont%2 == 0:
            rojo +=1
            verde -=1

    #Poner en una funcion
    #Separadores de dificultad
    fuenteDificultad = pygame.font.Font( pygame.font.get_default_font(), 30)
    cont = 0
    for LINEA_POS_X in LINEAS_DIFICULTAD_X:
        if cont == 0:
            dificultad = "Facil"
        elif cont == 1:
            dificultad = "Normal"
        elif cont == 2:
            dificultad = "Dificil"
        else:
            dificultad = "Imposible"
        EtiquetaDificultad = EtiquetaDelTexto(dificultad,1,COLOR_VERDE,fuenteDificultad)

        pygame.draw.line(screen,COLOR_GRIS_OSCURO,(LINEA_POS_X,REC6_Y1-10),(LINEA_POS_X,REC6_Y2+10),6)
        screen.blit(EtiquetaDificultad,(LINEA_POS_X-EtiquetaDificultad.get_width()//2,REC6_Y1+40))

        cont +=1

    #Selector de difultad
    REC7 = pygame.Rect(rectangulo7[0],REC7_Y1,rectangulo7[2],REC7_Y12)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC7,0,10)

    #Valores base de los textos
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 40)
    etiquetaJugar = EtiquetaDelTexto("Jugar",1,COLOR_AZUL,defaultFont)
    etiquetaSalir = EtiquetaDelTexto("Salir",1,COLOR_AZUL,defaultFont)
    etiquetaAcercaDe = EtiquetaDelTexto("Acerca De:",1,COLOR_AZUL,defaultFont)

    #Dibuja los textos
    screen.blit(etiquetaJugar,(REC3_X1+REC3_X12//2-etiquetaJugar.get_width()//2 , REC3_Y1+REC3_Y12//2-etiquetaJugar.get_height()//2))
    screen.blit(etiquetaSalir,(REC4_X1+REC4_X12//2-etiquetaSalir.get_width()//2 , REC4_Y1+REC4_Y12//2-etiquetaSalir.get_height()//2))
    screen.blit(etiquetaAcercaDe,(REC5_X1+REC5_X12//2-etiquetaAcercaDe.get_width()//2 , REC5_Y1+REC5_Y12//2-etiquetaAcercaDe.get_height()//2))

#Ultima funcion dibujar
def dibujarFinal(screen,gano,palabraCorrecta,intentos,segundos):

    #Dibuja las figuras
    #rectangulo reiniciar
    REC1 = pygame.Rect(REC1_X1,REC1_Y1, REC1_X12, REC1_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC1,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC1,7,30)
    #rectangulo salir
    REC2 = pygame.Rect(REC2_X1,REC2_Y1, REC2_X12, REC2_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC2,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC2,7,30)
    #rectangulo menu
    REC8 = pygame.Rect(REC8_X1,REC8_Y1, REC8_X12, REC8_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC8,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC8,7,30)
    #rectangulo guardar
    REC9 = pygame.Rect(REC9_X1,REC9_Y1, REC9_X12, REC9_Y12)
    pygame.draw.rect(screen,COLOR_ROJO,REC9,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC9,7,30)   

    #Valores base de los textos
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 40)
    etiquetaReiniciar = EtiquetaDelTexto("Reiniciar",1,COLOR_AZUL,defaultFont)
    etiquetaSalir = EtiquetaDelTexto("Salir",1,COLOR_AZUL,defaultFont)
    etiquetaMenu = EtiquetaDelTexto("Menu",1,COLOR_AZUL,defaultFont)
    etiquetaGuardar = EtiquetaDelTexto("Guardar",1,COLOR_AZUL,defaultFont)

    #Dibuja los textos
    screen.blit(etiquetaReiniciar,(REC1_X1+REC1_X12//2-etiquetaReiniciar.get_width()//2 , REC1_Y1+REC1_Y12//2-etiquetaReiniciar.get_height()//2))
    screen.blit(etiquetaSalir,(REC2_X1+REC2_X12//2-etiquetaSalir.get_width()//2 , REC2_Y1+REC2_Y12//2-etiquetaSalir.get_height()//2))
    screen.blit(etiquetaMenu,(REC8_X1+REC8_X12//2-etiquetaMenu.get_width()//2 , REC8_Y1+REC8_Y12//2-etiquetaMenu.get_height()//2))
    screen.blit(etiquetaGuardar,(REC9_X1+REC9_X12//2-etiquetaGuardar.get_width()//2 , REC9_Y1+REC9_Y12//2-etiquetaGuardar.get_height()//2))
   
    #Intruduce el texto final#
    finalFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_FINAL)
    if gano:
        #valor base de el texto
        textoFinal = "Felicidades, Has ganado"
        etiqueta = EtiquetaDelTexto(textoFinal, 1 , COLOR_BLANCO,finalFont)
        #Dibuja el texto
        mostrarTexto(screen,CENTRO_PANTALLA_X,200,etiqueta)
        
    elif intentos==0 or segundos<0.1:
        #valores base de los textos
        textoFinal = "Lo siento, has perdido"
        textoPalabraCorrecta = "La palabra correcta es: "+str(palabraCorrecta)
        #Dibuja los textos
        mostrarTexto(screen,CENTRO_PANTALLA_X,200,EtiquetaDelTexto(textoFinal, 1 , COLOR_BLANCO,finalFont))
        mostrarTexto(screen,CENTRO_PANTALLA_X,260,EtiquetaDelTexto(textoPalabraCorrecta, 1 , COLOR_BLANCO,FuenteDelTexto(TAMANNO_LETRA)))

#funcion dibujar en el juego
def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
                correctas, incorrectas, casi, error, palabraCorrecta, intentos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra la longitud de la palabra
    screen.blit(defaultFont.render("Letras: " +str(len(palabraCorrecta)), 1 , COLOR_TEXTO), (690, 50))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 80 * pos))
        pos += 1

    #muestra el abcdario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            #Cambia el color de las letras
            color = cambiarColorLetra(letra,correctas,casi,incorrectas)
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA
    
    #Detecta los tipos de errores
    if error=="logitud erronea":
        textoError = "La longitud de la palabra introducida no es la correcta"
    elif error=="palabra desconocida":
        textoError = "La palabra introducida no se encuentra en el juego"
    elif error=="ya ingresada":
        textoError = "No puedes repetir las palabras"
    else:
        textoError = ""

    #Imprime el texto de error
    mostrarTexto(screen,CENTRO_PANTALLA_X,ALTO-100 ,EtiquetaDelTexto(textoError,1,COLOR_TEXTO, FuenteDelTexto(TAMANNO_LETRA)))
    
    
def dibujarGuardar(screen,nombre):
    REC10 = pygame.Rect(REC10_X1,REC10_Y1, REC10_X12, REC10_Y12)  
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 40)  
    pygame.draw.rect(screen,COLOR_ROJO,REC10,0,30)
    pygame.draw.rect(screen,COLOR_GRIS_OSCURO,REC10,7,30)
    etiquetaSalir = EtiquetaDelTexto("Salir",1,COLOR_AZUL,defaultFont)  
    screen.blit(etiquetaSalir,(REC10_X1+REC10_X12//2-etiquetaSalir.get_width()//2 , REC10_Y1+REC10_Y12//2-etiquetaSalir.get_height()//2))  
        #Limpia la pantalla        
    textoFinal = "INGRESA TU NOMBRE"
    mostrarTexto(screen,CENTRO_PANTALLA_X,ALTO-100 ,EtiquetaDelTexto(textoFinal,1,COLOR_TEXTO, FuenteDelTexto(TAMANNO_LETRA)))
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    etiquetaNombre = defaultFont.render(nombre, 1, COLOR_TEXTO)
    screen.blit(etiquetaNombre, (CENTRO_PANTALLA_X-etiquetaNombre.get_width()//2, 550))

    pos = 0
    for nick,puntos in devoluciones10():
        screen.blit(defaultFont.render(nick, 1, COLOR_LETRAS), (50,20+ 40 * pos))
        screen.blit(defaultFont.render(str(puntos), 1, COLOR_LETRAS), (500,20+40 * pos))
        pos += 1
        






    





