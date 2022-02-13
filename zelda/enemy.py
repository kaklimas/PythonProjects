from entity import Entity
import pygame
from settings import *

class Enemy(Entity):
    def __init__(self, monster_name, pos,  groups):
        super().__init__(groups)