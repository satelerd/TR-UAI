from sys import winver
import pygame
import time
import random


pygame.font.init()
FONT = pygame.font.SysFont("Sans", 40)
historiaFONT = pygame.font.SysFont("Sans", 24)
pygame.init()

# Historia UAI
historiaa = [
    [
        "habia una vez un alumno nuevo de la uai, desde su primer dia hasta el ultimo",
        " nunca logro descubrir el mundo de la universidad, hizo todos sus años online."
    ],
    [
        "hay cosas muy grandes a lo largo del planeta tierra, como el empire state,",
        " chayanne o boquita... pero nada superara a los pumas ingenieros."
    ],
    [
        "el puma camina sabiamente por lo desconocido, guiado por su inteligencia.",
        " se le ve muy fresco gracias al conocimiento que le dio core."
    ],
    [
        "si bien vivimos en lo desconocido y muchas veces en diferencias,",
        " esta clarisimo que el campus de viña es mucho mas bonito."
    ],
    [
        "vivir en marte no va a ser facil.",
        " la unica razon para que los humanos vayan al espacio seria la aventura."
    ],
    [
        "la ciencia descubre las verdades esenciales sobre lo que existe en lo desconocido,",
        " la ingenieria consiste en crear cosas que nunca existieron."
    ]
]

randomInt = random.randint(0,len(historiaa) - 1)

# Colores
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLACK = (75,75,75)
GREEN = (0,128,1)
RED = (255,0,0)

# Window
size = width, height = int(1100 - 1100*0.2), 600
win = pygame.display.set_mode(size)
pygame.display.set_caption("TypeRacer")

# HUD
try:
    print("try")
    bg = pygame.image.load("stars_bg.jpg")
except:
    print("excep´t")
    bg = BLACK


button = pygame.Rect(width*0.05, height*0.75, 150, 90)  

def draw_window(palabra, colorLetra, fraseBuena, tiempoTotal, ppm):
    if bg == BLACK:
        win.fill(bg)
    else:
        win.blit(bg, (0, 0))


    
    # Derecha del win cuadrado (typeracer)
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(0, 0, 10, height))
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(0, 0, width, 10))
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(width-10, 0, 10, height))
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(0, height-10, width, 10))

    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(0, height*0.3, width, 10))
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(0, height*0.6, width, 10))

    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.03, height*0.45, 835, 90))

    # Historia arriba
    titulo = FONT.render("Texto que deberás typear:",1,WHITE)
    win.blit(titulo, (width*0.02, height*0.02, 100, 100))
    historiaTexto = historiaFONT.render(historiaa[randomInt][0],1,WHITE)
    win.blit(historiaTexto, (width*0.02+5, height*0.13, 100, 100))
    historiaTexto2 = historiaFONT.render(historiaa[randomInt][1],1,WHITE)
    win.blit(historiaTexto2, (width*0.02, height*0.13 + 40, 100, 100))

    # Historia medio
    titulo2 = FONT.render("Frase actual:",1,WHITE)
    win.blit(titulo2, (width*0.02, height*0.325, 100, 100))
    historiaBueno = historiaFONT.render(fraseBuena, 1, WHITE)
    win.blit(historiaBueno, (width*0.037, height*0.45, 100, 100))
    historiaEscrito = historiaFONT.render(palabra+"|",1,colorLetra)
    win.blit(historiaEscrito, (width*0.037, height*0.45+50, 100, 100))

    textInput = pygame.Rect(width*0.03, height*0.45+50, 835, 30) 
    pygame.draw.rect(win,colorLetra, textInput,3)

    # Abajo (boton y resultado)
    # Boton
    botonTexto = FONT.render("Jugar", 1, WHITE)
    win.blit(botonTexto, (width*0.09, height*0.78))
    pygame.draw.rect(win, WHITE, button,5)

    #timer
    pygame.draw.rect(win, LIGHTBLACK, pygame.Rect(width*0.4, height*0.6, 10, height))

    # Puntaje
    puntajeTitulo = FONT.render("Resultados",1,WHITE)
    win.blit(puntajeTitulo, (width*0.425, height*0.64))

    if termino:
        tiempoTexto = FONT.render(tiempoTotal+ " segundos",1,WHITE)
        win.blit(tiempoTexto, (width*0.475, height*0.76))
        ppmTexto = FONT.render(str(ppm)+ " ppm",1,WHITE)
        win.blit(ppmTexto, (width*0.475, height*0.85))

    pygame.display.update()

