from road import Road
from car import Car


def test_road_init():
    road = Road(length=10)
    assert road.length == 10


def test_road_add_car():
    road = Road()
    car_to_add = Car()
    road.place_car(car_to_add)
    assert len(road.cars) == 1
