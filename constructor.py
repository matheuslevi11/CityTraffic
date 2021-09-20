"""O conteúdo deste arquivo destina-se a preparar a cidade instanciando
os carros que nela residem."""

import classes
import mapa

def build_city():

    # Criando uma lista com todos os tipos de direções de carros
    all_directions = []
    all_directions.append([1,4,3,2])
    all_directions.append([1,2,3,4])
    all_directions.append([3,4,1,2])
    all_directions.append([3,2,1,4])
    all_directions.append([4,3,2,1])
    all_directions.append([2,3,4,1])
    all_directions.append([4,1,2,3])
    all_directions.append([2,3,4,1])
    all_directions.append([1,4,3,2])
    all_directions.append([1,2,3,4])

    map = mapa.create_map()


    # Criando todos os carros e adicionando eles nas ruas
    d = 0
    for i in range(1, 101):
        x,y = calculate_inicial_pos(i, map)
        pos = [x, y]
        newCar = classes.Car(i, all_directions[d], pos)
        map[x][y]["car"] = newCar
        d += 1
        d = d % len(all_directions)

    return map

def calculate_inicial_pos(id, map):
    h_gap = 3
    v_gap = 4

    if id == 100:
        x = 5*h_gap
        y = 5*v_gap-1
        # Procurando um lugar vazio para colocar o carro
        while map[x][y]["car"] != None:
            y += 1
        return x, y
    
    if id < 10:
        zero = "0"
        id = zero + str(id)

    id = str(id)
    id = id.replace("0", "5")
  
    x = int(id[0]) * h_gap
    y = (int(id[1]) - 1) * v_gap + 1

    
    while map[x][y]["car"] != None:   
        y += 1

    return x,y