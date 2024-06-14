import pygame
from pygame.locals import QUIT
import math

class Circle:
    def __init__(self, x, y, radius, dot_radius):
        self.center_x = x
        self.center_y = y
        self.radius = radius
        self.angle = 0
        self.dot_radius = dot_radius

    def draw(self, window):
        pygame.draw.circle(window, "black", (self.center_x, self.center_y), self.radius, 1)
        x = self.center_x + self.radius * math.cos(math.radians(self.angle))
        y = self.center_y + self.radius * math.sin(math.radians(self.angle))
        pygame.draw.circle(window, "green", (x, y), self.dot_radius)
        # print(self.dot_radius)
        self.angle += 1
        # print(self.angle)


class Main:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
    
    def components(self):
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    
    def Loop(self):
        self.run = True
        self.circle = Circle(350, 250, 100, 10)
        self.clock = pygame.time.Clock()
        while self.run:
            self.clock.tick(100)
            for event in pygame.event.get():    
             if event.type == QUIT:
                    self.run = False

            self.win.fill(WHITE)
            self.circle.draw(self.win)
            pygame.display.flip()


WIDTH = 700
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = Main(WIDTH, HEIGHT)
window.components()
window.Loop()