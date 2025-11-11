import pygame
from typing import TYPE_CHECKING
from bullet import Bullet
from round import Round

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    def __init__(self, game:'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.main_gun = pygame.sprite.Group()
        self.cannons = pygame.sprite.Group()

    def update_arsenal(self):
        
        
        
        self.main_gun.update()
        self._remove_bullets_offscreen()

        self.cannons.update()
        self._remove_rounds_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.main_gun.copy():
            if bullet.rect.bottom <= 0:
                self.main_gun.remove(bullet)

    def _remove_rounds_offscreen(self):
        for round in self.cannons.copy():
            if round.rect.bottom <= 0:
                self.cannons.remove(round)

    def draw(self):
        for bullet in self.main_gun:
            bullet.draw_bullet()

        for round in self.cannons:
            round.draw_round()

    def fire_bullet(self):
        if len(self.main_gun) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.main_gun.add(new_bullet)
            return True
        return False
    
    def fire_round(self):
        if len(self.main_gun) < self.settings.round_amount:
            new_round = Round(self.game)
            self.cannons.add(new_round)
            return True
        return False