import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.lazer_sound = pygame.mixer.Sound(self.settings.lazer_sound)
        self.lazer_sound.set_volume(0.5)
        self.impact = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact.set_volume(0.7)


        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet =AlienFleet(self)
        self.alien_fleet.create_fleet()

    def run_game(self):
        # Game Loop etc.
        while self.running:
            self._check_events()

            self.ship.update()
            self.alien_fleet.update_fleet()

            self._check_colissions()

            self._update_screen() 
            self.clock.tick(self.settings.FPS)

    def _check_colissions(self):

        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            #alien fleet reset, player reset, loose one life.
            self._reset_level()

        #check collisions for aliens and screen bottom
        if self.alien_fleet.check_fleet_bottom():
            self._reset_level()
        
        

        #check collisions for bullets and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact.play()
            self.impact.fadeout(150)

        pass

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

        pass

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        #self.alien.draw_alien()
        self.alien_fleet.draw_fleet()
        pygame.display.flip()



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.lazer_sound.play()
            #play the lazer sound
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

