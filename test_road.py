import numpy as np

from road import Road


def test_road_init():
    road = Road(length=10)
    assert len(road.blank_road) == 10
