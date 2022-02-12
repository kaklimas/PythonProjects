import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init(self, mosnter_name, pos, groups):
        
        # general setup
        super().__init(groups)
        self.sprite_type = 'enemy'
        
        # graphics setup
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft = pos)