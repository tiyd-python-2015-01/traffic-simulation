import numpy as np


class Road:
    """
    Responsibilities:
    - Keeps the position of cars
    - Tells car if other car is within range

    Collaborators
    - Cars travel on the Road
    """

    def __init__(self, length=1000):
        self.length = length
        self.reset()

    def place_car(self, car):
        """initializes car on the road at the cars position,
        changes all 0's on the road array to 1's for the car's length"""
        position = car.position
        length = car.length
        self.road[position:(position + length)] = 1

    def is_car_in_range(self, car):
        """Returns true if car if it is within 20 meters"""
        location = car.position
        length = car.length
        buffer_beginning = location + car.length
        buffer_end = location + 4 * car.length + 1
        return self.road[buffer_beginning:buffer_end].any() == 1


    def reset(self):
        self.road = np.zeros(self.length)
