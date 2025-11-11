import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:

    def __init__(self):

        #Game initialization.

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
        self.lazer_sound.set_volume(0.7)


        self.ship = Ship(self, Arsenal(self))

    def run_game(self):

        # Game Loop etc.

        while self.running:
            self._check_events()

            self.ship.update()

            self._update_screen() 
            self.clock.tick(self.settings.FPS)



    def _update_screen(self):

        #Redraws the screen.

        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()



    def _check_events(self):

        #Checks what inputs have been recieved.

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

        #Check for pressing down buttons

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        #Gag idea. Currently just crashes my code.
        #elif event.key == pygame.K_s:
            #self.ship.spin = True

        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        
        elif event.key == pygame.K_1:
            if self.ship.fire_main_gun():
                self.lazer_sound.play()
            #play the lazer sound
        elif event.key == pygame.K_2:
            if self.ship.fire_cannons():
                self.lazer_sound.play()
            #plays regular lazer sound for now.
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        
        # Check for letting go of keys

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
        #Gag idea. Currently just crashes my code.
        #elif event.key == pygame.K_s:
            #self.ship.spin = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

