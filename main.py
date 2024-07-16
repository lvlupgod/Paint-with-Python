import time

import pygame
import math
from random import randint

cursor_count = 0
timer = pygame.time.Clock()
level = []
cursors = [pygame.cursors.arrow, pygame.cursors.diamond, pygame.cursors.broken_x, pygame.cursors.tri_left, pygame.cursors.tri_right]
colors = [ 'black','red','blue', 'red', 'yellow', 'green', 'purple', 'pink', 'cyan', 'brown']
color = 'black'
size = 25



pygame.init()
active = False
text = ''
font = pygame.font.Font('freesansbold.ttf', 40)
modes = pygame.display.list_modes()
WIDTH, HEIGHT = modes[0]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(True)
screen.fill('white')
pygame.display.flip()
pygame.display.flip()
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
line_point1 = 0
line_point2 = 0
running = True
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')


def draw(x_pos, y_pos, color, size):
    # screen.blit(q,(x_pos,y_pos))
    screen.blit(q, (1677 - size, 0))
    pygame.draw.circle(screen, color , (x_pos, y_pos), size)
    pygame.display.flip()
    timer.tick(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

while running:
    size_text = font.render('Size : ' + str(size), True, 'black', 'cyan')
    color_text = font.render('Color : ' + str(color), True, color, "white")
    color_reset_text = font.render('Color : ' + str(color), True, 'white', "white")
    clear_text = font.render('Size : ' + str(size), True, 'white', 'white')
    screen.blit(size_text, (500, 0))
    screen.blit(color_text, (800, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            if event.y > event.x:
                size += 1
                screen.blit(clear_text, (620, 0))
            else :
                size -= 1
                screen.blit(clear_text, (620, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cursor_count += 1

    if pygame.mouse.get_pressed() == (True, False, False):
        x_pos, y_pos = pygame.mouse.get_pos()
        draw(x_pos, y_pos, color, size)
    if pygame.mouse.get_pressed() == (False, False, True):
        color = 'white'
    if size < 0 :
        size = 0
    keys = pygame.key.get_pressed()
    q = pygame.Surface((35 + size, 35 + size))
    q.fill(color)
    rect = pygame.Surface(( 35 + size * 2, 35 +size))
    rect.fill(color)
    if keys[pygame.K_1]:
        color = colors[0]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_2]:
        color = colors[1]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_3]:
        color = colors[2]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_4]:
        color = colors[3]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_5]:
        color = colors[4]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_6]:
        color = colors[5]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_7]:
        color = colors[6]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_8]:
        color = colors[7]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_9]:
        color = colors[8]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_0]:
        color = colors[9]
        screen.blit(color_reset_text, (800, 0))
    if keys[pygame.K_r]:
        screen.fill('white')
        pygame.display.flip()
        user_text = ''
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_b]:
        size = 35
        color = "black"
    if keys[pygame.K_s]:
        screen.blit(q, pygame.mouse.get_pos())
    if keys[pygame.K_SPACE]:
        screen.blit(rect, pygame.mouse.get_pos())
    if keys[pygame.K_d]:
        line_point1, line_point2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color , pygame.mouse.get_pos(), 6)
    if keys[pygame.K_l]:
        if line_point1 != 0 and line_point2 != 0:
            pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 6)
            time.sleep(0.1)
            pygame.draw.line(screen, color, (line_point1, line_point2), pygame.mouse.get_pos(),size - 33)
    if cursor_count < 0:
        cursor_count = 0
    cursor_count = cursor_count % 4
    pygame.mouse.set_cursor(cursors[(cursor_count)])
print(cursor_count)
pygame.quit()
