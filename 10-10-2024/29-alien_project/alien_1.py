import pygame

class  Alien():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load(r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\29-alien_project\images\alien_1.png')
        
        new_width = int(self.image.get_width() * 0.1)  
        new_height = int(self.image.get_height() * 0.1)  
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)