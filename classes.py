class Car:
    def __init__(self, id, directs, position):
        self.id = id
        self.directions = directs
        self.pos = position

class Direction:
    def __init__(self):
        self.horizontal = [2,4,4,4,4,2,4,4,4,4]
        self.vertical = [1,3,1,1,3,1,3,3,1,3]

class Semaforo:
    def __init__(self):
        self.colorH = 'g'
        self.colorV = 'r'
        self.greenTime = 5
        self.time = 0

    def update(self):
        self.time += 1
        if self.time <= self.greenTime:
            self.colorH = 'g'
            self.colorV = 'r'
        elif self.time < self.greenTime + 2:
            self.colorH = 'y'
        else:
            self.colorH = 'r'
            self.colorV = 'g'

        if self.time == 10: self.time = 0