import pygame
import game_functions as gf

from settings import Settings
from spaceship import Spaceship
from alien_1 import Alien
from pygame.sprite import Group

def run_game():
    
    # main func to start and create screen
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion by Matteo")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    
    #spawns the entities
    spaceship = Spaceship(ai_settings, screen)
    alien = Alien(screen)
    bullets = Group()
    
   # starts the main loop for the game. 
    while True:
        
        #runs game functions 
        gf.check_events(spaceship, bullets, ai_settings, screen)
        spaceship.update()
        gf.update_bullets(bullets) 
        
        gf.update_screen(ai_settings, screen, spaceship, alien, bullets)
        
        #makes the most recent drawn screen visible
        pygame.display.flip()
        
run_game()