import pygame
import time
import random

randomInt = random.randint(0,3)

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
        " chayane o boquita... pero nada superara a los pumas ingenieros."
    ],
    [
        "el puma camina sabiamente por lo desconocido, guiado por su inteligencia.",
        " se le ve muy fresco gracias al conocimiento que obtuvo en la uai."
    ],
    [
        "si bien vivimos en lo desconocido, aprendiendo constantemente,",
        " esta clarisimo que el campus de viña es mucho mas bonito"
    ]
]

# Historia
historia = "en el hotel habia noventa y siete agentes de publicidad neoyorquinos." 
historiaPalabras = ["en","el","hotel","habia","noventa","y","siete","agentes","de","publicidad","neoyoruinos."]
historia2 = " como monopolizaban las lineas telefonicas de larga distancia,"
historia3 = " la chica del 507 tuvo que esperar su llamada desde el mediodia hasta las dos y media de la tarde." 
historia4 = " pero no perdio el tiempo. En una revista femenina leyo un articulo titulado" 
historia5 = " el sexo es divertido o infernal. Lavo su peine y su cepillo."
historia6 = "quito una mancha de la falda de su traje beige. Corrio un poco el boton de la blusa de Saks. Se arranco los dos pelos que acababan de salirle en el lunar. Cuando, por fin, la operadora la llamó, estaba sentada en el alféizar de la ventana y casi había terminado de pintarse las uñas de la mano izquierda. No era una chica a la que una llamada telefónica le produjera gran efecto. Se comportaba como si el teléfono hubiera estado sonando constantemente desde que alcanzó la pubertad. "

# Colores
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,128,1)
RED = (255,0,0)

# Window
size = width, height = 1100, 700
win = pygame.display.set_mode(size)
pygame.display.set_caption("TypeRacer")

# HUD
button = pygame.Rect(width*0.35, height*0.75, 170, 90)  
win.fill(WHITE)
def draw_window(palabra, colorLetra, fraseBuena, tiempoTotal, ppm):
    win.fill(WHITE)

    # Izquierda del win (nombre y marcador)
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, 0, 10, height))
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, 0, width*0.25, 10))
    pygame.draw.rect(win, (BLACK), pygame.Rect(width*0.25, 0, 10, height)) 
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, height-10, width*0.25, 10))

    pygame.draw.rect(win, (BLACK), pygame.Rect(0, height*0.3, width*0.25, 10))


    nombreTexto = FONT.render("Nombre:", 1, BLACK)
    win.blit(nombreTexto, (width*0.01,30))

    marcadorTexto = FONT.render("Marcador:",1,BLACK)
    win.blit(marcadorTexto, (width*0.01, height*0.3 + 30))

    
    # Derecha del win cuadrado (typeracer)
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, 0, 10, height))
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, 0, width, 10))
    pygame.draw.rect(win, BLACK, pygame.Rect(width-10, 0, 10, height))
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, height-10, width, 10))

    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, height*0.3, width, 10))
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, height*0.6, width, 10))

    # Historia arriba
    titulo = FONT.render("Texto que deberás typear:",1,BLACK)
    win.blit(titulo, (width*0.32, height*0.02, 100, 100))
    historiaTexto = historiaFONT.render(historiaa[randomInt][0],1,BLACK)
    win.blit(historiaTexto, (width*0.32+5, height*0.09, 100, 100))
    historiaTexto2 = historiaFONT.render(historiaa[randomInt][1],1,BLACK)
    win.blit(historiaTexto2, (width*0.32, height*0.09 + 25*1, 100, 100))
    # historiaTexto3 = historiaFONT.render(historia3,1,BLACK)
    # win.blit(historiaTexto3, (width*0.32, height*0.09 + 25*2, 100, 100))
    # historiaTexto4 = historiaFONT.render(historia4,1,BLACK)
    # win.blit(historiaTexto4, (width*0.32, height*0.09 + 25*3, 100, 100))
    # historiaTexto5 = historiaFONT.render(historia5,1,BLACK)
    # win.blit(historiaTexto5, (width*0.32, height*0.09 + 25*4, 100, 100))

    # Historia medio
    titulo2 = FONT.render("Frase actual:",1,BLACK)
    win.blit(titulo2, (width*0.32, height*0.05 +25*7.5, 100, 100))
    historiaBueno = historiaFONT.render(fraseBuena, 1, BLACK)
    win.blit(historiaBueno, (width*0.337, height*0.05 + 25*10, 100, 100))
    historiaEscrito = historiaFONT.render(palabra+"|",1,colorLetra)
    win.blit(historiaEscrito, (width*0.337, height*0.05 + 25*12, 100, 100))

    textInput = pygame.Rect(width*0.33, height*0.05 +25*12, 680, 30) 
    pygame.draw.rect(win,colorLetra, textInput,3)

    # Abajo (boton y resultado)
    # Boton
    botonTexto = FONT.render("Jugar", 1, BLACK)
    win.blit(botonTexto, (width*0.39, height*0.78))
    pygame.draw.rect(win, [255, 0, 0], button,5)

    #timer
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.65, height*0.6, 10, height))

    # Puntaje
    puntajeTitulo = FONT.render("Resultados",1,BLACK)
    win.blit(puntajeTitulo, (width*0.675, height*0.64))

    if termino:
        tiempoTexto = FONT.render(tiempoTotal+ " segundos",1,BLACK)
        win.blit(tiempoTexto, (width*0.675, height*0.76))
        ppmTexto = FONT.render(str(ppm)+ " ppm",1,BLACK)
        win.blit(ppmTexto, (width*0.675, height*0.85))

    pygame.display.update()