# Timer
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)

        timerBlock = pygame.Rect(width*0.27 - 10, height*0.78, 100, 50) 
        pygame.draw.rect(win, BLACK, timerBlock)
        timerTexto = FONT.render("t-"+ timer+" s",1,WHITE)
        win.blit(timerTexto, (width*0.27, height*0.78))
        pygame.display.update()

        time.sleep(1)
        t -= 1

    return time.time()


primeraRun = True
palabra = ""
fraseBuena = ""
historiaFrase = historiaa[randomInt][0]
colorLetra = WHITE
contador = 0
contadorHistoria = 0
contadorPalabras = 0
tiempoTotal = 0
ppm = 0
FPS = 60
correcto = True
run = True
comenzar = False
termino = False
clock = pygame.time.Clock()

# GAME LOOP
while run:
    clock.tick(FPS)
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()

    # Loop de eventos
    for event in pygame.event.get():
        # Salir
        if event.type == pygame.QUIT:
            run = False

        #Apreta el boton del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if button.collidepoint(mouse_pos):
                    if not primeraRun:
                        randomInt = random.randint(0,len(historiaa) - 1)
                    primeraRun = False
                    palabra = ""
                    fraseBuena = ""
                    historiaFrase = historiaa[randomInt][0]
                    colorLetra = WHITE
                    contador = 0
                    contadorHistoria = 0
                    contadorPalabras = 0
                    tiempoTotal = 0
                    ppm = 0
                    FPS = 60
                    correcto = True
                    run = True
                    comenzar = False
                    termino = False
                    clock = pygame.time.Clock()
                    comenzar = True
                    fraseBuena = historiaFrase
                    tiempoEmpieza = countdown(3)
                    break

        # Levanto una tecla
        if event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)

            if tecla == "return":
                tecla = " "
            elif tecla == "space":
                tecla = " "
            elif tecla == ";":
                tecla = "ñ"
            elif len(tecla)>1 and tecla != "backspace":
                # print(tecla)
                break

            # Si dio a start, Comienza el juego
            if comenzar:
                # Pasar de historia a h2 a h3...
                if contador == len(historiaFrase):
                    # if palabra != fraseBuena[0:len(palabra)]:
                    #     print("entramos aqui")
                    #     contador -= 1
                    #     break
                    # if not correcto:
                    #     contador -= 1
                    #     break

                    contador = 0
                    contadorHistoria += 1

                    if contadorHistoria == 1:
                        historiaFrase = historiaa[randomInt][1]

                    elif contadorHistoria == 2:
                        tiempoTermina = time.time()
                        tiempoTotal = tiempoTermina-tiempoEmpieza
                        for letter in historiaa[randomInt][0]:
                            if letter == " ":
                                contadorPalabras += 1
                        for letter in historiaa[randomInt][1]:
                            if letter == " ":
                                contadorPalabras += 1
                        ppm = str(contadorPalabras/(tiempoTotal/60))[:5]
                        tiempoTotal = str(tiempoTotal)[:5]

                        contadorHistoria = 0
                        comenzar = False
                        termino = True
                        break

                    palabra = ""
                    fraseBuena = ""
                
                fraseBuena = historiaFrase

                if palabra == fraseBuena[0:len(palabra)]:
                    correcto = True
                else:
                    correcto = False

                # Correcto
                if tecla == historiaFrase[contador].lower():
                    if correcto:
                        palabra += tecla
                        colorLetra = WHITE
                    else:
                        palabra += tecla
                        colorLetra = RED

                # elif "tecla pa atras hay q cont -= 1"
                elif tecla == "backspace":
                    # fraseBuena = fraseBuena[:-2]
                    contador -= 1
                    palabra = palabra[:-1]
                    continue

                # Incorrecto
                else:
                    palabra += tecla
                    colorLetra = RED

                contador += 1
        
        
    
    draw_window(palabra, colorLetra, fraseBuena, tiempoTotal, ppm)
    
pygame.quit()