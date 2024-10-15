import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # GAME LOOP
    while True:
        # Scan for quit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black
        screen.fill((0, 0, 0, 255))
        # Draw player sprite
        player.draw(screen)
        # Refresh screen
        pygame.display.flip()

        

        # Advance the game clock.  This should happen last.
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()