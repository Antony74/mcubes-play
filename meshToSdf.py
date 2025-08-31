from mesh_to_sdf import mesh_to_voxels

import trimesh
import skimage

print('Load mcup.stl')
mesh = trimesh.load('mcup.stl')

print('mesh_to_voxels')
voxels = mesh_to_voxels(mesh, 128, pad=True)

print('marching_cubes')
vertices, faces, normals, _ = skimage.measure.marching_cubes(voxels, level=0)

print('Trimesh')
mesh = trimesh.Trimesh(vertices=vertices, faces=faces, vertex_normals=normals)

print('Save mcup-resampled.stl')
mesh.export('mcup-resampled.stl')

print('Show')
mesh.show()
