import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.ship_lives)

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        #Image set-up
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        #Time set-up
        self.running = True
        self.clock = pygame.time.Clock()

        #Sound Settings
        pygame.mixer.init()
        self.lazer_sound = pygame.mixer.Sound(self.settings.lazer_sound)
        self.lazer_sound.set_volume(0.25)
        self.impact = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact.set_volume(1)


        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.game_active = True

    def run_game(self):
        # Game Loop etc.
        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_colissions()
            
            self._update_screen() 
            self.clock.tick(self.settings.FPS)

    def _check_colissions(self):

        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet) or self.ship.check_collisions(self.alien_fleet.special):
            #alien fleet reset, player reset, loose one life.
            self.check_game_status()

        #check collisions for aliens and screen bottom
        self.alien_fleet.check_fleet_bottom()
        
        

        #check collisions for bullets and aliens
        collisions_main_gun = self.alien_fleet.check_cannon_collisions(self.ship.arsenal.main_gun)
        self.alien_fleet.check_special_cannon_collisions(self.ship.arsenal.main_gun)
        if collisions_main_gun:
            self.impact.play()
            self.impact.fadeout(150)

        #check collisions for rounds and aliens
        collisions_cannon1 = self.alien_fleet.check_round_collisions(self.ship.arsenal.cannon1)
        collisions_cannon2 = self.alien_fleet.check_round_collisions(self.ship.arsenal.cannon2)
        self.alien_fleet.check_special_round_collisions(self.ship.arsenal.cannon1)
        self.alien_fleet.check_special_round_collisions(self.ship.arsenal.cannon2)
        if collisions_cannon1:
            self.impact.play()
            self.impact.fadeout(150)
        if collisions_cannon2:
            self.impact.play()
            self.impact.fadeout(150)
        
        #check if aliens are gone
        if self.alien_fleet.check_fleet_count() and self.alien_fleet.check_special_count():
            self.game_stats.level += 1
            self._reset_level()

        pass

    def check_game_status(self):
        if self.game_stats.ship_lives > 0:
            self.game_stats.ship_lives -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False
      

    def _reset_level(self):
        self.ship.arsenal.main_gun.empty()
        self.ship.arsenal.cannon1.empty()
        self.ship.arsenal.cannon2.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.special.empty()
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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_1:
            if self.ship.fire_main_gun():
                self.lazer_sound.play()
            #play the lazer sound
        elif event.key == pygame.K_2:
            if self.ship.fire_cannon1():
                self.lazer_sound.play()
        elif event.key == pygame.K_3:
            if self.ship.fire_cannon2():
                self.lazer_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

