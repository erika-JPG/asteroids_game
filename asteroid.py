import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0) 

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #spawning more asteroids
        angle = random.uniform(20, 50)

        first = self.velocity.rotate(angle)
        second = self.velocity.rotate(-angle)

        first_velocity = first * 1.2
        second_velocity = second* 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = first * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = second * 1.2

