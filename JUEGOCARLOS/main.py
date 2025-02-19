import pygame
import constantes
from personaje import Personaje

pygame.init()
ventana = pygame.display.set_mode((constantes.ALTO_VENTANA,
                                   constantes.ANCHO_VENTANA))
pygame.display.set_caption("Alien Breed")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size=(w*scale, h*scale))
    return nueva_imagen




player_image = pygame.image.load("assets/images/characters/player//personaje 1.png")
player_image=  escalar_img(player_image, constantes.SCALA_PERSONAJE)

jugador = Personaje(50,50, player_image)

#definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#controlar el frame rate
reloj = pygame.time.Clock()

run = True
while run == True:

    #que vaya a 60 FPS
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)


    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)



    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        #para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False


    pygame.display.update()


pygame.quit()