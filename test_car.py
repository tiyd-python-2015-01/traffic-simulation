from car import Car

def test_accelerate():
    car = Car()
    car.speed = 20
    car.speed = car.accelerate()
    assert car.speed == 22

    car2 = Car()
    car2.speed = 32
    car2.speed = car2.accelerate()
    assert car2.speed == 33.33

def test_decelerate():
    car = Car()
    car.speed = 20
    car.speed = car.decelerate()
    assert car.speed == 18
