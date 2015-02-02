from simulation import Simulation
from road import Road

a_road = Road()

def test_spacing():
    a_simulation = Simulation(a_road)
    a_simulation.place_evenly_spaced_cars()
    assert a_simulation.get_num_cars() == 30
