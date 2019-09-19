# state file generated using paraview version 5.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1486, 924]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.5, 0.5, -0.5]
renderView1.StereoType = 0
renderView1.CameraPosition = [3.5628566837277296, -0.3683817822446255, 0.530036134277208]
renderView1.CameraFocalPoint = [0.5000000000000002, 0.4999999999999998, -0.4999999999999999]
renderView1.CameraViewUp = [-0.3107661822949143, 0.030736498617534386, 0.9499892881472813]
renderView1.CameraParallelScale = 0.8660254037844386
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
test6_32dpvd = PVDReader(FileName='/home/jb/Vyuka/PAV - python pro aplikovane vedy/notebooks/cube/test6_32d.pvd')

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'piezo_head_p0'
piezo_head_p0LUT = GetColorTransferFunction('piezo_head_p0')
piezo_head_p0LUT.RGBPoints = [-3.000001075304584, 0.231373, 0.298039, 0.752941, -1.5176776011019648, 0.865003, 0.865003, 0.865003, -0.035354126899345584, 0.705882, 0.0156863, 0.14902]
piezo_head_p0LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'piezo_head_p0'
piezo_head_p0PWF = GetOpacityTransferFunction('piezo_head_p0')
piezo_head_p0PWF.Points = [-3.000001075304584, 0.0, 0.5, 0.0, -0.035354126899345584, 1.0, 0.5, 0.0]
piezo_head_p0PWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from test6_32dpvd
test6_32dpvdDisplay = Show(test6_32dpvd, renderView1)
# trace defaults for the display properties.
test6_32dpvdDisplay.Representation = 'Surface'
test6_32dpvdDisplay.ColorArrayName = ['CELLS', 'piezo_head_p0']
test6_32dpvdDisplay.LookupTable = piezo_head_p0LUT
test6_32dpvdDisplay.OSPRayScaleArray = 'pressure_p1'
test6_32dpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
test6_32dpvdDisplay.SelectOrientationVectors = 'None'
test6_32dpvdDisplay.ScaleFactor = 0.1
test6_32dpvdDisplay.SelectScaleArray = 'None'
test6_32dpvdDisplay.GlyphType = 'Arrow'
test6_32dpvdDisplay.GlyphTableIndexArray = 'None'
test6_32dpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
test6_32dpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
test6_32dpvdDisplay.ScalarOpacityFunction = piezo_head_p0PWF
test6_32dpvdDisplay.ScalarOpacityUnitDistance = 0.23646295393780983
test6_32dpvdDisplay.GaussianRadius = 0.05
test6_32dpvdDisplay.SetScaleArray = ['POINTS', 'pressure_p1']
test6_32dpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
test6_32dpvdDisplay.OpacityArray = ['POINTS', 'pressure_p1']
test6_32dpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
test6_32dpvdDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for piezo_head_p0LUT in view renderView1
piezo_head_p0LUTColorBar = GetScalarBar(piezo_head_p0LUT, renderView1)
piezo_head_p0LUTColorBar.Title = 'piezo_head_p0'
piezo_head_p0LUTColorBar.ComponentTitle = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(test6_32dpvd)
# ----------------------------------------------------------------