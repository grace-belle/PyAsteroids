import pygame
from circleshape import CircleShape
import constants
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        if self.radius > constants.ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            self.velocity1 = self.velocity.rotate(angle)
            self.velocity2 = self.velocity.rotate(-angle)
            ast_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, ast_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, ast_radius)
            asteroid1.velocity = self.velocity1 * 1.2
            asteroid2.velocity = self.velocity2 * 1.2