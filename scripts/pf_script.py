#from paraview.vtk import dataset_adapter as DA

from paraview.vtk.numpy_interface.dataset_adapter import numpyTovtkDataArray as da
import numpy
pdi = self.GetInputDataObject(0,0)
pdo = self.GetOutputDataObject(0)
pdo.CopyAttributes(pdi)

old_pts = inputs[0].Points
bary = mean(old_pts,axis=0)
print(bary)
new_pts = old_pts - numpy.array([1,2,3])
#pdo.PointData.append(new_pts, 'newpts')
arr = da(new_pts, 'newpts')
pdo.GetPoints().SetData(arr)