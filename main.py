from constructor import build_city
from time import sleep
from graphics import draw_city, update_city


map = build_city()

view = draw_city(map)

for iteration in range(0, 1001):
    # Mover todos os carros
    movedcars = []
    for i in range(0, 28):
        for j in range(0, 37):
            if map[i][j]["type"] != "quadra":
                if map[i][j]["car"] is not None:
                    id = map[i][j]["car"].id
                    if id not in movedcars:
                        movedcars.append(id)
                        map[i][j]["car"].drive(map)


    # Clock de todos os semáforos
    for i in range(0, 28):
        for j in range(0, 37):
            if map[i][j]["type"] == "sem":
                #fluxo = map[i][j]["sem"].fluxo()
                #if fluxo > 3:
                    #sem[i][j]
                map[i][j]["sem"].update()
    update_city(map, view, iteration)
    sleep(0.05) # 50 milisegundos de delay 00