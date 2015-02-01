import numpy as np


class Road:
    """
    Responsibilities:
    - Keeps the position of cars

    Collaborators
    - Cars travel on the Road
    """

    def __init__(self, length=1000):
        self.length = length
        self.reset()

    def place_car(self, *args):
        """initializes car on the road at the cars position,
        changes all 0's on the road array to 1's for the car's length"""
        for car in args:
            position = car.position
            length = car.length
            self.road[position:(position + length)] = 1

    def reset(self):
        self.road = np.zeros(self.length)
