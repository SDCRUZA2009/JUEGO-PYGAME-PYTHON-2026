import pygame
import constantes
from personaje import Player
from weapon import Weapon 

pygame.init()

window = pygame.display.set_mode((constantes.WIDTH_WINDOW, 
                                   constantes.HEIGHT_WINDOW))
pygame.display.set_caption("Mi Juego")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#importar imagenes
#Personaje
animaciones = []
for i in range (4):
    img = player_image = pygame.image.load(f"assets//images//characters//player//Player_{i}.png").convert_alpha()
    img = escalar_img(img, constantes.SCALA_PLAYER)
    animaciones.append(img)

#arma
image_gun = pygame.image.load(f"assets//images//weapons//gun.png").convert_alpha()
image_gun = escalar_img(image_gun, constantes.SCALA_GUN)

#crear un jugador de la clase personaje
player = Player(40, 40, animaciones)

#crear un arma de la clase weapon
gun = Weapon(image_gun)

#definir las variables de movimiento del jugador
move_up = False
move_down = False
move_left = False
move_right = False

#CONTROLAR EL FRAME RATE
clock = pygame.time.Clock()

run = True
while run:
    
    #QUE VAYA A 60 FPS
    clock.tick(constantes.FPS)
    window.fill(constantes.COLOR_BG)

    #calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if move_right == True:
        delta_x = constantes.VELOCIDAD
    if move_left == True:
        delta_x = -constantes.VELOCIDAD
    if move_up == True:
        delta_y = -constantes.VELOCIDAD
    if move_down == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    player.move(delta_x, delta_y)

    #actualizar el estado del jugador
    player.update()

    #actualizar el estado del arma
    gun.update(player)

    #dibujar el jugador
    player.draw(window)

    #dibujar el arma
    gun.draw(window)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False

    pygame.display.update()

pygame.quit()
