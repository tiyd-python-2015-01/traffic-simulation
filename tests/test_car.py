from car import Car


# set up some test cars
car_a = Car(position=33)
car_b = Car(position=100)
car_c = Car(position=149)
car_d = Car(position=208)
car_list = [car_a, car_b, car_c, car_d]


def test_position():
    car1 = Car(position=6)
    car2 = Car(position=1006)
    car3 = Car(position=42006)
    assert car1.position == 6
    assert car2.position == 6
    assert car3.position == 6


def test_accelerate():
    car = Car()
    car.speed = 20
    car.accelerate()
    assert car.speed == 22

    car2 = Car()
    car2.speed = 32
    car2.accelerate()
    assert car2.speed == 33.33


def test_decelerate():
    car = Car()
    car.speed = 20
    car.decelerate()
    assert car.speed == 18


def test_accelerate_condition():
    car = Car()
    car.speed = 20
    assert car.accelerate_condition() is True
    car.speed = 33.33
    assert car.accelerate_condition() is False


def test_move():
    car = Car(position=0, speed=20)
    car.move()
    assert car.position == 20
    car2 = Car(position=1000, speed=20)
    car2.move()
    assert car.position == 20
    car3 = Car(position=999, speed=20)
    car3.move()
    assert car3.position == 19
