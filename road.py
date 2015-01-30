import numpy as np


class Road:
    def __init__(self, length=100):
        self.length = length
        self.blank_road = np.zeros(length, int)
        self.cars = []
        self.car_positions = {}

    def give_position_of_car(self, car):
        return self.car_positions[car]

    def place_car(self, car, position=0):
        self.cars.append(car)
        self.car_positions[car] = position
