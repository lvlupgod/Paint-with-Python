import pygame
import math
from random import randint

timer = pygame.time.Clock()
level = []
colors = [ 'black','red','blue', 'red', 'yellow', 'green', 'purple', 'pink', 'cyan', 'brown']
color = 'black'
size = 35


pygame.init()

modes = pygame.display.list_modes()
WIDTH, HEIGHT = modes[0]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(True)
screen.fill('white')
pygame.display.flip()
pygame.cursors.load_xbm('PaintfromWish\cursor.xbm', 'PaintfromWish\cursor.xbm')
pygame.display.flip()
running = True



def draw(x_pos, y_pos, color, size):
    # screen.blit(q,(x_pos,y_pos))
    q = pygame.Surface((35, 35))
    q.fill(color)
    screen.blit(q, (1677 - size, 0))
    pygame.draw.circle(screen, color , (x_pos, y_pos), size)
    pygame.display.flip()
    timer.tick(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

while running:
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            if event.y > event.x:
                size += 3
            else : size -= 3
    if pygame.mouse.get_pressed() == (True, False, False):
        x_pos, y_pos = pygame.mouse.get_pos()
        draw(x_pos, y_pos, color, size)
    if pygame.mouse.get_pressed() == (False, False, True):
        color = 'white'
    if keys[pygame.K_1]:
        color = colors[0]
    if keys[pygame.K_2]:
        color = colors[1]
    if keys[pygame.K_3]:
        color = colors[2]
    if keys[pygame.K_4]:
        color = colors[3]
    if keys[pygame.K_5]:
        color = colors[4]
    if keys[pygame.K_6]:
        color = colors[5]
    if keys[pygame.K_7]:
        color = colors[6]
    if keys[pygame.K_8]:
        color = colors[7]
    if keys[pygame.K_9]:
        color = colors[8]
    if keys[pygame.K_0]:
        color = colors[9]
    if keys[pygame.K_r]:
        screen.fill('white')
        pygame.display.flip()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_s]:
        

        pygame.quit()