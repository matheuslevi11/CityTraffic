"""Este arquivo se destina a iniciar as imagens e desenhá-las na tela"""
import pygame
from constructor import build_city
from street_directions import get_street_direction

map = build_city()

def inicialize_imgs():
    # Quadras e ruas
    global quadra_tile, street_tile, streetH_tile, streetV_tile
    quadra_src = pygame.image.load('images/grass.png').convert_alpha()
    quadra_tile = pygame.transform.scale(quadra_src, (25, 25))
    street_src = pygame.image.load('images/street.png').convert_alpha()
    street_tile = pygame.transform.scale(street_src, (25, 25))
    streetH_src = pygame.image.load('images/streetH.png').convert_alpha()
    streetH_tile = pygame.transform.scale(streetH_src, (25, 25))
    streetV_src = pygame.image.load('images/streetV.png').convert_alpha()
    streetV_tile = pygame.transform.scale(streetV_src, (25, 25))

    # Carros
    global car_tile, carH_tile, carV_tile
    carH_src = pygame.image.load('images/carH.png').convert_alpha()
    carH_tile = pygame.transform.scale(carH_src, (25, 25))
    carV_src = pygame.image.load('images/carV.png').convert_alpha()
    carV_tile = pygame.transform.scale(carV_src, (25, 25))

    # Semáforos
    global semG_tile, semY_tile, semR_tile
    semG_src = pygame.image.load('images/semG.png').convert_alpha()
    semG_tile = pygame.transform.scale(semG_src, (25, 25))
    semY_src = pygame.image.load('images/semY.png').convert_alpha()
    semY_tile = pygame.transform.scale(semY_src, (25, 25))
    semR_src = pygame.image.load('images/semR.png').convert_alpha()
    semR_tile = pygame.transform.scale(semR_src, (25, 25))

    # Carros em semáforos
    global semRcarH_tile, semRcarV_tile, semGcarH_tile
    global semGcarV_tile, semYcarH_tile, semYcarV_tile
    semRcarH_src = pygame.image.load('images/semRcarH.png').convert_alpha()
    semRcarH_tile = pygame.transform.scale(semRcarH_src, (25, 25))
    semRcarV_src = pygame.image.load('images/semRcarV.png').convert_alpha()
    semRcarV_tile = pygame.transform.scale(semRcarV_src, (25, 25))
    semGcarH_src = pygame.image.load('images/semGcarH.png').convert_alpha()
    semGcarH_tile = pygame.transform.scale(semGcarH_src, (25, 25))
    semGcarV_src = pygame.image.load('images/semGcarV.png').convert_alpha()
    semGcarV_tile = pygame.transform.scale(semGcarV_src, (25, 25))
    semYcarH_src = pygame.image.load('images/semYcarH.png').convert_alpha()
    semYcarH_tile = pygame.transform.scale(semYcarH_src, (25, 25))
    semYcarV_src = pygame.image.load('images/semYcarV.png').convert_alpha()
    semYcarV_tile = pygame.transform.scale(semYcarV_src, (25, 25))


def draw_quadra(screen, retangulo):
    global quadra_tile
    screen.blit(quadra_tile, retangulo)

def draw_street(x, y, screen, retangulo):
    global street_tile, streetH_tile, streetV_tile

    direct = get_street_direction(map, x, y)
    
    if x == 0 and y == 0:
        screen.blit(street_tile, retangulo)
    elif x == 0 and y == 36:
        screen.blit(street_tile, retangulo)
    elif x == 27 and y == 0:
        screen.blit(street_tile, retangulo)
    elif x == 27 and y == 36:
        screen.blit(street_tile, retangulo)
    elif direct == 1 or direct == 3:
        screen.blit(streetV_tile, retangulo)
    else:
        screen.blit(streetH_tile, retangulo)

def draw_car(x, y, screen, retangulo):
    global carH_tile, carV_tile

    direct = get_street_direction(map, x, y)
    
    if direct == 1 or direct == 3:
        screen.blit(carV_tile, retangulo)
    else:
        screen.blit(carH_tile, retangulo)

def draw_sem(color, car, map, screen, retangulo):
    global semR_tile, semG_tile, semY_tile
    global semRcarH_tile, semRcarV_tile, semGcarH_tile
    global semGcarV_tile, semYcarH_tile, semYcarV_tile
    if car is None:
        if color == 'r':
            screen.blit(semR_tile, retangulo)
        elif color == 'g':
            screen.blit(semG_tile, retangulo)
        else:
            screen.blit(semY_tile, retangulo)
    else:
        x = car.pos[0]
        y = car.pos[1]
        possible_dirs = get_street_direction(map, x, y)
        
        heading_direction = 0
        # Descobrindo a direção em que o carro tá indo
        for d in car.directions:
            if d in possible_dirs:
                backup_x, backup_y = x, y
                x, y = car.walk_street(map, x, y, d)
                if x < 0 or x > 27 or y < 0 or y > 36:
                    continue
                if map[x][y]["car"] is None:
                    heading_direction = d
                    break
                x = backup_x
                y = backup_y
                
        if heading_direction == 1 or heading_direction == 3:
            orient = 0 # direção vertical
        else:
            orient = 1 # direção horizontal

        if color == 'r':
            if orient:
                screen.blit(semRcarH_tile, retangulo)
            else:
                screen.blit(semRcarV_tile, retangulo)
        elif color == 'g':
            if orient:
                screen.blit(semGcarH_tile, retangulo)
            else:
                screen.blit(semGcarV_tile, retangulo)
        else:
            if orient:
                screen.blit(semYcarH_tile, retangulo)
            else:
                screen.blit(semYcarV_tile, retangulo)



        