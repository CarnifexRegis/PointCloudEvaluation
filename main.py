import open3d as o3d
import numpy as np
print("Testing IO for meshes ...")
groundTruth = o3d.io.read_triangle_mesh("bun_zipper.ply")
groundTruth.compute_vertex_normals()
scan = o3d.io.read_triangle_mesh("bun_zipper_res4.ply")
scan.compute_vertex_normals()
#o3d.visualization.draw_geometries([groundTruth])
#o3d.visualization.draw_geometries([scan])
#print(groundTruth)
#print(scan)
pcdGroundTruth = groundTruth.sample_points_uniformly(number_of_points=100000)
pcdScans = scan.sample_points_uniformly(number_of_points=100000)
recall = pcdGroundTruth.compute_point_cloud_distance(pcdScans)
precision = pcdScans.compute_point_cloud_distance(pcdGroundTruth)
recallArray = np.asarray(recall)
precisionArray = np.asarray(precision)
threshold = np.double(0.001)
#numpay length instead of numpy zero
#Zu große auslesen und
R = np.double(np.count_nonzero(recallArray < threshold))/np.double(recallArray.size)
P = np.double(np.count_nonzero(precisionArray < threshold))/np.double(recallArray.size)
print(np.count_nonzero(recallArray < threshold))
print(np.double(np.count_nonzero(recallArray)))
print("R: ")
print(R)
print("P: ")
print(P)
fScore = 2.0 * R * P/(R + P)
print("F-Score: ")
print(fScore)
#schaune op poincloud distance funktioniert array = null
#ind = np.where(dists > 0.005)[0]
#pcdGroundTruthWithoutScans = pcdScans.select_by_index(ind)
#o3d.visualization.draw_geometries([pcdGroundTruthWithoutScans])
#o3d.visualization.draw_geometries([pcdGroundTruth])
#o3d.visualization.draw_geometries([pcdScans])
