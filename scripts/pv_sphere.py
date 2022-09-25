from paraview.simple import *
import vtk

# Create a view
view = CreateRenderView()

# Initialize a new interactor
iren = vtk.vtkRenderWindowInteractor()
#iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackball())
iren.SetInteractorStyle(vtk.vtkInteractorStyleSwitch())
iren.SetRenderWindow(view.GetRenderWindow())
iren.Initialize()

# Build pipeline
# Create a new sphere proxy on the active connection and register it
# in the sources group.
sphere = Sphere(ThetaResolution=8, PhiResolution=12)

# Apply a shrink filter
#shrink = Shrink(sphere)
#shrink.ShrinkFactor = 0.9

# Turn the visiblity of the shrink object on.
dp = GetDisplayProperties()

Show(sphere)
#Show(sphere)

# Render the scene ( Sphere outline)
Render()
iren.Start()

# Create new dataset for the sphere grid
elev = Elevation(sphere)
Show(elev)

# Set representaion of the dataset
dp = GetDisplayProperties(elev)
# Possible representations: ['Outline', 'Points', 'Wireframe', 'Surface', 'Surface With Edges']
dp.Representation = 'Wireframe'

Render()

# Start interaction
iren.Start()

