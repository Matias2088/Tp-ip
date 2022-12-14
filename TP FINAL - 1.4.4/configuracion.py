
FPS_inicial = 3

#Tamannos de Letras
TAMANNO_LETRA = 20
TAMANNO_LETRA_GRANDE = 70
TAMANNO_LETRA_FINAL = 50
TIEMPO_BASE = 120

#Largo de las palabras
LARGO = 5

#Posiciones de pantalla
ANCHO = 800
ALTO = 600
CENTRO_PANTALLA_X = ANCHO//2
CENTRO_PANTALLA_Y = ALTO//2

#Colores
COLOR_LETRAS = (20,200,20)
COLOR_FONDO = (0,0,0)
COLOR_TEXTO = (200,200,200)
COLOR_TIEMPO_FINAL = (200,20,10)
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (250,10,10)
COLOR_AMARILLO = (250,250,10)
COLOR_VERDE = (10,250,10)
COLOR_FINAL = (50,50,250)
COLOR_GRIS_OSCURO = (80,80,80)

#valores figuras
#rectangulo Reiniciar
REC1_X1 = CENTRO_PANTALLA_X-270
REC1_X2 = REC1_X1 + 200
REC1_X12 = REC1_X2-REC1_X1
REC1_Y1 = CENTRO_PANTALLA_Y
REC1_Y2 = REC1_Y1 + 70
REC1_Y12 = REC1_Y2-REC1_Y1

#rectangulo SalirFinal
REC2_X1 = REC1_X1
REC2_X2 = REC2_X1 + 200
REC2_X12 = REC2_X2 - REC2_X1
REC2_Y1 = REC1_Y2 + 50
REC2_Y2 = REC2_Y1 + 70
REC2_Y12 = REC2_Y2 - REC2_Y1

#rectangulo Menu
REC8_X1 = CENTRO_PANTALLA_X+70
REC8_X2 = REC8_X1 + 200
REC8_X12 = REC8_X2 - REC8_X1
REC8_Y1 = REC1_Y1 
REC8_Y2 = REC8_Y1 + 70
REC8_Y12 = REC8_Y2 - REC8_Y1

#rectangulo GUARDAR
REC9_X1 = CENTRO_PANTALLA_X+70
REC9_X2 = REC9_X1 + 200
REC9_X12 = REC9_X2 - REC9_X1
REC9_Y1 = REC1_Y2 + 50
REC9_Y2 = REC9_Y1 + 70
REC9_Y12 = REC9_Y2 - REC9_Y1

#rectangulo Jugar
REC3_X1 = CENTRO_PANTALLA_X-130
REC3_X2 = REC3_X1 + 260
REC3_X12 = REC3_X2-REC3_X1
REC3_Y1 = 30
REC3_Y2 = REC3_Y1 + 70
REC3_Y12 = REC3_Y2-REC3_Y1

#rectangulo SalirInicio
REC4_X1 = REC3_X1
REC4_X2 = REC3_X2
REC4_X12 = REC4_X2-REC4_X1
REC4_Y1 = CENTRO_PANTALLA_Y+100
REC4_Y2 = REC4_Y1 + 70
REC4_Y12 = REC4_Y2-REC4_Y1

#rectangulo AcercaDe:
REC5_X1 = REC3_X1
REC5_X2 = REC3_X2
REC5_X12 = REC5_X2-REC5_X1
REC5_Y1 = CENTRO_PANTALLA_Y
REC5_Y2 = REC5_Y1 + 50
REC5_Y12 = REC4_Y2-REC4_Y1

#Linea dificultad
REC6_X1 = CENTRO_PANTALLA_X-255
REC6_X2 = REC6_X1 + 510
REC6_X12 = REC6_X2 - REC6_X1
REC6_Y1 = REC3_Y2 + 50
REC6_Y2 = REC6_Y1 + 15
REC6_Y12 = REC6_Y2 - REC6_Y1

#Separadores de difucultad
LINEAS_DIFICULTAD_X = []
for x in range(REC6_X1+15,REC6_X2+1,(REC6_X12-30)//3):
    LINEAS_DIFICULTAD_X.append(x)

#Figura movil "scrol"
REC7_Y1 = REC6_Y1 - 20
REC7_Y2 = REC7_Y1 + 55
REC7_Y12 = REC7_Y2 - REC7_Y1

#rectangulo SalirGuardar
REC10_X1 = CENTRO_PANTALLA_X-100
REC10_X2 = REC10_X1 + 200
REC10_X12 = REC10_X2 - REC10_X1
REC10_Y1 = CENTRO_PANTALLA_Y+100
REC10_Y2 = REC10_Y1 + 70
REC10_Y12 = REC10_Y2 - REC10_Y1
