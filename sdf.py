import math

def createSurface(fn, depth):
    def surface(x, y, z):
        return abs(fn(x, y, z) + depth) - depth

    return surface

def cylinderWidth(y):
    return 1

def createTruncateY(fn, start, end):
    def truncateY(x, y, z):
        if (y >= start and y <= end):
            return fn(x, y, z)
        else:
            return 10

    return truncateY

def createCylinder(fn):
    def cylinder(x, y, z):
        return (math.sqrt(x**2 + z**2) - fn(y))

    return cylinder

def createSdf(solid): 
    def sdf(x, y, z):
        cylinder = createCylinder(cylinderWidth)
        surface = createSurface(cylinder, 0.1)

        if (solid):
            surface = cylinder

        truncateY = createTruncateY(surface, -1.5, 1.5)
        return -truncateY(x, y, z)
    
    return sdf
