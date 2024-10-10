import sys
import pygame

# Runs the event checker (listens to mouse and keyboard inputs)
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
# Updates images on the screen and flip to the new screen
def update_screen(ai_settings, screen, spaceship, alien):
    
    #fills the screen every pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # spawns the ship
    spaceship.blitme()
    alien.blitme()
    
            