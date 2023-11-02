import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Programming Fundamentals")

x_coordinate = 500
y_coordinate = 300

running = True
while running == True:
    for event in pyagme.event.get():
        pygame.draw.rect(screen, (255,255,255), (x_coordinate, y_coordinate, 50, 50))

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate

