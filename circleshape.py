import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def check_collisions(self, other) -> bool:
        # distance = pygame.Vector2(player.rect.center).distance_to(pygame.Vector2(other.rect.center))
        distance = pygame.Vector2(self.position).distance_to(pygame.Vector2(other.position))
        maxDistance = self.radius + other.radius

        if distance <= maxDistance:
            return True
        else:
            return False


    def draw(self, screen):
        # sub-classes must override
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pass

    def update(self, dt):
        # sub-classes must override
        pass