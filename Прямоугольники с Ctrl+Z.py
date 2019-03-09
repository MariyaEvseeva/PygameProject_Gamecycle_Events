import pygame

size = w, h = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
rect_color = pygame.Color('white')
start_x = []
start_y = []
rect_w = []
rect_h = []

x1 = y1 = 0

drawing = False
z = False
ctrl = False

while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                z = True
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                z = False
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = False

        if z == True and ctrl == True and len(start_x) > 0:
            start_x.pop()
            start_y.pop()
            rect_w.pop()
            rect_h.pop()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            x1, y1 = event.pos
            x2, y2 = x1, y1

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            start_x.append(x1)
            start_y.append(y1)
            rect_w.append(x2 - x1)
            rect_h.append(y2 - y1)

        if event.type == pygame.MOUSEMOTION:
            x2, y2 = event.pos

    for i in range(len(start_x)):
        pygame.draw.rect(screen, rect_color, ((start_x[i], start_y[i]),
                                              (rect_w[i], rect_h[i])), 5)
    if drawing == True:
        pygame.draw.rect(screen, rect_color,
                         ((x1, y1), (x2 - x1, y2 - y1)), 5)

    pygame.display.flip()
pygame.quit()