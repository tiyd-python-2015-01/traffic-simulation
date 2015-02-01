from car import Car
from road import Road
import random
import numpy as np

class Simulation:
    """
    Responsibilities:
    - Creates new cars to be put on the road
    - Moves cars over time
    - Records traffic data

    Collaborators:
    - Has a road filled with cars
    """

    def __init__(self, car_list=[]):
        self.road = Road()
        self.car_list = car_list
        self.iterations = 0

    def initialize_car_list(self, number_of_cars):
        increment = round(self.road.length / number_of_cars+1)
        p = 0
        for i in range(number_of_cars):
            car = Car(p)
            self.car_list.append(car)
            p += increment

    def add_cars_to_road(self):
        for car in self.car_list:
            self.road.place_car(car)

    def accelerate_or_deccelerate(self, car):
        """Randomly deccelerates the car 10 percent of the time"""
        if random.random() < .1:
            car.deccelerate()
        else:
            car.accelerate()

    def find_next_car(self, main_car):
        for idx, car in enumerate(self.car_list):
            if car == main_car:
                return self.car_list[idx + 1]

    def match_car_speed(self, fast_car, slow_car):
        """match the current_speed of a slower car"""
        fast_car.current_speed = slow_car.current_speed

    def check_for_crash(self, car, next_car):
        """Scans for any cars that it will encounter if traveling
        at the same speed"""
        next_space = (car.position + car.length + car.current_speed) % 1000
        car_ahead = next_car.position
        return next_space >= car_ahead

    def check_buffer_zone(self, car, next_car):
        if car.position < 975:
            return (next_car.position - car.position) <= 25
        else:
            return (next_car.position + 1000 - car.position) <= 25

    def one_second(self):
        """A one second iteration of the simulation"""
        self.road.reset()
        for car, car_ahead in zip(self.car_list, self.car_list[1:]+self.car_list[:1]):
            if car.current_speed > 25 and self.check_for_crash(car, car_ahead):
                self.match_car_speed(car, car_ahead)
            elif self.check_buffer_zone(car, car_ahead):
                self.match_car_speed(car, car_ahead)
            else:
                self.accelerate_or_deccelerate(car)
            car.move()
            self.road.place_car(car)


    def run_simulation(self, seconds):
        """ Runs the a one second iteration for a number of seconds"""
        car_position_array = np.zeros(shape=(seconds, 30))
        car_speed_array = np.zeros(shape=(seconds, 30))
        self.car_list = []  # Clear car list
        self.initialize_car_list(30)
        self.add_cars_to_road
        for i in range(seconds):
            self.one_second()
            car_position_array[i] = [car.position for car in self.car_list]
            car_speed_array[i] = [car.current_speed for car in self.car_list]
        return car_position_array, car_speed_array


    def get_car_speeds(self):
        """Iterates through the car list and returns the current speed of each
        car"""
        car_speeds = []
        for car in self.car_list:
            car_speeds.append(car.current_speed)
        return car_speeds
