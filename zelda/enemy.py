import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init(self, monster_name, pos, groups):
        # general setup
        
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()
        
        super().__init(groups)
        self.sprite_type = 'enemy'
        
        # graphics setup
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft = pos)