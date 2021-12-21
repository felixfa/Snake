import pygame

pygame.init()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            running = False