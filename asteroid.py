import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()

        # IF the asteroid is a small one, do nothing.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid1.velocity = a1 * 1.2
        small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid2.velocity = a2 * 1.2

        


    # Override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt