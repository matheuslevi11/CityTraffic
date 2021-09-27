from street_directions import *

class Semaforo:
    def __init__(self):
        self.colorH = 'r'
        self.colorV = 'g'
        self.greenTime = 5
        self.redTime = 12
        self.time = 0

    def update(self):
        self.time += 1
        if self.time <= self.greenTime:
            self.colorV = 'g'
            self.colorH = 'r'
        elif self.time < self.greenTime + 2:
            self.colorV = 'y'
        else:
            self.colorV = 'r'
            self.colorH = 'g'

        if self.time == self.redTime: self.time = 0
    
    def fluxo(self, map, x, y):
        flow = []
        counter = 0
        d = get_street_direction(map, x, y)
        # Checando horizontalmente
        dir_map = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
        for i in range(0, 7):
            x += dir_map[d[0]-1][0]
            y += dir_map[d[0]-1][1]
            if x < 0 or x > 27 or y < 0 or y > 36:
                break
            if map[x][y]['type'] == 'quadra': break
            if map[x][y]["car"] is not None:
                counter += 1
        flow.append(counter)
        # Checando verticalmente
        counter = 0
        for i in range(0, 7):
            x += dir_map[d[1]-1][0]
            y += dir_map[d[1]-1][1]
            if x < 0 or x > 27 or y < 0 or y > 36:
                break
            if map[x][y]['type'] == 'quadra': break
            if map[x][y]["car"] is not None:
                counter += 1
        flow.append(counter)
        return flow
    
class Car:
    def __init__(self, id, directs, position):
        self.id = id
        self.directions = directs
        self.pos = position

    # Retorna o semáforo na direção do carro
    def get_street_sem(self, map):
        x = self.pos[0]
        y = self.pos[1]
        x, y = self.walk_street(map, x, y)
        if x > 27 or y > 36 or x < 0 or y < 0:
            return None
        if map[x][y]["type"] == "sem":
            return map[x][y]["sem"]
        return None

    # Retorna a próxima posição de acordo com a direção da rua
    def walk_street(self, map, x, y, d=0):
        if d != 0:
            direction = d
        else:
            direction = get_street_direction(map, x, y)
        dir_map = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
        x += dir_map[direction-1][0]
        y += dir_map[direction-1][1]
        return x,y

    # Faz o carro andar
    def drive(self, map):
        x = self.pos[0]
        y = self.pos[1]
        if map[x][y]["type"] == "sem":
            self.choose_direction(map)
            return 1
        orientation = get_street_type(x, y)
        sem = self.get_street_sem(map)

        if sem is None:
            # Se não existe semáforo a frente, simplesmente ande
            x, y = self.walk_street(map, x, y)
            #if self.pos[0] == 0:
                #print(f"tentando ir de [{self.pos[0]}][{self.pos[1]}] para [{x}][{y}]")
            self.move_car(map, x, y)
            return
        if orientation == 'h':
            if sem.colorH == 'g':
                # Ande se o sinal estiver verde
                x, y = self.walk_street(map, x, y)
                self.move_car(map, x, y)
        elif orientation == 'v':
            if sem.colorV == 'g':
                # Ande se o sinal estiver verde
                x, y = self.walk_street(map, x, y)
                self.move_car(map, x, y)
        return 0
                
    # Decide o caminho do carro
    def choose_direction(self, map):
        x = self.pos[0]
        y = self.pos[1]
        possible_dirs = get_street_direction(map, x, y)
        
        for d in self.directions:
            if d in possible_dirs:
                backup_x, backup_y = x, y
                x, y = self.walk_street(map, x, y, d)
                if self.move_car(map, x, y):
                    return
                else:
                    x = backup_x
                    y = backup_y


    # Move o carro na matriz
    def move_car(self, map, x, y):
        if x < 0 or x > 27 or y < 0 or y > 36:
            return 0
        if map[x][y]["car"] is None:
            map[x][y]["car"] = self
            map[self.pos[0]][self.pos[1]]["car"] = None
            self.pos[0] = x
            self.pos[1] = y
            return 1
        return 0