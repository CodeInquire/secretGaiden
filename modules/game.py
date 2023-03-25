import pygame
from .config import *
from .engine import *

class Game:

    def __init__(self, master):

        self.master = master
        master.game = self

        self.screen = pygame.display.get_surface()

        self.canvas = pygame.Surface((W, H))
        self.canvas.set_colorkey((0, 0, 0))

    def run(self):

        mouse = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        relx, rely = pygame.mouse.get_rel()
        if mouse[0]:
            pygame.draw.line(self.canvas, "blue", (mx-relx, my-rely), (mx, my), 12)
        if mouse[2]:
            pygame.draw.line(self.canvas, "black", (mx-relx, my-rely), (mx, my), 24)

        self.screen.fill((80, 1, 24))
        self.screen.blit(self.canvas, (0, 0))
        