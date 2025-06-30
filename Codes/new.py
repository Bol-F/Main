import pygame
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Рисуем 1000 случайных кругов
    for _ in range(1000):
        x, y = random.randint(0, width), random.randint(0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), 5)
    pygame.display.flip()
    screen.fill((0, 0, 0))  # Очистка экрана
    clock.tick(60)  # 60 FPS
