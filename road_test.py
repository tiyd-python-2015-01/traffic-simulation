from road import Road
from car import Car


buttonwood = Road()
buick = Car()
honda = Car()

def test_length():
    assert buttonwood.length == 1000
    assert len(buttonwood.road) == 1000

def test_car_position():
    buick.position = 15
    buttonwood.place_car(buick)
    assert buttonwood.road[15:20].all() == 1

def test_car_in_range():
    buick.position = 15
    honda.position = 35
    buttonwood.place_car(buick)
    buttonwood.place_car(honda)
    assert buttonwood.is_car_in_range(buick) == True
    assert buttonwood.is_car_in_range(honda) == False

def test_road_reset():
    buttonwood.road[15:20] = 1
    buttonwood.reset()
    assert buttonwood.road.all() == 0
