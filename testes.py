import pygame
from pygame.locals import Rect, QUIT

pygame.init()
screen = pygame.display.set_mode((975,725),0,32)
pygame.display.set_caption("Transito da Cidade")
screen.fill((142,215,23))

x = 0
y = 0
rect_size = 25
x += rect_size
retangulo = Rect(x, y, rect_size, rect_size)

img = pygame.image.load('images/car.jpg').convert_alpha()
imgR = pygame.transform.scale(img, (rect_size, rect_size))
screen.blit(imgR, retangulo)
pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()