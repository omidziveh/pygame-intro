import pygame
import sys
pygame.init()
width = 1300
height = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (120, 120, 120)
padding = 150
display=pygame.display.set_mode((width,height))
running = True
x = 200
y = 200
vx = 15
vy = 15
cs = 40
mouse_x = -100
mouse_y = -100
mouse_state = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_state = 1
            print(mouse_x, mouse_y)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x = -100
            mouse_y = -100
            mouse_state = 0
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
    if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= cs ** 2 and mouse_state == 1:
        print('Game Over Bro')
    display.fill(GREY)
    pygame.draw.rect(display, WHITE, (padding, padding, width - 2 * padding,
                                      height - 2 * padding))
    pygame.draw.circle(display, (0, 0, 0), (x, y), cs)
    x += vx
    y += vy
    if x >= width - padding - cs or x <= cs + padding:
        vx = -vx
    if y >= height - padding - cs or y <= cs + padding:
        vy = -vy
    pygame.display.update()
    pygame.time.Clock().tick(60)
