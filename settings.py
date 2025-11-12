from pathlib import Path

class Settings:
    
    def __init__(self):
        
        #Basic Game Settings
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        #Ship Settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed_horizontal = 5
        self.ship_speed_vertical = 5

        #Settings for Main Gun
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.lazer_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        #Settings for Cannons
        self.round_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        #self.round_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.round_speed = 7
        self.round_w = 12.5
        self.round_h = 40
        self.round_amount = 10