import pygame
import random


pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Programming Fundamentals")

x_coordinate = 500
y_coordinate = 300


running = True
pygame.time.Clock().tick(60)

while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (random.randint(100,255),random.randint(0,50),random.randint(0,100)), (x_coordinate, y_coordinate, 50, 50))
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate -= 0.1

    if button[pygame.K_RIGHT]:
        x_coordinate += 0.1

    if button[pygame.K_UP]:
        y_coordinate -= 0.1

    if button[pygame.K_DOWN]:
        y_coordinate += 0.1

    if x_coordinate < 0:
        x_coordinate = 0

    if y_coordinate < 0:
        y_coordinate = 0

    pygame.display.flip()