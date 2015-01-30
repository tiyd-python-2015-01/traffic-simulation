import numpy as np
import random
from car import Car
from road import Road


class Simulator:
    """The simulator class

    Responsibilities:
      *Checks car locations in relation to each other
      *Sends signals to cars if they are too close or a collision will occur
      *Updates the positions of each car within the road object each turn
      *Keeps a cumulative average and standard deviation for eacn car
       for each section of road

      Collaborators:
       *Uses information provided by the car class to update locations
        within the road class
       *Uses the road objects to keep track of car locations in relation to
        each other.
    """


    def __init__(self, car_types, roads):
        self.cars = []
        self.car_types = car_types
        self.roads = roads

    def create_car(self):
        """Creates a new car object of random type and puts it onto the road"""
        new_car = random.randomchoice(self.car_types)()
        self.place_car_on_road(new_car)

    def next(self):
        pass

    def place_car_on_road(self, new_car):
        """Places a car into the road object in the initial location"""
        for count in range(len(new_car)):
            self.roads[0] = new_car

    def start(self):
        """Fills the road with cars.  Returns when the road is full and
        enough iterations have run to ensure a good flow of random traffic."""
        car_count, iterations, next_car_count = 0

        while car_count < 30 * len(roads):
            if iterations == next_car_at:
                self.create_car()
                next_car_at = iterations + np.random.randint(2, 7)
                car_count += 1
            iterations += 1
