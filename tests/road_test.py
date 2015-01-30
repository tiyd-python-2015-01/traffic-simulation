import numpy as np
from traffic_simulation.road import Road


def test_road_creation_contents():
    test_road = Road()
    assert len(test_road.road) == 1000
    assert np.sum(test_road.road) == 0
