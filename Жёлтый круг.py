import pygame

size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
screen.fill(pygame.Color('blue'))
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = pygame.Color('yellow')
plus_radius = 25
pygame.time.set_timer(plus_radius, 10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            circle_exists = True
            screen.fill(pygame.Color('blue'))
            circle_radius = 0
            circle_pos = event.pos
            pygame.draw.circle(screen, circle_color, 
                               circle_pos, circle_radius, circle_width)

        if event.type == plus_radius and circle_exists:
            circle_radius += 1
            pygame.draw.circle(screen, circle_color, 
                               circle_pos, circle_radius, circle_width)

    pygame.display.flip()
    clock.tick(50)


pygame.quit()