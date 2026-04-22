import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25
        self.color = (255, 0, 0) 
        self.step = 20


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, direction, width, height):
        if direction == 'left':
            if self.x - self.step >= self.radius:
                self.x -= self.step
        if direction == 'right':
            if self.x + self.step + self.radius <= width:
                self.x+=self.step
        if direction == "down":
            if self.y + self.radius + self.step <=height:
                self.y+=self.step
        if direction == "up":
            if self.y - self.step - self.radius >= 0:
                self.y -= self.step
