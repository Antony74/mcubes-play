# usage:
#     python ./main.py

import numpy as np
import mcubes
from stl import mesh

from sdf import sdf

N = 100  # resolution per axis
xMin, xMax = -2, 2
yMin, yMax = -2, 2
zMin, zMax = -2, 2

values = np.zeros((N, N, N), dtype=np.float32)

for xIndex, x in enumerate(np.linspace(xMin, xMax, N)):
    for yIndex, y in enumerate(np.linspace(yMin, yMax, N)):
        for zIndex, z in enumerate(np.linspace(zMin, zMax, N)):
            values[xIndex, yIndex, zIndex] = sdf(x, y, z)

vertices, triangles = mcubes.marching_cubes(values, 0.0)

stl_mesh = mesh.Mesh(np.zeros(triangles.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(triangles):
    for j in range(3):
        stl_mesh.vectors[i][j] = vertices[f[j], :]

stl_mesh.save('model.stl')
