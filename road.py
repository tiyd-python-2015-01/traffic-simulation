import numpy as np

class Road:

    def __init__(self):

        self.length = 999

        self.roads = np.zeros(self.length + 1)

class HardRoad(Road):

    def __init__(self):

        self.length = 999

        self.roads = np.zeros(self.length + 1)

        self.length = 6999
