import numpy as np
from car import Car


class Simulation:
    def __init__(self, road, duration=60, number_of_cars=30):
        self.road = road
        self.time = 0
        self.number_of_cars = number_of_cars
        self.duration = duration
        self.representation = np.zeros((duration, road.length))
        self.speeds = np.zeros((duration, number_of_cars))

    def click_time_forward(self):
        self.time += 1
        self.road.move_cars()

    def update_results(self):
        position_list = self.road.get_approx_car_positions()
        def is_a_car_there(position_index, position_list):
            if position_index in position_list:
                return 1
            else:
                return 0
        position_vector = [is_a_car_there(index, position_list)
                           for index in range(self.road.length)]
        self.representation[self.time] += position_vector
        self.speeds[self.time] += self.get_car_speeds()


    def return_representation(self):
        return self.representation

    def place_evenly_spaced_cars(self):
        """Generate a number of cars, default 30, and place them evenly
        on the road."""
        car_positions = np.linspace(0, self.road.length, self.number_of_cars)
        for position in car_positions:
            car = Car(position=position)
            self.road.place_car(car)

    def get_num_cars(self):
        return self.road.get_num_cars()

    def get_car_speeds(self):
        """Gets a list of car speeds"""
        return self.road.get_car_speeds()

    def run_simulation(self):
        self.place_evenly_spaced_cars()
        for time in range(self.duration):
            self.update_results()
            self.click_time_forward()
