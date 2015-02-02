from trafficsim.car import Car


best_car = Car(5)
best_car.speed_up()
best_car.speed_up()


def test_car_speed_up():
    assert best_car.speed == 4
    best_car.speed_up()
    assert best_car.speed == 6
    best_car.speed_up()
    assert best_car.speed == 8


def test_car_slow_down():
    best_car.slow_down()
    assert best_car.speed == 6
    best_car.slow_down()
    assert best_car.speed == 4


def test_car_position():
    assert best_car.back == 5


def test_car_movement():
    best_car.move(1000)
    assert best_car.back == 9
