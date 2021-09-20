"""Este arquivo contém o código que armazena a direção das ruas,
de acordo com o padrão."""

from classes import Direction

"""
Direções: 
1 - cima
2 - direita
3 - baixo
4 - esquerda
"""

def get_street_direction(map, x, y):
    if x == 0 and y == 0:
        return 2
    if x == 0 and y == 36:
        return 3
    if x == 27 and y == 0:
        return 1
    if x == 27 and y == 36:
        return 4
    dirs = Direction()
    if map[x][y]["type"] == "sem":
        h_street = int(x / 3)
        v_street = int(y / 4)
        direc1 = dirs.horizontal[h_street]
        direc2 = dirs.vertical[v_street]
        return direc1, direc2
    if x % 3 == 0:
        h_street = int(x / 3)
        direc = dirs.horizontal[h_street]
        return direc
    else:
        v_street = int(y / 4)
        direc = dirs.vertical[v_street]
        return direc

