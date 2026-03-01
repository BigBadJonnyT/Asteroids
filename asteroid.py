import pygame
import random
from circleshape import CircleShape
from constants import DRAW_COLOR, LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = DRAW_COLOR
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            new_vector_one = self.velocity.rotate(new_angle)
            new_vector_two = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_one.velocity = new_vector_one * 1.2
            new_asteroid_two.velocity = new_vector_two * 1.2



