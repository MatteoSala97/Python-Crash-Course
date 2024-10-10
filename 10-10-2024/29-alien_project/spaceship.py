import pygame

class Spaceship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load(r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\29-alien_project\images\spaceship.png')
        
        new_width = int(self.image.get_width() * 0.2)  
        new_height = int(self.image.get_height() * 0.2)  
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #movement flag (allows continuous movement without having to spam the key)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)