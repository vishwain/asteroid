import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color=(255,255,0,1), center=self.position, radius=SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt