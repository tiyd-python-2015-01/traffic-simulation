import numpy as np


class Road():
    """
    Creates a 1,000m array that serves as an infinite road loop
    """

    def __init__(self):
        self.track = np.array(np.zeros((1, 1000)))
