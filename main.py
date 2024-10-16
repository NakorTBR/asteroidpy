import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # GAME LOOP
    while True:
        # Scan for quit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update updatable group
        for obj in updatable:
            obj.update(dt)
        # Update asteroids group
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
        # Fill screen with black
        screen.fill((0, 0, 0, 255))
        # Update drawables group
        for obj in drawable:
            obj.draw(screen)        
        # Refresh screen
        pygame.display.flip()        

        # Advance the game clock.  This should happen last.
        # 60 FPS cap
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()