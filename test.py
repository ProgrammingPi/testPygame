import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1200, 800))
r = pygame.Rect(575, 375, 50, 50)
pygame.draw.rect(screen, (255, 0, 255), r, 0)

pygame.draw.circle(screen, (255,0,0), (600,400), 100, width=5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()