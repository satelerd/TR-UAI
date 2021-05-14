import pygame
import time

pygame.font.init()
FONT = pygame.font.SysFont("Sans", 40)
historiaFONT = pygame.font.SysFont("Sans", 20)
pygame.init()

# Historia
historia = "En el hotel había noventa y siete agentes de publicidad neoyorquinos." 
historiaPalabras = ["En","el","hotel","había","noventa","y","siete","agentes","de","publicidad","neoyoruinos."]
historia2 = "Como monopolizaban las líneas telefónicas de larga distancia,"
historia3 = "la chica del 507 tuvo que esperar su llamada desde el mediodía hasta las dos y media de la tarde." 
historia4 = "Pero no perdió el tiempo. En una revista femenina leyó un artículo titulado" 
historia5= "«El sexo es divertido o infernal». Lavó su peine y su cepillo. Quitó una mancha de la falda de su traje beige. Corrió un poco el botón de la blusa de Saks. Se arrancó los dos pelos que acababan de salirle en el lunar. Cuando, por fin, la operadora la llamó, estaba sentada en el alféizar de la ventana y casi había terminado de pintarse las uñas de la mano izquierda. No era una chica a la que una llamada telefónica le produjera gran efecto. Se comportaba como si el teléfono hubiera estado sonando constantemente desde que alcanzó la pubertad. "

# Window
size = width, height = 1100, 700
win = pygame.display.set_mode(size)
pygame.display.set_caption("TypeRacer")

FPS = 60

# Colores
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,143,57)
RED = (255,0,0)

# HUD
win.fill(WHITE)
def draw_window(palabra, colorLetra):
    # Izquierda (nombre y marcador)
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, 0, 10, height))
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, 0, width*0.25, 10))
    pygame.draw.rect(win, (BLACK), pygame.Rect(width*0.25, 0, 10, height)) 
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, height-10, width*0.25, 10))

    pygame.draw.rect(win, (BLACK), pygame.Rect(0, height*0.3, width*0.25, 10))


    nombreTexto = FONT.render("Nombre:", 1, BLACK)
    win.blit(nombreTexto, (width*0.01,30))

    marcadorTexto = FONT.render("Marcador:",1,BLACK)
    win.blit(marcadorTexto, (width*0.01, height*0.3 + 30))

    
    # Derecha cuadrado (typeracer)
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, 0, 10, height))
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, 0, width, 10))
    pygame.draw.rect(win, BLACK, pygame.Rect(width-10, 0, 10, height))
    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, height-10, width, 10))

    pygame.draw.rect(win, BLACK, pygame.Rect(width*0.3, height*0.3, width, 10))

    # Historia arriba
    historiaTexto = historiaFONT.render(historia,1,BLACK)
    win.blit(historiaTexto, (width*0.32, height*0.05, 100, 100))
    historiaTexto2 = historiaFONT.render(historia2,1,BLACK)
    win.blit(historiaTexto2, (width*0.32, height*0.05 + 25*1, 100, 100))
    historiaTexto3 = historiaFONT.render(historia3,1,BLACK)
    win.blit(historiaTexto3, (width*0.32, height*0.05 + 25*2, 100, 100))
    historiaTexto4 = historiaFONT.render(historia4,1,BLACK)
    win.blit(historiaTexto4, (width*0.32, height*0.05 + 25*3, 100, 100))
    historiaTexto5 = historiaFONT.render(historia5,1,BLACK)
    win.blit(historiaTexto5, (width*0.32, height*0.05 + 25*4, 100, 100))

    # Historia medio
    historiaEscrito = historiaFONT.render( palabra ,1,colorLetra)
    win.blit(historiaEscrito, (width*0.32, height*0.05 + 25*8, 100, 100))



    pygame.display.update()


# Funciones
# Ocupa la letra correcta
def letraCorrecta():

    print("Correcto")
    

    # escribe palabra, y pon q se vea de color verde

# Ocupa una letra incorrecta
def letraIncorrecta():
    print("Incorrecto")
    # escribe palabra, y pon que se vea de color rojo


palabra = ""
colorLetra = RED
contador = 0
correcto = True
run = True
clock = pygame.time.Clock()


while run:
    clock.tick(FPS)
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()

    # Loop de eventos
    for event in pygame.event.get():

        # Levanto una tecla
        if event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)
            print()
            print("historia[contador], tecla")
            print(historia[contador],"                    ", tecla)

            # Correcto
            if tecla == historia[contador].lower():
                if correcto:
                    palabra += tecla
                    print("palabra: ",palabra)
                    colorLetra = GREEN
                    letraCorrecta()
                else:
                    palabra += tecla
                    print("palabra: ",palabra)
                    colorLetra = GREEN
                    letraCorrecta()
                    # deberia ser letraIncorrecta()

            # Espacio
            elif tecla == "space" and historia[contador] == " ":
                correcto = True
                palabra += historia[contador]
                print("palabra: ",palabra)
                letraCorrecta()

            # elif "tecla pa atras hay q cont -= 1"

            # Incorrecto
            else:
                palabra += tecla
                colorLetra = RED
                print("palabra: ",palabra)
                letraIncorrecta()

            contador += 1
            
        

        # Salir
        if event.type == pygame.QUIT:
            run = False
    
    draw_window(palabra,colorLetra)
    


pygame.quit()