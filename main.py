import pygame

from constants import *
from draw_board import draw_squares


def main():
    print(f"Starting Chess with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_SIZE}")
    print(f"Screen height: {SCREEN_SIZE}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        draw_squares(screen)
        pygame.display.flip()
        clock.tick(60)




if __name__ == "__main__":
    main()
