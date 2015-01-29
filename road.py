import numpy as np

class Road:
    def __init__(self, length=100):
        self.length=length
        self.blank_road = np.zeros(length, int)

    def give_position(self, car):
        pass

    def place_car(self, car, position):
        pass
