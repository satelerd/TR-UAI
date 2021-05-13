import pygame
import time

pygame.init()

# Historia
historia = "daniel matias"


# Window
size = width, height = 1100, 700
win = pygame.display.set_mode(size)
pygame.display.set_caption("TypeRacer")


# Funciones
# Ocupa una letra incorrecta
def letraIncorrecta():
    print("Incorrecto")

# Ocupa la letra correcta
def letraCorrecta():
    print("Correcto")


run = True
contador = 0
while run:
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

    
    
    # inicioJuego(keys)


pygame.quit()