

def mostrarTexto(texto,tipoDeRenderizado,ColorDelTexto,coordenadaX,coordenadaY,TamañoDeLaFuente,NombreDeLaFuente=pygame.font.get_default_font()):
    #Tipo y tamaño de letra
    FuenteDelTexto = pygame.font.Font( NombreDeLaFuente , TamañoDeLaFuente )
    #Frase y sus caracteristicas
    EtiquetaDelTexto = FuenteDelTexto.render( texto , tipoDeRenderizado , ColorDelTexto )
    ###--Esto es lo que escribe en pantalla--###
    screen.blit( EtiquetaDelTexto, ( coordenadaX, coordenadaY))



