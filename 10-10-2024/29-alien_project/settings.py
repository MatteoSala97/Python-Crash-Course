class Settings():
    # initializes the game's settings
    def __init__(self):
        
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (160,180,200)
        
        # Ship settings
        self.spaceship_speed_factor = 1
        
        
        # Bullet settings
        self.bullet_speed_factor = 1.1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 5