import pygame
import constantes
import math
import random

class Weapon():
    def __init__(self, image, image_bullet):
        self.image_bullet = image_bullet
        self.image_original = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.shape = self.image.get_rect()
        self.fired = False
        self.last_shoot = pygame.time.get_ticks()

    def update(self, Player):
        shoot_cooldown = constantes.SHOOT_COOLDOWN
        bullet = None
        self.shape.center = Player.shape.center

         #mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distance_x = mouse_pos[0] - self.shape.centerx
        distance_y = -(mouse_pos[1] - self.shape.centery)
        self.angle = math.degrees(math.atan2(distance_y, distance_x))

        if Player.flip == False:
            self.shape.x = self.shape.x + Player.shape.width /1.5
            self.shape.y = self.shape.y + Player.shape.height /6.5
            self.rotate_weapon(False)

            self.angle = max(-10, min(10, self.angle))
            self.rotate_weapon(False)

        if Player.flip == True:
            self.shape.x = self.shape.x - Player.shape.width /1.5
            self.shape.y = self.shape.y + Player.shape.height /6.5
            if self.angle > 0:
                self.angle = max(180 - 10, min(180 + 10, self.angle))
            else: 
                self.angle = max(-180 - 10, min(-180 + 10, self.angle))

            self.rotate_weapon(True)
        #print(self.angle)
        
        #detectar los clicks del mouse
        if pygame.mouse.get_pressed()[0] and self.fired == False and (pygame.time.get_ticks() - self.last_shoot >= shoot_cooldown):
            bullet = Bullet(self.image_bullet, self.shape.centerx, self.shape.centery, self.angle)
            self.fired = True
            self.last_shoot = pygame.time.get_ticks()

        #resetear el click del mouse
        if pygame.mouse.get_pressed()[0] == False:
            self.fired = False

        return bullet
        

    def rotate_weapon(self, rotate):

        if rotate == True:
            image_flip = pygame.transform.flip(self.image_original,
                                               True, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
        else:
            image_flip = pygame.transform.flip(self.image_original,
                                               False, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
            

    def draw(self, interface):
        self.image = pygame.transform.rotate(self.image, self.angle)
        interface.blit(self.image, self.shape)
        #pygame.draw.rect(interface, constantes.COLOR_GUN, self.shape, 1)
    
    
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image
        self.angle = angle
        self.imageB = pygame.transform.rotate(self.image_original, self.angle)
        self.rect = self.imageB.get_rect()
        self.rect.center = (x, y)
        #CALCULAR LA VELOCIDAD
        self.delta_x = math.cos(math.radians(self.angle))*constantes.VELOCIDAD_BULLET
        self.delta_y = -math.sin(math.radians(self.angle))*constantes.VELOCIDAD_BULLET

    def update(self, list_enemies):
        self.rect.x = self.rect.x + self.delta_x
        self.rect.y  = self.rect.y + self.delta_y
        #vwer si las balas salen de pantalla
        if self.rect.right < 0 or self.rect.left > constantes.WIDTH_WINDOW or self.rect.bottom < 0 or self.rect.top > constantes.HEIGHT_WINDOW:
            self.kill()

        #verificar si hay colision con enemigos
        for enemie in list_enemies:
            if enemie.shape.colliderect(self.rect):
                damage = 15 + random.randint(-7, 7)
                enemie.energy = enemie.energy - damage
                self.kill()
                break

    def draw(self, interface):
        interface.blit(self.imageB, (self.rect.centerx,
                                    self.rect.centery -  int(self.imageB.get_height()/2)))
