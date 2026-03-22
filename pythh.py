import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))  # needs tuple
pygame.display.set_caption("My First pygame window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing should be inside the loop
    screen.fill((100, 150, 200))
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 50))
    pygame.display.flip()

pygame.quit()
sys.exit()