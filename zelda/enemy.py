from entity import Entity
import pygame
from settings import *
from support import import_folder

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):
        
        # general setup
        super().__init__(groups)
        self.sprite_type = "enemy"
        
        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = pygame.Surface((64, 64)) 
        self.rect = self.image.get_rect(topleft = pos)
    
    def import_graphics(self, monster_name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'./graphics/monsters/{monster_name}/'
        
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)