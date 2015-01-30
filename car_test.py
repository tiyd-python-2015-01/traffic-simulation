from car import Car

buick = Car()
honda = Car()

def test_accelerate():
    assert buick.accelerate() == 2

def test_deccelerate():
    buick.current_speed = 10
    buick.deccelerate()
    assert buick.current_speed == 8
    honda.current_speed = 1
    honda.deccelerate()
    assert honda.current_speed == 0

def test_accelerate():
    buick.current_speed = 10
    buick.accelerate()
    assert buick.current_speed == 12
    honda.current_speed = 32
    honda.accelerate()
    assert honda.current_speed == honda.max_speed

def test_move():
    buick.current_speed = 10
    buick.move()
    assert buick.position == 12
