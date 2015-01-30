import numpy as np


class Car:
    """ The car class will be the base class to keep track of information
    pertaining to each car on the road during the traffic simulation.  It
    will be extended by other classes to implement different types of drivers.

    Responsibilities:
    * Store current car speed
    * Store current car location
    * Store basic car info like max speed and length of car
    * Store rules for acceleration
    * Store rules for deceleration
    """


    def __init__(self):
        self.speed = 0
        self.acceleration = 2
        self.max_speed = 33.333
        self.length = 5
        self.position = np.array([0, 4])

    def __len__(self):
        """Provide an easy way to reference the lenght of the car so the
        simulation can determine how many elements in the road list
        the car should occupy.  This is more relevant to implementation of
        different car types."""
        return self.length

    def random_slowdown(self):
        """When called slows the car down by 2 meters per second 10% of the
        time"""
        if np.random.random() > .9:
            self.speed -= 2

    def too_close(self, speed_to_match):
        """Will be called if the simulation determines the car is within 4
        car lengths of another car.  Will be provided ther current speed of
        the car that is too close and will set current speed to speed of
        the car ahead."""
        self.speed = speed_to_match

    def increase_speed(self):
        """Increases the speed of the car if it is not already going its max
        speed.  If the cars acceleration will exceed max speed, then current
        speed is set to max speed"""
        if self.speed + 2 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 2

    def update_position(self):
        """Calculates and returns the car's new position within the road
        object's list"""
        self.position += round(self.speed)
        return self.position

    def report_speed(self):
        """Returns the current speed of the car for data tracking by the
        simulation"""
        return self.speed
