import pygame

size = w, h = 501, 501
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
circle_color = pygame.Color('red')
circle_x = x1 = w // 2 + 1
circle_y = y1 = h // 2 + 1
circle_pos = (circle_x, circle_y)
circle_radius = 20
circle_w = 0

while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos

    if x1 > circle_x:
        circle_x += 1
    elif x1 < circle_x:
        circle_x -= 1

    if y1 > circle_y:
        circle_y += 1
    elif y1 < circle_y:
        circle_y -= 1

    circle_pos = (circle_x, circle_y)
    pygame.draw.circle(screen, circle_color, circle_pos,
                       circle_radius, circle_w)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()