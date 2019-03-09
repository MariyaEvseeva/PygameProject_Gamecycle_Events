import math
import pygame

size = width, height = 201, 201
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
circle_color = polygon_color = pygame.Color('white')
circle_x = width // 2 + 1
circle_y = height // 2 + 1
circle_pos = (circle_x, circle_y)
angle = 35 / 360
r = 70
speed = 0

while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            if event.button == 1:
                speed -= 2 / 180
            if event.button == 3:
                speed += 2 / 180

    circle_pos = (circle_x, circle_y)
    pygame.draw.circle(screen, circle_color, circle_pos, 10, 0)

    for i in range(3):
        a = (circle_x + r * math.cos(angle * math.pi),
             circle_y + r * math.sin(angle * math.pi))
        b = (circle_x + r * math.cos((angle + 1 / 6) * math.pi),
             circle_y + r * math.sin((angle + 1 / 6) * math.pi))
        polygon_points = [circle_pos, a, b]
        pygame.draw.polygon(screen, polygon_color, polygon_points, 0)
        angle += 120 / 180

    angle += speed

    pygame.display.flip()
    clock.tick(50)
pygame.quit()