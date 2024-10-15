import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # GAME LOOP
    while True:
        # Scan for quit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black
        screen.fill((0, 0, 0, 255))
        # Refresh screen
        pygame.display.flip()

if __name__ == "__main__":
    main()