# Timer
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)

        timerBlock = pygame.Rect(width*0.53, height*0.78, 100, 50) 
        pygame.draw.rect(win, WHITE, timerBlock)
        timerTexto = FONT.render("t-"+ timer+" s",1,BLACK)
        win.blit(timerTexto, (width*0.53, height*0.78))
        pygame.display.update()

        time.sleep(1)
        t -= 1

    return time.time()
    # seconds = 0
    # minutes = 0
    # termino = False
    # while not termino:

    #     timerBlock = pygame.Rect(width*0.53, height*0.78, 100, 50) 
    #     pygame.draw.rect(win, WHITE, timerBlock)
    #     timerTexto = FONT.render("t+"+ str(seconds) +" s",1,BLACK)
    #     win.blit(timerTexto, (width*0.53, height*0.78))
    #     pygame.display.update()

    #     time.sleep(1)
    #     seconds = int(time.time() - time_start) - minutes * 60
    #     if seconds >= 60:
    #         minutes += 1
    #         seconds = 0
        
    #     if seconds == 10:
    #         termino = True


palabra = ""
fraseBuena = ""
historiaFrase = historiaa[randomInt][0]
colorLetra = GREEN
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
                    # prints current location of mouse
                    # print('button was pressed at {0}'.format(mouse_pos))
                    comenzar = True
                    fraseBuena = historiaFrase
                    tiempoEmpieza = countdown(3)
                    break

        # Levanto una tecla
        if event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)

            if tecla == "return":
                comenzar = True
                fraseBuena = historiaFrase
                break
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

                    # if contadorHistoria == 0:
                    #     historiaFrase = historia2
                    # elif contadorHistoria == 1:
                    #     historiaFrase = historia3
                    # elif contadorHistoria == 2:
                    #     historiaFrase = historia4
                    # elif contadorHistoria == 3:
                    #     historiaFrase = historia5
                    # if contadorHistoria == 0:
                    #     tiempoTermina = time.time()
                    #     tiempoTotal = tiempoTermina-tiempoEmpieza
                    #     for letter in historiaFrase:
                    #         if letter == " ":
                    #             contadorPalabras += 1
                    #     ppm = str(contadorPalabras/(tiempoTotal/60))[:5]
                    #     tiempoTotal = str(tiempoTotal)[:5]

                        # contadorHistoria = 0
                        # comenzar = False
                        # termino = True
                        # break
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
                        colorLetra = GREEN
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