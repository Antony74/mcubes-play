# usage:
#     python ./main.py

import numpy as np
import mcubes
from stl import mesh

from sdf import sdf

X, Y, Z = np.mgrid[-2:2:100j, -2:2:100j, -2:2:100j]
values = sdf(X, Y, Z)

vertices, triangles = mcubes.marching_cubes(values, 0.0)

stl_mesh = mesh.Mesh(np.zeros(triangles.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(triangles):
    for j in range(3):
        stl_mesh.vectors[i][j] = vertices[f[j], :]

stl_mesh.save('model.stl')
