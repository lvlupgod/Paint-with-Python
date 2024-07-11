import pygame
import math
from random import randint

level = []

pygame.init()

modes = pygame.display.list_modes()
WIDTH, HEIGHT = modes[0]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
running = True
q = pygame.Surface((32, 32))
q.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

pygame.quit()