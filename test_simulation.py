from car import Car
from simulation import Simulation


sim = Simulation()
buick = Car()
honda = Car(position=16)
miata = Car()
corvette = Car()
toyota = Car()
nova = Car()
car_list = [buick, honda]

def test_initialize_cars_on_road():
    sim3 = Simulation()
    sim3.initialize_car_list(30)
    assert len(sim3.car_list) == 30
    sim3.add_cars_to_road()


def check_buffer_zone():
    buick.position = 15
    honda.position = 34
    miata.position = 54
    corvette.position = 80
    sim1 = Simulation([buick, honda, miata, corvette])
    sim1.road.place_car(buick, honda, miata, corvette)
    assert sim1.check_buffer_zone(buick, honda) == True
    assert sim1.is_car_in_range(honda, miata) == True
    assert sim1.is_car_in_range(miata, corvette) == False


def test_check_for_crash():
    buick.current_speed = 20
    honda.position = 25
    corvette.position = 26
    corvette.current_speed = 2
    miata.position = 29
    toyota.position = 990
    sim = Simulation([buick, honda, corvette, toyota])
    assert sim.check_for_crash(toyota, buick) == True
    assert sim.check_for_crash(buick, honda) == True
    assert sim.check_for_crash(buick, corvette) == False
    assert sim.check_for_crash(corvette, miata) == True

def test_find_next_car():
    sim = Simulation(car_list)
    assert sim.find_next_car(buick) == honda


def test_accelerate_or_deccelerate():
    buick.current_speed = 20
    sim.accelerate_or_deccelerate(buick)
    assert buick.current_speed != 20

def test_match_car_speed():
    buick.current_speed = 28
    honda.current_speed = 20
    sim.match_car_speed(buick, honda)
    assert buick.current_speed and honda.current_speed == 20

def test_check_buffer_zone():
    buick.position = 974
    honda.position = 999
    miata.position = 976
    corvette.position = 1
    nova.position = 28
    sim_buffer = Simulation()
    assert sim_buffer.check_buffer_zone(buick, honda) == True
    assert sim_buffer.check_buffer_zone(honda, corvette) == True
    assert sim_buffer.check_buffer_zone(corvette, nova) == False

def test_cars_are_moving():
    sim = Simulation(car_list)
    buick.current_speed = 20
    honda.current_speed = 25
    position_b = buick.position
    position_h = honda.position
    sim.one_second()
    assert position_b != buick.position
    assert position_h != honda.position
