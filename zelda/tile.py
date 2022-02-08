import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        
        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
<<<<<<< HEAD
        self.hitbox = self.rect.inflate(0, -50)
=======
        self.hitbox = self.rect.inflate(0, -45)
>>>>>>> 84e5afee287fa3aa07483ad2595297d3a15a6b9f
            
