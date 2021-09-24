"""Este arquivo realiza a parte gráfica do programa, utilizando a
biblioteca pygame para tal."""

from time import sleep
import pygame
from pygame.locals import Rect, QUIT
from constructor import build_city
from street_directions import get_street_direction
from sys import exit
from _thread import *

def draw_city(map):
    # Inciando o pygame
    pygame.init()
    screen = pygame.display.set_mode((975,725),0,32)
    pygame.display.set_caption("Transito da Cidade")

    # Desenhando o mapa na tela
    screen.fill((142,215,23))
    update_city(map, screen, 0)
    pygame.display.flip()
    start_new_thread(loop, (0,))
    return screen

def update_city(map, screen, cont):
    screen.fill((142,215,23))
    x = 0
    y = 0
    rect_size = 25
    for i in range(0, 28):
        for j in range(0, 37):
            x += rect_size
            retangulo = Rect(x, y, rect_size, rect_size)
            color = (220, 220, 220)
            if map[i][j]["type"] == "sem":
                if map[i][j]["sem"].colorH == 'r':
                    color = (255, 0, 0)
                elif map[i][j]["sem"].colorH == 'g':
                    color = (0, 255, 0)
                else:
                    color = (255, 215, 25)
            if map[i][j]["type"] == "quadra":
                color = (173, 216, 230)
            if map[i][j]["type"] != "quadra":
                if map[i][j]["car"]:
                    color = (0, 0, 0)
            
            pygame.draw.rect(screen, color, retangulo)
        y += rect_size
        x = 0
    
    opensans = pygame.font.SysFont('arial', 30)
    contador = f'Iteração: = {cont}'
    texto = opensans.render(contador, True, (255, 0, 0))
    screen.blit(texto, (0, 0))

    pygame.display.update()

# Loop do Pygame
def loop(temp):
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()