import pygame

width, height = 400, 400
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

circle_radius = 10
circle_color = pygame.Color('white')
circle = []
speed = []
screen2 = pygame.Surface(screen.get_size())

while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())

        if event.type == pygame.MOUSEBUTTONUP:
            circle.append(list(event.pos))
            speed.append([-1, -1])

        if event.type == pygame.QUIT:
            running = False

    screen2.fill(pygame.Color('black'))

    for i in range(len(circle)):
        for j in (0, 1):
            if circle[i][j] >= size[j] - circle_radius or circle[i][j] <= circle_radius:
                speed[i][j] = -speed[i][j]
            circle[i][j] += speed[i][j]

        pygame.draw.circle(screen2, circle_color,
                           circle[i], circle_radius, 0)

    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(100)

pygame.quit()