"""Este arquivo realiza a parte gráfica do programa, utilizando a
biblioteca pygame para tal."""

from time import sleep
from main import mapaFinal
import pygame
from pygame.locals import Rect, QUIT
from constructor import build_city
from street_directions import get_street_direction
from sys import exit

def draw_city(map):
    x = 0
    y = 0
    rect_size = 25
    for i in range(0, 28):
        for j in range(0, 37):
            x += rect_size
            retangulo = Rect(x, y, rect_size, rect_size)
            color = (220, 220, 220)
            if map[i][j]["type"] == "sem":
                color = (0, 240, 0)
            if map[i][j]["type"] == "quadra":
                color = (0, 0, 240)
            if map[i][j]["type"] != "quadra":
                if map[i][j]["car"]:
                    color = (240, 0, 0)
            
            pygame.draw.rect(screen, color, retangulo)
        y += rect_size
        x = 0

# Inciando o pygame
pygame.init()
screen = pygame.display.set_mode((975,725),0,32)
pygame.display.set_caption("Transito incrível da titia roberta")

# Desenhando o mapa na tela
screen.fill((142,215,23))
map = build_city()
draw_city(map)
pygame.display.flip()
print("Apagando a tela")
screen.fill((0,0,0))
sleep(1)
map = mapaFinal()
print("desenhando o estado final")
draw_city(map)
pygame.display.update()


# Loop do Pygame
while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()


