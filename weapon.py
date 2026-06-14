import pygame
import constantes

class Weapon():
    def __init__(self, image):
        self.image_original = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.shape = self.image.get_rect()

    def update(self, Player):
        self.shape.center = Player.shape.center
        self.shape.x = self.shape.x + Player.shape.width /2
        self.shape.y = self.shape.y + Player.shape.height /6.5

    def draw(self, interface):
        interface.blit(self.image, self.shape)
        pygame.draw.rect(interface, constantes.COLOR_GUN, self.shape, 1)
