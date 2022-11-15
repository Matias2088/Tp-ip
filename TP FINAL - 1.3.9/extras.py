import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

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
            color = cambiarColorLetra(letra,correctas,casi,incorrectas)
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA
    
    #Detecta errores e imprime en la pantalla su tipo
    if error=="logitud erronea":
        textoError = "La longitud de la palabra introducida no es la correcta"
    elif error=="palabra desconocida":
        textoError = "La palabra introducida no se encuentra en el diccionario"
    else:
        textoError = ""

    mostrarTexto(screen,CENTRO_PANTALLA_X,ALTO-100 ,EtiquetaDelTexto(textoError,1,COLOR_TEXTO, FuenteDelTexto(TAMANNO_LETRA)))

    #Intruduce el texto final#
    finalFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_FINAL)
    if gano:
        #Limpia la pantalla        
        screen.fill(COLOR_FONDO)
        textoFinal = "Felicidades, Has ganado"
        #Opcion 2
        fuente = FuenteDelTexto(TAMANNO_LETRA_FINAL)
        etiqueta = EtiquetaDelTexto(textoFinal, 1 , COLOR_FINAL,fuente)
        mostrarTexto(screen,CENTRO_PANTALLA_X,250,etiqueta)

    elif intentos==0 or segundos<0.1:
        #Limpia la pantalla        
        screen.fill(COLOR_FONDO)
        textoFinal = "Lo siento, has perdido"
        textoPalabraCorrecta = "La palabra correcta es: "+str(palabraCorrecta)
        #Opcion 1
        mostrarTexto(screen,CENTRO_PANTALLA_X,250,EtiquetaDelTexto(textoFinal, 1 , COLOR_FINAL,FuenteDelTexto(TAMANNO_LETRA_FINAL)))
        
        mostrarTexto(screen,CENTRO_PANTALLA_X,310,EtiquetaDelTexto(textoPalabraCorrecta, 1 , COLOR_FINAL,FuenteDelTexto(TAMANNO_LETRA)))




    





