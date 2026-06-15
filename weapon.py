import pygame
import constantes
import math

class Weapon():
    def __init__(self, image):
        self.image_original = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.shape = self.image.get_rect()

    def update(self, Player):
        self.shape.center = Player.shape.center
        if Player.flip == False:
            self.shape.x = self.shape.x + Player.shape.width /1.5
            self.shape.y = self.shape.y + Player.shape.height /6.5
            self.rotate_weapon(False)

        if Player.flip == True:
            self.shape.x = self.shape.x - Player.shape.width /1.5
            self.shape.y = self.shape.y + Player.shape.height /6.5
            self.rotate_weapon(True)
        
        #mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distance_x = mouse_pos[0] - self.shape.centerx
        distance_y = -(mouse_pos[1] - self.shape.centery)
        self.angle = math.degrees(math.atan2(distance_y, distance_x))

        print(self.angle)
        
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
    
    
