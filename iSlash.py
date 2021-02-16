import pygame
pygame.init()
width = 800
height = 600
display=pygame.display.set_mode((width,height))
running = True
x = 100
y = 100
vx = 5
vy = 5
cs = 70
while running:
    display.fill((255, 255, 255))
    pygame.draw.circle(display, (0, 0, 0), (x, y), cs)
    x += vx
    y += vy
    if x >= width - cs or x <= cs:
        vx = -vx
    if y >= height - cs or y <= cs:
        vy = -vy
    pygame.display.update()
    pygame.time.Clock().tick(60)
