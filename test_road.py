import numpy as np

from road import Road
from car import Car


def test_road_init():
    road = Road(length=10)
    assert len(road.blank_road) == 10

def test_road_add_car():
    road = Road(length=10)
    car_to_add = Car()
    road.place_car(car_to_add)
