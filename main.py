from constructor import build_city
from time import sleep


map = build_city()
#view = draw_city(map)
for iteration in range(0, 1001):
    # Mover todos os carros
    for i in range(0, 28):
        for j in range(0, 37):
            if map[i][j]["type"] != "quadra":
                if map[i][j]["car"] is not None:
                    map[i][j]["car"].drive(map)

    # Clock de todos os semáforos
    for i in range(0, 28):
        for j in range(0, 37):
            if map[i][j]["type"] == "sem":
                map[i][j]["sem"].update()
    #update_city(map)
    sleep(0.005) # 50 milisegundos de delay