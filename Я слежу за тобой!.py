import pygame

size = w, h = 200, 200
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
text_size = 100
text_color = pygame.Color('red')
pygame.init()
font = pygame.font.Font(None, text_size)
number = 1

while running:
    screen.fill(pygame.Color('black'))
    text = font.render(str(number), True, text_color)
    (text_w, text_h) = text.get_rect().size
    text_x = (w - text_w) // 2
    text_y = (h - text_h) // 2
    screen.blit(text, [text_x, text_y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEOEXPOSE:
            number += 1

    pygame.display.flip()
    clock.tick(100)

pygame.quit()