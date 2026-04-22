import pygame
from ball import Ball

# 1. Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

# 2. Создаем шарик в центре
my_ball = Ball(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        my_ball.move("left", WIDTH, HEIGHT)
    if keys[pygame.K_d]:
        my_ball.move("right", WIDTH, HEIGHT)
    if keys[pygame.K_w]:
        my_ball.move("up", WIDTH, HEIGHT)
    if keys[pygame.K_s]:
        my_ball.move("down", WIDTH, HEIGHT)

    screen.fill((255, 255, 255)) 
    my_ball.draw(screen)         # Рисуем шарик
    
    pygame.display.flip()        # Показываем результат
    clock.tick(60)               

pygame.quit()