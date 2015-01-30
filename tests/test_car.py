import numpy as np
from traffic_simulation.car import Car

def test_len():
    new_car = Car()
    assert len(new_car) == 5


def test_slow_down():
    np.random.seed(24)
    new_car = Car()
    new_car.speed = 20
    new_car.random_slowdown()
    assert new_car.speed == 18
    np.random.seed(23)
    new_car.random_slowdown()
    assert new_car.speed == 18


def test_increase_speed_report_speed():
    new_car = Car()
    new_car.increase_speed()
    assert new_car.report_speed() == 2
    new_car.speed = 33
    new_car.increase_speed()
    assert new_car.report_speed() == 33.333
