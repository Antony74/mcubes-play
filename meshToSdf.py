from mesh_to_sdf import mesh_to_voxels

import trimesh
import skimage

print('Load mcup.stl')
mesh = trimesh.load('mcup.stl')

resolution = 256
filename = 'mcup-resampled-{resolution}.stl'.format(resolution=resolution)

print('mesh_to_voxels')
voxels = mesh_to_voxels(mesh, resolution, pad=True)

print('marching_cubes')
vertices, faces, normals, _ = skimage.measure.marching_cubes(voxels, level=0)

print('Trimesh')
mesh = trimesh.Trimesh(vertices=vertices, faces=faces, vertex_normals=normals)

print('Save ' + filename)
mesh.export(filename)

print('Show')
mesh.show()
