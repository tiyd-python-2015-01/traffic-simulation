import numpy as np


class Road:
    def __init__(self, length=1000):
        self.length = length #  length in meters
        self.cars = []

    def place_car(self, car):
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            # First check if the car wants to match speed
            if car.is_within_range_of_bumper(self.cars):
                car.match_speed(self.cars)
            # Otherwise randomly decelerate
            elif car.random_deceleration():
                car.decelerate()
            # Or accelerate to max speed
            elif car.accelerate_condition():
                car.accelerate()

            # Last, move the cars, but stop them if they're about to collide.
            # if car.will_hit_car(self.cars):
            #     car.stop()
            # else:
            #     car.move()
            car.move()

    def get_approx_car_positions(self):
        "Gives a list of car positions as ints."
        return [int(car.position) for car in self.cars]

    def get_num_cars(self):
        return len(self.cars)

    def get_car_speeds(self):
        return [car.speed for car in self.cars]
