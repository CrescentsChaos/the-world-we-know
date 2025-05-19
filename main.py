import pygame

pygame.init()

#game window
screen_width = 1920*0.8
screen_height = 1080*0.8

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

run= True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()  # Update the display