import pygame
import random

class Stars():
    def __init__(self, screen, ai_settings, num_stars=20):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stars = pygame.sprite.Group()
        
        self.image = pygame.image.load(r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\29-alien_project\images\stars.svg')
        new_width = int(self.image.get_width() * 0.4)  
        new_height = int(self.image.get_height() * 0.4)  
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        
        for _ in range(num_stars):
            star = self.create_star()
            self.stars.add(star)
        
    def create_star(self):
        # Crea una nuova stella con posizione casuale
        star = pygame.sprite.Sprite()
        star.image = self.image
        star.rect = self.image.get_rect()
        
        star.rect.x = random.randint(0, self.screen.get_width() - star.rect.width)
        star.rect.y = random.randint(0, self.screen.get_height() - star.rect.height)
        return star

    def blitme(self):
        for star in self.stars:
            self.screen.blit(star.image, star.rect)