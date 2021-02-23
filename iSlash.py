import pygame
import sys
pygame.init()
width = 800
height = 600
display=pygame.display.set_mode((width,height))
running = True
x = 100
y = 100
vx = 5
vy = 5
cs = 40
mouse_x = -100
mouse_y = -100
mouse_state = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    display.fill((255, 255, 255))
    pygame.draw.circle(display, (0, 0, 0), (x, y), cs)
    x += vx
    y += vy
    if x >= width - cs or x <= cs:
        vx = -vx
    if y >= height - cs or y <= cs:
        vy = -vy
    pygame.display.update()
    pygame.event.pump()
    pygame.time.Clock().tick(60)
