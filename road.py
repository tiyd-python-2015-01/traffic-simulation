import numpy as np

class Road:
    """The Road class is a storage object that will contain all of the
    cars created by the simulation.  The road may have a modifer that will
    indicate the difficulty of driving on this section of road and will
    be used to calculate the chance of slowdown by drivers throughout that
    section of road.

    Responsibilities:
    * Contains a list where each element in the list corresponds to 1 meter
      of road
    * Has a modifier variable that will be used to modify the slowdown chance
      of each car contained by the road object."""


    def __init__(self, modifier=1):
        self.road = np.zeros(1000).tolist()
        self.modifier = modifier

    def get_road_modifier(self):
        """Returns the slowdown modifier for this road object.  Default is 1"""
        return self.modifier

    def get_section(self, start, stop):
        """Returns a slice of the road"""
        return self.road[start:stop]

    def insert_car(self, car):
        """Inserts a car into the starting location of this road object"""
        for count in range(len(car)):
            self.road[count] = car
