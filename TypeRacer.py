import pygame

pygame.font.init()
FONT = pygame.font.SysFont("Sans", 40)
historiaFONT = pygame.font.SysFont("Sans", 20)
pygame.init()

# Historia aaa
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
def draw_window(palabra, colorLetra, fraseBuena):
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
    historiaTexto = historiaFONT.render(historia,1,BLACK)
    win.blit(historiaTexto, (width*0.32+5, height*0.09, 100, 100))
    historiaTexto2 = historiaFONT.render(historia2,1,BLACK)
    win.blit(historiaTexto2, (width*0.32, height*0.09 + 25*1, 100, 100))
    historiaTexto3 = historiaFONT.render(historia3,1,BLACK)
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

    textInput = pygame.Rect(width*0.33, height*0.05 +25*12, 650, 30) 
    pygame.draw.rect(win,colorLetra, textInput,3)

    # Abajo (boton y resultado)
    # Boton
    botonTexto = FONT.render("Jugar", 1, BLACK)
    win.blit(botonTexto, (width*0.39, height*0.78))
    pygame.draw.rect(win, [255, 0, 0], button,5)

    #timer
    timerTexto = FONT.render("t-0:00",1,BLACK)
    win.blit(timerTexto, (width*0.55, height*0.78))

    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.65, height*0.6, 10, height))

    # Puntaje
    puntajeTitulo = FONT.render("Puntaje",1,BLACK)
    win.blit(puntajeTitulo, (width*0.675, height*0.64))

    if termino:
        finalTexto = FONT.render("FIN",1,BLACK)
        win.blit(finalTexto, (width*0.675, height*0.78))

    pygame.display.update()


    # escribe palabra, y pon q se vea de color verde


palabra = ""
fraseBuena = ""
historiaFrase = historia
colorLetra = GREEN
contador = 0
contadorHistoria = 0
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
            elif len(tecla)>1 and tecla != "backspace":
                # print(tecla)
                break

            # Si dio a start, Comienza el juego
            if comenzar:
                # Pasar de historia a h2 a h3...
                if contador == len(historiaFrase):
                    # if not correcto:
                    #     contador -= 1
                    #     break

                    contador = 0
                    if contadorHistoria == 0:
                        historiaFrase = historia2
                    # elif contadorHistoria == 1:
                    #     historiaFrase = historia3
                    # elif contadorHistoria == 2:
                    #     historiaFrase = historia4
                    # elif contadorHistoria == 3:
                    #     historiaFrase = historia5
                    elif contadorHistoria == 1:
                        contadorHistoria = 0
                        comenzar = False
                        termino = True
                        print("FIIIIIIIIIIIIIIIIIIIIIIIN")
                        break
                    palabra = ""
                    fraseBuena = ""
                    contadorHistoria += 1


                fraseBuena = historiaFrase

                print()
                # print("frase buena: ", fraseBuena)
                # print("historia[contador], tecla")
                # print(historia[contador],"                    ", tecla)

                # Definir si esta bien o mal
                print()
                # print(palabra)
                # print(fraseBuena[0:contador])
                print
                if palabra == fraseBuena[0:contador]:
                    correcto = True
                else:
                    correcto = False

                # Correcto
                if tecla == historiaFrase[contador].lower():
                    if correcto:
                        palabra += tecla
                        colorLetra = GREEN
                        print("Correcto")
                    else:
                        palabra += tecla
                        colorLetra = RED
                        print("Incorrecto")
                        # deberia ser letraIncorrecta()

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
                    # print("palabra: ",palabra)
                    print("Incorrecto")

                contador += 1
        
        
    
    draw_window(palabra, colorLetra, fraseBuena)
    


pygame.quit()