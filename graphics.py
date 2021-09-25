"""Este arquivo realiza a parte gráfica do programa, utilizando a
biblioteca pygame."""

import pygame
from pygame.locals import Rect, QUIT
from draw import *
from sys import exit
from _thread import *

def draw_city(map):
    # Inciando o pygame
    pygame.init()
    screen = pygame.display.set_mode((975,725),0,32)
    pygame.display.set_caption("Transito da Cidade")    
    inicialize_imgs()

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

            # Desenhar semáforos
            if map[i][j]["type"] == "sem":
                if map[i][j]["car"]:
                    draw_sem(map[i][j]["sem"].colorV, map[i][j]["car"], map, screen, retangulo)
                else:
                    draw_sem(map[i][j]["sem"].colorV, None, map, screen, retangulo)
            
            # Desenhar quadras
            elif map[i][j]["type"] == "quadra":
                draw_quadra(screen, retangulo)

            # Desenhar ruas e carros
            elif map[i][j]["type"] != "quadra":
                if map[i][j]["car"]:
                    draw_car(i, j, screen, retangulo)
                else:
                    draw_street(i, j, screen, retangulo)
            
        y += rect_size
        x = 0
    
    # Desenhando o contador de iteração na tela
    opensans = pygame.font.SysFont('opensanscondensed', 25)
    contador = f'Iteração: = {cont}'
    texto = opensans.render(contador, True, (255, 255, 255))
    screen.blit(texto, (0, 0))

    pygame.display.update()


# Loop do Pygame
def loop(temp):
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()