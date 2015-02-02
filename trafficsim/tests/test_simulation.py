from trafficsim.simulation import Simulation


sim = Simulation()

sim_two = Simulation(number_of_cars=30)

edge_sim = Simulation(number_of_cars=2)

edge_sim_two = Simulation(number_of_cars=2)

sim_three = Simulation(number_of_cars=3)


def test_speed():
    sim.traffic[0].speed_up()
    start_speed = sim.traffic[0].speed
    sim.adjust_speeds()
    assert start_speed != sim.traffic[0].speed


def test_speed_adjust():
    sim_two.traffic[2].set_slow_chance(0)
    sim_two.traffic[3].set_slow_chance(0)
    sim_two.traffic[2].set_position(80)
    sim_two.traffic[2].set_speed(20)
    sim_two.traffic[3].set_speed(10)
    sim_two.adjust_speeds()
    assert sim_two.traffic[2].speed == 12
    assert sim_two.traffic[3].speed == 12


def test_edge_case():
    edge_sim.traffic[1].set_speed(30)
    edge_sim.traffic[1].set_position(990)
    edge_sim.traffic[0].set_position(10)
    edge_sim.adjust_speeds()
    assert edge_sim.traffic[1].speed == 2


def test_edge_case_two():
    edge_sim_two.traffic[1].set_speed(10)
    edge_sim_two.traffic[1].set_position(995)
    edge_sim_two.traffic[0].set_position(4)
    edge_sim_two.traffic[0].set_speed(30)
    edge_sim_two.move_cars()
    assert edge_sim_two.traffic[1].back == 998
    assert edge_sim_two.traffic[0].back == 34


def test_movement():
    sim_three.traffic[0].set_slow_chance(0)
    sim_three.traffic[1].set_slow_chance(0)
    sim_three.traffic[2].set_slow_chance(0)
    sim_three.traffic[0].set_position(10)
    sim_three.traffic[1].set_position(20)
    sim_three.traffic[2].set_position(500)
    sim_three.traffic[0].set_speed(20)
    sim_three.traffic[1].set_speed(5)
    sim_three.traffic[2].set_speed(30)
    sim_three.move_cars()
    assert sim_three.traffic[0].back == 19
    assert sim_three.traffic[1].back == 25
    assert sim_three.traffic[2].back == 530
