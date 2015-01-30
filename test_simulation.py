from car import Car
from road import Road
from simulation import Simulation


sim = Simulation()
buick = Car()
honda = Car(position=16)
car_list = [buick, honda]

def test_add_car():
    sim.add_car()
    assert sim.road.road[1] == 1
    sim.add_car(12)
    assert sim.road.road[12] == 1
    assert len(sim.car_list) == 2

def test_randomly_slow_down():
    assert sim.randomly_slow_down() == False or sim.randomly_slow_down() == True

def test_cars_are_moving():
    sim = Simulation(car_list)
    position_b = buick.position
    position_h = honda.position
    sim.one_second()
    assert position_b != buick.position
    assert position_h != honda.position
