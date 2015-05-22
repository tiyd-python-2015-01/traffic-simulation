from road import Road
import random


class Car:

    def __init__(self, desired_speed, speed, road, start_location):

        self.speed = speed
        self.road = road
        self.location = start_location
        self.desired_speed = desired_speed

    def slow(self):
        """slows the car by 2 m/s"""
        if self.speed > 1:
            self.speed -= 2

    def acc(self):
        """Accellerates the car by 2 m/s"""
        if self.speed < self.desired_speed:
            self.speed += 2

    def check_location(self):
        """Makes sure car wont drive off the map"""
        if self.location + self.speed <= self.road.length:
            return True

    def move_car(self):
        """Moves car up as many spaces as its speed"""
        self.location += self.speed

    def loop_car(self):
        """ for cars at end of track puts it to a beginning location based on
        speed"""

        def adjust_ratio():
            return (self.location + self.speed) - self.road.length
        self.location = adjust_ratio()

    def go(self):
        """Moves the cars after checking driving logic"""
        if self.check_location():
            self.move_car()
        else:
            self.loop_car()
