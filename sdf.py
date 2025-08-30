import math

def sdf(x, y, z):
    return -(math.sqrt(x**2 + y**2 + z**2) - 1.0)
