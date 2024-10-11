import sys
import pygame

from bullet import Bullet 
from alien import Alien



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
       
       
       
def get_number_aliens_x(ai_settings, alien_width): 
    available_space_x = ai_settings.screen_width - 2 * alien_width 
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x

def get_number_rows(ai_settings, spaceship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - spaceship_height)
    number_rows = int(available_space_y / (2 * alien_height)) 
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

# Create an alien and find the number of aliens in a row. 
def create_fleet(ai_settings, screen, spaceship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, spaceship.rect.height, alien.rect.height)
    
    # Crea la prima fila di alieni
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
 
 
       
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
    alien.draw(screen)
    
    # Draws bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #makes the most recent drawn screen visible
    pygame.display.flip()
    
    


            