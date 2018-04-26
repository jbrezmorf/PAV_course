from paraview.simple import *
import vtk

# Create a view
view = CreateRenderView()

# Initialize a new interactor
#from libvtkRenderingPython import *
iren = vtk.vtkRenderWindowInteractor()
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackball())
iren.SetRenderWindow(view.GetRenderWindow())
iren.Initialize()

# Build pipeline
# Create a new sphere proxy on the active connection and register it
# in the sources group.
sphere = Sphere(ThetaResolution=8, PhiResolution=32)

# Apply a shrink filter
shrink = Shrink(sphere)

# Turn the visiblity of the shrink object on.
Show(shrink)

# Render the scene
Render()

# Start interaction
iren.Start()

