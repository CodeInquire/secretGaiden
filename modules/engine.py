import pygame
import os
from .config import *


class CustomGroup(pygame.sprite.Group):

    def draw(self):

        for sprite in self.sprites():
            sprite.draw()

    def draw_y_sort(self, key):
        
        """draws the sprites sorted in the order of the given key"""
        for sprite in sorted(self.sprites(), key=key):
            sprite.draw()


class CustomTimer:

    def __init__(self):

        self.running = False
        self.duration = None
        self.start_time = None
        self.loops = 0
        self.infinite = False

    def start(self, duration, loops=1):

        self.running = True
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.loops = loops
        self.infinite = loops <= 0

    def signal(self):

        """starts timer with 0 duration, to act as a signal"""

        self.running = True
        self.duration = 0
        self.start_time = pygame.time.get_ticks()
        self.loops = 1
        self.infinite = False

    def stop(self):
     
        if self.running:
            self.running = False
            return True

    def check(self):

        if not self.running:
            return False
     
        if pygame.time.get_ticks() - self.duration >= self.start_time:

            if self.infinite:
                self.start_time += self.duration
                return True
            
            self.loops -= 1
            if self.loops == 0:
                self.running = False
            else:
                self.start_time += self.duration
            return True
     

def import_spritesheet(folder_path, sheet_name):

    """imports a given spritesheet and places it in a list"""
    sprite_list = []
    name, size = sheet_name[:-4].split('-')
    w, h = [int(x) for x in size.split('x')]
    sheet = pygame.image.load(F"{folder_path}/{sheet_name}").convert_alpha()
    for j in range(sheet.get_height()//h):
        for i in range(sheet.get_width()//w):
            sprite = sheet.subsurface((w*i, h*j, w, h))
            sprite_list.append(sprite)
    return sprite_list


def import_sprite_sheets(folder_path) -> dict[str, list[pygame.Surface]]:

    """imports all spritesheets in a folder"""
    animations = {}

    for file in os.listdir(folder_path):
        if file.endswith(".png"):
            animations[file.split('-')[0]] = import_spritesheet(folder_path, file)

    return animations


def load_pngs_dict(folder_path) ->  dict[str, pygame.Surface]:

    sprites = {}
    for file in os.listdir(folder_path):
        sprites[file[:-4]] = pygame.image.load(F"{folder_path}/{file}").convert_alpha()
    return sprites


def load_pngs(folder_path) ->  list[pygame.Surface]:
    "loads all png from folder"

    return [pygame.image.load(F"{folder_path}/{file}").convert()
            for file in sorted(os.listdir(folder_path))]


def dist_sq(p1, p2):

    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
