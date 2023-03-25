import pygame, json
from pygame.locals import *
from random import randint, choice
from sys import exit

### Initialization and base variable constants
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

WIDTH = 1024
HEIGHT = 768

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('This is a template'.upper())

CLOCK = pygame.time.Clock()

### Main game func/loop
def MAIN():

    RUN = True

    while RUN:

        WINDOW.fill((100,100,255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT')
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT RELEASED')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT RELEASED')


        pygame.display.flip()

### Call to MAIN game func to run game
MAIN() if __name__ == '__main__' else print('Not Main')
