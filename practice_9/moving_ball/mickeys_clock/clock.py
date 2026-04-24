import pygame
import math
import datetime

class MickeyClock:
    def __init__(self, center):
        self.center = center

    def draw_hand(self, screen, length, angle, color):
        rad = math.radians(angle - 90)
        x = self.center[0] + length * math.cos(rad)
        y = self.center[1] + length * math.sin(rad)
        pygame.draw.line(screen, color, self.center, (x, y), 6)

    def draw(self, screen):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        sec_angle = seconds * 6
        min_angle = minutes * 6

        self.draw_hand(screen, 120, sec_angle, (0, 0, 255))  # left hand
        self.draw_hand(screen, 80, min_angle, (0, 0, 0))     # right hand