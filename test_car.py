from car import Car


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
    assert car2.speed == 33


def test_decelerate():
    car = Car()
    car.speed = 20
    car.decelerate()
    assert car.speed == 18


def test_accelerate_condition_speed():
    car = Car()
    car.speed = 20
    assert car.accelerate_condition_speed() is True
    car.speed = 33
    assert car.accelerate_condition_speed() is False


# def test_accelerate_condition_car():
#     car1 = Car(position=0)
#     car2 = Car(position=40)
#     car3 = Car(position=60)
#     car4 = Car(position=80)
#     car_list = [car1, car2, car3, car4]
#
#     assert car1.accelerate_condition_car(car_list) is True
#     assert car2.accelerate_condition_car(car_list) is False
#     assert car2.accelerate_condition_car(car_list) is False
#     assert car2.accelerate_condition_car(car_list) is True

# def test_accelerate_condition(car_list):
#     car_list = [33, 100, 149, 208]
#     car1 = Car(position=0, speed=20)
#     assert car1.accelerate_condition(car_list) is True
#     car2 = Car(position=0, speed=33.33)
#     assert car2.accelerate_condition(car_list) is False
#     car3 = Car(position=10, speed=20)
#     assert car3.accelerate_condition(car_list) is False
#     car4 = Car(position=10, speed=33.33)
#     assert car4.accelerate_condition(car_list) is False


def test_move():
    car = Car(position=0, speed=20)
    car.move()
    assert car.position == 20
    car2 = Car(position=1000, speed=20)
    car2.move()
    assert car.position == 20

def test_move_check():
    car = Car(position=0, speed=20)
    x = car.move_check()
    assert x == 20
    car2 = Car(position=50, speed=30)
    y = car2.move_check()
    assert y == 80
