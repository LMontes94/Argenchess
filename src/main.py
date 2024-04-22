import pygame
from const import *


class App():
    def __init__(self) -> None:
        self.MAX_WIDTH = MAX_WIDTH
        self.MAX_HEIGHT = MAX_HEIGHT

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("#B9D5EF")

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


main = App()
main.start()
