import pygame

pygame.init()

ancho = (800)
alto= (600)

screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit
