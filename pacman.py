import pygame
from pygame.locals import *
from vector import Vector2
from constants import *


class Pacman(object):
    def __init__(self):
        self.position = Vector2(200, 400)
        self.directions = {STOP: Vector2(), UP: Vector2(0, -1), DOWN: Vector2(0, 1), LEFT: Vector2(-1, 0),
                           RIGHT: Vector2(1, 0)}
        self.direction = STOP
        self.speed = 100
        self.radius = 10
        self.collideRadius = 5
        self.color = YELLOW

    def update(self, dt):
        self.position += self.directions[self.direction] * self.speed * dt
        direction = self.teclasMovimiento()
        self.direction = direction

    def teclasMovimiento(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP

    def comer(self, pastilla):
        d = self.position - pastilla.position
        dSquared = d.magnitudeSquared()
        rSquared = (pastilla.radius + self.collideRadius) ** 2
        if dSquared <= rSquared:
            return pastilla
        return None

    def colisionFantasma(self, ghost):
        d = self.position - ghost.position
        dSquared = d.magnitudeSquared()
        rSquared = (ghost.radius + self.collideRadius) ** 2
        if dSquared <= rSquared:
            return ghost
        return None
    # obsoleto , lo dejo pero ya no vale
    # def muerte(self, screen):
    #     p = self.position.asInt()
    #     pygame.draw.circle(screen, self.color, p, 0)

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)
