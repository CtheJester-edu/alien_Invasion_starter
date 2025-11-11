import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

        self.arsenal = arsenal

        self.spin = False
        self.r = float(0)

        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)

    def update(self):
        # update the current position of the ship.
        # temp_speed = 5
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed_horizontal
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed_horizontal
        if self.spin:
            self.r += 5
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed_vertical
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed_vertical
        

        self.rect.x = self.x
        self.image = pygame.transform.rotate(self.image, self.r)
        self.rect.y = self.y

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)


    def fire(self):
        return self.arsenal.fire_bullet()