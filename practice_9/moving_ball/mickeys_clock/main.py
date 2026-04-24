import pygame
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = MickeyClock((WIDTH // 2, HEIGHT // 2))

running = True
while running:
    clock.tick(1)  # update every second
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, (0, 0, 0), (WIDTH // 2, HEIGHT // 2), 150, 3)
    mickey.draw(screen)

    pygame.display.flip()

pygame.quit()