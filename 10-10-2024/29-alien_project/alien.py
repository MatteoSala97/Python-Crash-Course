import pygame
from pygame.sprite import Sprite

class Alien(Sprite):  
    def __init__(self, ai_settings, screen):
        super().__init__()  
        self.screen = screen

        # Loads the image and resizes 
        self.image = pygame.image.load(r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\29-alien_project\images\alien.png')
        new_width = int(self.image.get_width() * 0.1)  
        new_height = int(self.image.get_height() * 0.1)  
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        # Creates the rectangle to handle movement
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Sets the initial position in the center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        # Spawns the alien(s)
        self.screen.blit(self.image, self.rect)
