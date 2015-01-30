import numpy as np


class Road():
    """
    its length - 1,000 meter road
    end of road equals the start of the road, so it's a loop
    """

    def __init__(self):
        self.track = np.array(np.zeros((1, 1000)))
