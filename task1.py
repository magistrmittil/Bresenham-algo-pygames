import time
import pygame
import math

#алгоритм Брезенхема 
def bresenham_circle(x_center, y_center, radius):
    points = []
    x, y = 0, radius
    d = 3 - 2 * radius
    while y >= x:
        points.extend([
            (x_center + x, y_center + y), (x_center - x, y_center + y),
            (x_center + x, y_center - y), (x_center - x, y_center - y),
            (x_center + y, y_center + x), (x_center - y, y_center + x),
            (x_center + y, y_center - x), (x_center - y, y_center - x)
        ])
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
    return points

# Измерение Брезенхема
def measure_bresenham(radius, circles):
    start_time = time.time()
    for _ in range(circles):
        bresenham_circle(0, 0, radius)
    end_time = time.time()
    return end_time - start_time

# окружность через Pygame + измерение времени построения
def measure_pygame_circle(radius, circles):
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    start_time = time.time()
    for _ in range(circles):
        pygame.draw.circle(screen, (255, 255, 255), (0, 0), radius)
    end_time = time.time()
    pygame.quit()
    return end_time - start_time
    
#радиус и количетсво измеряемых по времени окружностей
circles = 100000
radius = 50

bre_time = measure_bresenham(radius, circles)
print("Время Брезенхема:", bre_time)

pygame_time = measure_pygame_circle(radius, circles)
print("Время построения окружности Pygame:", pygame_time)

if bre_time > pygame_time:
    print("Алгоритм Брезенхема менее производителен")