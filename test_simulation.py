from simulation import Simulation

def test_simulation_init():
    sim = Simulation()
    assert len(sim.car_list) == 30
