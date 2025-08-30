import numpy as np

def sdf(x, y, z):
    return -(np.sqrt(x**2 + y**2 + z**2) - 1.0)
