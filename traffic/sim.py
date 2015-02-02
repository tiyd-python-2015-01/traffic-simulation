import numpy as np
import random


class Sim():
    """
    Restarts a car's speed to 0, if hits another car
    manages time (in seconds)
    When you start, add 30 cars to the road per km, evenly spaced
    Then run the simulation for 1 minute to get a continuous, randomized
    stream of traffic.
    """

    def __init__(self):
        self.crash_count = 0

    def add_car(self, roadway, car):
        roadway.track[0, car.location] += 1
        return roadway

    def remove_car(self, roadway, car):
        roadway.track[0, car.location] -= 0
        return roadway

    def move_cars_on_road(self, roadway, cars):
        for car in cars:
            self.remove_car(roadway, car)
            car.update_speed_to_loc()
            self.move_rules(cars)
            self.add_car(roadway, car)
        return roadway

    def move_rules(self, cars):
        counter = 1
        for car in cars:
            if car.is_car_too_close(cars[counter]):
                car.too_close_car(cars[counter])
            if counter == (len(cars) - 1):
                counter = 0
            else:
                counter += 1
        return True

    def car_impact(self, cars):
        counter = 1
        for car in cars:
            if car.did_hit_car(cars[counter]):
                self.crash_count += 1
            if counter == (len(cars) - 1):
                counter = 0
            else:
                counter += 1

    def increase_car_speed(self, cars):
        for car in cars:
            car.rising_speed()

    def m_to_km_conversion(num):
        return num * (3600/1000)
