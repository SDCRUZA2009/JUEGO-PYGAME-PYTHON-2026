import pygame
import constantes
from personaje import Player
from weapon import Weapon 
import os


#FUNCIONES:
#ESCALAR IMAGENES
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#FUNCION PARA CONTAR ELEMENTOS
def count_elements(directory):
    return len(os.listdir(directory))
#print(count_elements("assets//images//characters//enemies"))
#print(os.listdir("assets//images//characters//enemies"))

#FUNCION LISTAR NOMBRES ELEMENTOS
def name_files(directory):
    return os.listdir(directory)
#print(name_file("assets//images//characters//enemies"))


pygame.init()

window = pygame.display.set_mode((constantes.WIDTH_WINDOW, 
                                   constantes.HEIGHT_WINDOW))
pygame.display.set_caption("Mi Juego")

#importar imagenes
#Personaje
animations = []
for i in range (4):
    img = player_image = pygame.image.load(f"assets//images//characters//player//Player_{i}.png").convert_alpha()
    img = escalar_img(img, constantes.SCALA_PLAYER)
    animations.append(img)

#enemigos
directory_enemies = "assets//images//characters//enemies"
type_enemies = name_files(directory_enemies)
#print(f"enemies: {type_enemies}")
animations_enemies = {}
for eni in type_enemies:
    list_temp = []
    rout_temp = f"assets//images//characters//enemies//{eni}"
    print(f"archivos reales en {eni}: {os.listdir(rout_temp)}")
    archivos = os.listdir(rout_temp)
    imagenes = [f for f in archivos if f.endswith(".png") or f.endswith(".jpg")]
    #print(animations_enemies)
    try:
        imagenes.sort(key=lambda f: int("".join(filter(str.isdigit, f)) or 0))
    except Exception:
        imagenes.sort()
    for nombre_archivo in imagenes:
        ruta_completa = os.path.join(rout_temp, nombre_archivo)
        img_enemie = pygame.image.load(ruta_completa).convert_alpha()
        img_enemie = escalar_img(img_enemie, constantes.SCALA_ENEMIES)
        list_temp.append(img_enemie)
    
    animations_enemies[eni] = list_temp
#arma
image_gun = pygame.image.load(f"assets//images//weapons//gun.png").convert_alpha()
image_gun = escalar_img(image_gun, constantes.SCALA_GUN)

#balas
image_bullet = pygame.image.load(f"assets//images//weapons//Bullet.png").convert_alpha()
image_bullet = escalar_img(image_bullet, constantes.SCALA_GUN)

#crear un jugador de la clase personaje
player = Player(40, 40, animations, 100)

#crear un enemigo de la clase personaje
the_dark_soul= Player(150, 200, animations_enemies["the_dark_soul"], 100)
skeleton_blue= Player(100, 200, animations_enemies["skeleton_blue"], 100)
golem_blue = Player(200, 200, animations_enemies["golem_blue"], 100)
golem_verde = Player(250, 200, animations_enemies["golem_verde"], 100)
golem_cafe= Player(300, 200, animations_enemies["golem_cafe"], 100)

#CRER LISTA DE ENEMIGOS
list_enemies = []
list_enemies.append(the_dark_soul)
list_enemies.append(skeleton_blue)
list_enemies.append(golem_blue)
list_enemies.append(golem_verde)
list_enemies.append(golem_cafe)
#print(list_enemies)

#crear un arma de la clase weapon
gun = Weapon(image_gun, image_bullet)

#crear un grupo de sprites
group_bullet = pygame.sprite.Group()

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

    #actualizar el estdo del enemigo
    for ene in list_enemies:
        ene.update()
        print(ene.energy)

    #actualizar el estado del arma
    bullet = gun.update(player)
    if bullet:
        group_bullet.add(bullet)
    for bullet in group_bullet:
        bullet.update(list_enemies)
    #print(group_bullet)

    #dibujar el jugador
    player.draw(window)

    #dibujar a los enemigos
    for ene in list_enemies:
        ene.draw(window)

    #dibujar el arma
    gun.draw(window)

    #dibujar las balas
    for bullet in group_bullet:
        bullet.draw(window)

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
