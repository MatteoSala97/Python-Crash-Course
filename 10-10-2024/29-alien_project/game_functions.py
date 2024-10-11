import sys
import pygame

from bullet import Bullet 



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

# bullet function
def update_bullets(bullets):
    #deleting out-of-bounds bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)    
        # print(len(bullets))    
    bullets.update()

# Runs the event checker (listens to mouse and keyboard inputs)
def check_events(spaceship, bullets, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # moves the spaceship to the right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, spaceship)
                    bullets.add(new_bullet)
                 
            check_keydown_events(event, spaceship)
            
        # moves the spaceship to the left     
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
                
                
# Updates images on the screen and flip to the new screen
def update_screen(ai_settings, screen, spaceship, alien, bullets):
    
    #fills the screen every pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # spawns the ship
    spaceship.blitme()
    
    #spawns the alien
    alien.blitme()
    
    # Draws bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()


            