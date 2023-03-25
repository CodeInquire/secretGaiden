import pygame
import sys
import asyncio
from modules import *


class Master:

    def __init__(self):

        self.app:App
        self.debug:Debug
        self.dt:float
        self.offset:pygame.Vector2


class App:

    MAIN_MENU = 0
    IN_GAME = 1

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED)
        pygame.display.set_caption(NAME)
        # icon = pygame.image.load("graphics/icon.png").convert()
        # pygame.display.set_icon(icon)
        self.clock = pygame.Clock()

        self.state = self.IN_GAME

        self.master = Master()
        self.debug = Debug(font_size=16)
        self.master.debug = self.debug
        self.game = Game(self.master)

    async def run(self):
        
        while True:

            pygame.display.flip()
            self.master.dt = self.clock.tick(FPS) / 16.667
            if self.master.dt > 10:
                self.master.dt = 10
            self.debug("FPS", round(self.clock.get_fps(), 2))

            for event in pygame.event.get((pygame.QUIT)):
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            await asyncio.sleep(0)

            self.run_states()
            self.debug.draw()

    def run_states(self):

        if self.state == self.MAIN_MENU:
            self.main_menu.run()
        elif self.state == self.IN_GAME:
            self.game.run()


if __name__ == "__main__":
    app = App()
    asyncio.run(app.run())
