import sys
import pygame

# Runs the event checker (listens to mouse and keyboard inputs)
def check_events(spaceship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # moves the spaceship to the right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceship.moving_right = True
            elif event.key == pygame.K_LEFT:
                spaceship.moving_left = True
        # moves the spaceship to the left     
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceship.moving_right = False
            elif event.key == pygame.K_LEFT:
                spaceship.moving_left = False
                
# Updates images on the screen and flip to the new screen
def update_screen(ai_settings, screen, spaceship, alien):
    
    #fills the screen every pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # spawns the ship
    spaceship.blitme()
    
    #spawns the alien
    alien.blitme()


            