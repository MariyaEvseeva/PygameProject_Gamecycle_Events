import pygame

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
x = 0
y = 0
rect_color = pygame.Color('green')
a = ((x, y), (100, 100))
x1 = y1 = x2 = y2 = 0

while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if (x1 < x) or (x1 > x + 100) or (y1 < y) or (y1 > y + 100):
                x1 = y1 = 0

        if event.type == pygame.MOUSEMOTION and x1 > 0:
            x2 = event.pos[0] - x1
            y2 = event.pos[1] - y1

        if event.type == pygame.MOUSEBUTTONUP:
            x += x2
            y += y2
            x1 = y1 = x2 = y2 = 0

    a = ((x + x2, y + y2), (100, 100))
    pygame.draw.rect(screen, rect_color, a, 0)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()