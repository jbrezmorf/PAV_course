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

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1584, 804]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0, 0, 0]
renderView1.StereoType = 0
renderView1.CameraPosition = [-843016.147822867, -1030981.279358202, 8685.514177587218]
renderView1.CameraFocalPoint = [-818867.8250000001, -1029699.0550000018, -5.555000000659112]
renderView1.CameraViewUp = [0.3418241263036494, -0.11951250776112635, 0.9321335886906948]
renderView1.CameraParallelScale = 14256.569283711766
renderView1.Background = [0.32, 0.34, 0.43]


# Build pipeline
# Create a new sphere proxy on the active connection and register it
# in the sources group.
#cube = PVDReader(FileName="cube/test6_32d.pvd")
cube = XMLUnstructuredGridReader(FileName="cube/test6_32d/test6_32d-000000.vtu")

# Get value range of the "piezo_head_p0" array.
help(cube)
cell_data = cube.CellData
help(cell_data)
range = cell_data.GetArray("piezo_head_p0").GetComponentRange(0)

# get color transfer function/color map for 'piezo_head_p0'
col_map_tf = GetColorTransferFunction("piezo_head_p0")
col_map_tf.RescaleTransferFunction(range[0], range[1])

# Display mesh colored by "piezo_head_p0"
display = Show(cube, renderView1)
display.Representation = 'Surface'
display.ColorArrayName = ['CELLS', 'piezo_head_p0']
display.LookupTable = col_map_tf
# Set visible color bar.
display.SetScalarBarVisibility(renderView1, True)

# Render the scene
Render()
iren.Start()


# Apply ProgrammableFilter from a file
with open("pf_script.py", "r") as f:
     content = f.read()

pf = ProgrammableFilter(Input=[cube], Script=content)


# Render the scene
Render()
iren.Start()

