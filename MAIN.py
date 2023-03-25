import pygame, json
from pygame.locals import *
from random import randint, choice
from sys import exit

### initialization & base constants
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

WIDTH = 1024
HEIGHT = 768

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('This is a template'.upper())

CLOCK = pygame.time.Clock()

### main game func/loop
def MAIN():

    RUN = True

    while RUN:

        WINDOW.fill((100,100,255))

        for event in pygame.event.get():

            match event.type:

                case pygame.QUIT:
                    pygame.quit()
                    exit()

                case pygame.KEYDOWN:

                    match event.key:

                        case pygame.K_a | pygame.K_LEFT:
                            print('LEFT')
                        case pygame.K_d | pygame.K_RIGHT:
                            print('RIGHT')
            
            match event.type:

                case pygame.KEYUP:

                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            exit()

                    match event.key:
                        case pygame.K_a | pygame.K_LEFT:
                            print('LEFT RELEASED')
                        case pygame.K_d | pygame.K_RIGHT:
                            print('RIGHT RELEASED')


        pygame.display.flip()

### Call to MAIN game func to run game
MAIN() if __name__ == '__main__' else print('Not Main')
