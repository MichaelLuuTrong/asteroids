import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position , self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        dead_asteroid_velocity = self.velocity 

        positive_angle_split_vector = dead_asteroid_velocity.rotate(random_angle)
        negative_angle_split_vector = dead_asteroid_velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        smaller_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        smaller_asteroid_1.velocity = (positive_angle_split_vector * 1.2)
        smaller_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        smaller_asteroid_2.velocity = (negative_angle_split_vector * 1.2)
        
