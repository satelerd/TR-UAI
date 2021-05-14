import pygame
import time

pygame.init()

# Historia
historia = "daniel matias"

# Window
size = width, height = 1100, 700
win = pygame.display.set_mode(size)
pygame.display.set_caption("TypeRacer")

FPS = 60

# Colores
WHITE = (255,255,255)
BLACK = (0,0,0)

# HUD
def draw_window():
    win.fill(WHITE)
    pygame.draw.rect(win, (BLACK), pygame.Rect(0, 0, 300, height))
    pygame.display.update()


# Funciones
# Ocupa una letra incorrecta
def letraIncorrecta():
    print("Incorrecto")

# Ocupa la letra correcta
def letraCorrecta():
    print("Correcto")

clock = pygame.time.Clock()
run = True
contador = 0
while run:
    clock.tick(FPS)
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()
    # Loop de eventos
    for event in pygame.event.get():
        # Levanto una tecla
        if event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)
            print(historia[contador], tecla)
            contador += 1
            
        

        # Salir
        if event.type == pygame.QUIT:
            run = False
    
    draw_window()
    


pygame.quit()