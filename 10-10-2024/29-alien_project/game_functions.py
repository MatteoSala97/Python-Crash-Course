import sys
import pygame


# listener on keydown events 
def check_keydown_events(event, spaceship):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    elif event.key == pygame.K_UP:
        spaceship.moving_up = True
    elif event.key == pygame.K_DOWN:
        spaceship.moving_down = True
    

def check_keyup_events(event, spaceship):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = False
    elif event.key == pygame.K_UP:
        spaceship.moving_up = False
    elif event.key == pygame.K_DOWN:
        spaceship.moving_down = False



# Runs the event checker (listens to mouse and keyboard inputs)
def check_events(spaceship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # moves the spaceship to the right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, spaceship)
                
        # moves the spaceship to the left     
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
                
                
# Updates images on the screen and flip to the new screen
def update_screen(ai_settings, screen, spaceship, alien):
    
    #fills the screen every pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # spawns the ship
    spaceship.blitme()
    
    #spawns the alien
    alien.blitme()


            