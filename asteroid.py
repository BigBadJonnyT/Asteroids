import pygame
from circleshape import CircleShape
from constants import DRAW_COLOR, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = DRAW_COLOR
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt