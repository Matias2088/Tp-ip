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
    """hay 2 formas de hacer todo esto, Una corta utilizando una funcion ya creada.
    Y otra sin utilizar funciones, pero mas facil de entender   """
    #forma 1
    """renderTextoError = defaultFont.render(textoError,1,COLOR_TEXTO)
    screen.blit(renderTextoError, (( CENTRO_PANTALLA_X - renderTextoError.get_width()//2 ),ALTO-100))"""
    #forma 2
    mostrarTexto(screen,textoError,1,COLOR_TEXTO,CENTRO_PANTALLA_X,ALTO-100,TAMANNO_LETRA)  

    #Intruduce el texto final#

    #hay 2 formas de hacer todo esto, Una corta utilizando una funcion ya creada.
    #Y otra sin utilizar funciones, pero mas facil de entender
    finalFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_TEXTO_FINAL)
    if gano:        
        screen.fill(COLOR_FONDO)
        textoFinal = "Felicidades, Has ganado"
        #Forma 1
        mostrarTexto(screen,textoFinal,1,COLOR_FINAL,CENTRO_PANTALLA_X,250,TAMANNO_TEXTO_FINAL)
        #Forma 2
        """textoFinal = "Felicidades, Has ganado"
        EtiquetaDelTexto = finalFont.render(textoFinal,1,COLOR_FINAL)
        screen.blit(EtiquetaDelTexto, ((CENTRO_PANTALLA_X - EtiquetaDelTexto.get_width()//2),250))"""
    elif intentos==0:
        screen.fill(COLOR_FONDO)
        textoFinal = "Lo siento, has perdido"
        textoPalabraCorrecta = "La palabra correcta es: "+str(palabraCorrecta)
        #Forma 1
        mostrarTexto(screen,textoFinal,1,COLOR_FINAL,CENTRO_PANTALLA_X,250,TAMANNO_TEXTO_FINAL)
        
        mostrarTexto(screen,textoPalabraCorrecta,1,COLOR_FINAL,CENTRO_PANTALLA_X,300,TAMANNO_LETRA)
        #Forma 2
        """EtiquetaDelTexto = finalFont.render(textoFinal,1,COLOR_FINAL)
        screen.blit(EtiquetaDelTexto, ((CENTRO_PANTALLA_X - EtiquetaDelTexto.get_width()//2),250))
        
        textoPalabraCorrecta = "La palabra correcta es: "+str(palabraCorrecta)
        EtiquetaDeLaPalabraCorrecta = defaultFont.render(textoPalabraCorrecta,1,COLOR_FINAL)
        screen.blit(EtiquetaDeLaPalabraCorrecta, ((CENTRO_PANTALLA_X - EtiquetaDeLaPalabraCorrecta.get_width()//2),300))"""        
  
          
    """
    Para que entiendan, para escribir texto en pantalla utilice lo siguiente:

    #Tipo y tamaño de letra
    FuenteDelTexto = pygame.font.Font( NombreDeLaFuente , TamañoDeLaFuente )
    #Frase y sus caracteristicas
    EtiquetaDelTexto = FuenteDelTexto.render( texto , tipoDeRenderizado , ColorDelTexto )  ----- tipoDeRenderizado, siempre es mejor 1
    ###--Esto es lo que escribe en pantalla--###
    screen.blit( EtiquetaDelTexto, ( coordenadaX - EtiquetaDeLaPalabraCorrecta.get_width()//2, coordenadaY )) 
    ---EtiquetaDeLaPalabraCorrecta.get_width()//2 ---centra la frase en la coordenada indicada a su izquierda
    """




    








