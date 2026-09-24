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
renderView1.ViewSize = [1584, 804]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-818867.825, -1029699.0549999999, -5.555000000000007]
renderView1.StereoType = 0
renderView1.CameraPosition = [-843016.147822867, -1030981.279358202, 8685.514177587218]
renderView1.CameraFocalPoint = [-818867.8250000001, -1029699.0550000018, -5.555000000659112]
renderView1.CameraViewUp = [0.3418241263036494, -0.11951250776112635, 0.9321335886906948]
renderView1.CameraParallelScale = 14256.569283711766
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
proudenipvd = PVDReader(FileName='/home/jb/Vyuka/PAV - python pro aplikovane vedy/notebooks/uloziste/proudeni.pvd')

# create a new 'Slice'
slice1 = Slice(Input=proudenipvd)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-823978.7718020333, -1029699.0549999999, -5.555000000000007]

# create a new 'Cell Centers'
cellCenters1 = CellCenters(Input=slice1)

# create a new 'Glyph'
glyph1 = Glyph(Input=cellCenters1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'None']
glyph1.Vectors = ['POINTS', 'None']
glyph1.ScaleMode = 'vector'
glyph1.ScaleFactor = 1763.09375
glyph1.GlyphMode = 'All Points'
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'velocity_p0'
velocity_p0LUT = GetColorTransferFunction('velocity_p0')
velocity_p0LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.4527911928422476e-07, 0.865003, 0.865003, 0.865003, 2.905582385684495e-07, 0.705882, 0.0156863, 0.14902]
velocity_p0LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity_p0'
velocity_p0PWF = GetOpacityTransferFunction('velocity_p0')
velocity_p0PWF.Points = [0.0, 0.0, 0.5, 0.0, 2.905582385684495e-07, 1.0, 0.5, 0.0]
velocity_p0PWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'velocity_p0']
slice1Display.LookupTable = velocity_p0LUT
slice1Display.OSPRayScaleArray = 'conductivity'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 1764.053119909228
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.GaussianRadius = 882.026559954614
slice1Display.SetScaleArray = [None, '']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = [None, '']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show data from cellCenters1
cellCenters1Display = Show(cellCenters1, renderView1)
# trace defaults for the display properties.
cellCenters1Display.Representation = 'Surface'
cellCenters1Display.ColorArrayName = [None, '']
cellCenters1Display.OSPRayScaleArray = 'conductivity'
cellCenters1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellCenters1Display.SelectOrientationVectors = 'None'
cellCenters1Display.ScaleFactor = 1763.09375
cellCenters1Display.SelectScaleArray = 'None'
cellCenters1Display.GlyphType = 'Arrow'
cellCenters1Display.GlyphTableIndexArray = 'None'
cellCenters1Display.DataAxesGrid = 'GridAxesRepresentation'
cellCenters1Display.PolarAxes = 'PolarAxesRepresentation'
cellCenters1Display.GaussianRadius = 881.546875
cellCenters1Display.SetScaleArray = ['POINTS', 'conductivity']
cellCenters1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellCenters1Display.OpacityArray = ['POINTS', 'conductivity']
cellCenters1Display.OpacityTransferFunction = 'PiecewiseFunction'

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocity_p0LUT in view renderView1
velocity_p0LUTColorBar = GetScalarBar(velocity_p0LUT, renderView1)
velocity_p0LUTColorBar.Title = 'velocity_p0'
velocity_p0LUTColorBar.ComponentTitle = 'Magnitude'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(slice1)
# ----------------------------------------------------------------