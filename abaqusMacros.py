# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def MMC():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(120.0, 120.0))
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Matrix']
    p.BaseSolidExtrude(sketch=s, depth=120.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Matrix']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.ConstructionLine(point1=(-40.0, 0.0), point2=(81.25, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(20.0, 0.0), 
        axisPoint2=(0.0, 10.0))
    s1.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
    s1.Line(point1=(-20.0, 0.0), point2=(20.0, 0.0))
    s1.HorizontalConstraint(entity=g[6], addUndoState=False)
    s1.ParallelConstraint(entity1=g[3], entity2=g[6], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
    s1.autoTrimCurve(curve1=g[4], point1=(-12.6530914306641, 7.85093688964844))
    s1.autoTrimCurve(curve1=g[7], point1=(11.2992630004883, 8.45875549316406))
    s1.sketchOptions.setValues(constructionGeometry=ON)
    s1.assignCenterline(line=g[3])
    p = mdb.models['Model-1'].Part(name='Particulate', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Particulate']
    p.BaseSolidRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Particulate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Matrix']
    a.Instance(name='Matrix-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Particulate']
    a.Instance(name='Particulate-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=335.693, 
        farPlane=651.39, width=368.184, height=155.551, viewOffsetX=-9.02526, 
        viewOffsetY=-3.37665)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=357.05, 
        farPlane=628.681, width=391.609, height=165.447, cameraPosition=(
        -50.4812, 478.601, 286.868), cameraUpVector=(0.411125, 0.170796, 
        -0.895436), cameraTarget=(58.9017, 47.3032, 70.6691), 
        viewOffsetX=-9.59946, viewOffsetY=-3.59148)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=360.159, 
        farPlane=625.572, width=339.568, height=143.461, viewOffsetX=-9.68305, 
        viewOffsetY=-3.62275)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=381.709, 
        farPlane=665.152, width=408.444, height=172.56, cameraPosition=(
        -448.438, 207.605, 102.792), cameraUpVector=(0.580552, 0.78579, 
        -0.213292), cameraTarget=(54.8809, 48.1259, 56.9932))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=374.658, 
        farPlane=669.418, width=400.899, height=169.372, cameraPosition=(
        -412.56, 288.626, -8.32996), cameraUpVector=(0.724412, 0.686535, 
        0.0624299), cameraTarget=(54.4332, 47.1148, 58.3799))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=361.11, 
        farPlane=679.45, width=386.402, height=163.248, cameraPosition=(
        -298.005, 306.434, -238.926), cameraUpVector=(0.709958, 0.633971, 
        0.306659), cameraTarget=(52.6941, 46.8445, 61.8807))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=363.68, 
        farPlane=676.881, width=373.384, height=157.748)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=306.175, 
        farPlane=677.626, width=402.62, height=170.1, viewOffsetX=23.331, 
        viewOffsetY=6.01785)
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('Particulate-1', ), direction1=(1.0, 0.0, 
        0.0), direction2=(0.0, 0.0, -1.0), number1=2, number2=6, spacing1=40.0, 
        spacing2=20.0)
    a = mdb.models['Model-1'].rootAssembly
    a.deleteFeatures(('Particulate-1', 'Particulate-1-lin-2-1', ))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-2', ), vector=(69.0, 81.0, 
        89.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-2', ), vector=(70.0, 30.0, 
        80.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-3', ), vector=(10.0, 75.0, 
        79.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-3', ), vector=(88.0, 107.0, 
        118.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-4', ), vector=(6.0, 59.0, 
        23.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-4', ), vector=(23.0, 5.0, 
        76.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=302.849, 
        farPlane=699.481, width=398.246, height=168.252, cameraPosition=(
        -292.618, 313.851, -238.806), cameraUpVector=(0.57898, 0.658617, 
        0.480631), cameraTarget=(58.0809, 54.2616, 62.0012), 
        viewOffsetX=23.0775, viewOffsetY=5.95247)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-5', ), vector=(25.0, 110.0, 
        14.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-5', ), vector=(63.0, 40.0, 
        21.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.656, 
        farPlane=710.359, width=491.359, height=207.59, cameraPosition=(
        -395.426, 343.719, -26.0406), cameraUpVector=(0.760727, 0.607821, 
        0.2277), cameraTarget=(45.1482, 57.2658, 42.515), viewOffsetX=28.4731, 
        viewOffsetY=7.34418)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-6', ), vector=(72.0, 95.0, 
        44.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-6', ), vector=(115.0, 32.0, 
        111.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=375.57, 
        farPlane=714.977, width=493.876, height=208.653, cameraPosition=(
        -444.13, 237.822, -42.0649), cameraUpVector=(0.570265, 0.74685, 
        0.34207), cameraTarget=(47.9126, 59.9813, 42.3638), 
        viewOffsetX=28.6189, viewOffsetY=7.38179)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=379.214, 
        farPlane=715.047, width=498.668, height=210.678, cameraPosition=(
        -444.894, 235.669, -42.1477), cameraUpVector=(0.582303, 0.757673, 
        0.294714), cameraTarget=(47.1488, 57.8287, 42.281), 
        viewOffsetX=28.8966, viewOffsetY=7.45342)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-4', ), vector=(0.0, 0.0, 33.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=331.432, 
        farPlane=713.208, width=435.835, height=184.132, cameraPosition=(
        -343.331, 283.163, -210.289), cameraUpVector=(0.435837, 0.682732, 
        0.58645), cameraTarget=(66.1143, 62.4073, 43.6463), 
        viewOffsetX=25.2556, viewOffsetY=6.51427)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-5', ), vector=(0.0, 0.0, 57.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=311.432, 
        farPlane=657.518, width=409.535, height=173.021, cameraPosition=(
        -56.1982, 265.69, -399.823), cameraUpVector=(-0.478068, 0.523985, 
        0.704905), cameraTarget=(76.4365, 80.2421, 78.5895), 
        viewOffsetX=23.7316, viewOffsetY=6.12118)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=315.774, 
        farPlane=653.176, width=394.212, height=166.547, viewOffsetX=24.0624, 
        viewOffsetY=6.20652)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=304.763, 
        farPlane=642.335, width=380.466, height=160.74, cameraPosition=(
        159.527, 364.986, -331.041), cameraUpVector=(-0.9196, 0.229921, 
        0.318548), cameraTarget=(43.9148, 76.329, 98.1122), 
        viewOffsetX=23.2234, viewOffsetY=5.9901)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=319.012, 
        farPlane=643.551, width=398.254, height=168.255, cameraPosition=(
        161.29, 461.801, -228.351), cameraUpVector=(-0.945915, 0.091975, 
        0.311103), cameraTarget=(41.0975, 58.1737, 93.3631), 
        viewOffsetX=24.3092, viewOffsetY=6.27015)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-2-6', ), vector=(0.0, 0.0, 55.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=367.785, 
        farPlane=668.304, width=459.142, height=193.979, cameraPosition=(
        -75.7036, 490.026, -197.748), cameraUpVector=(-0.725217, -0.213891, 
        0.654455), cameraTarget=(60.4644, 61.7133, 83.0868), 
        viewOffsetX=28.0258, viewOffsetY=7.22878)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Particulate-1-lin-1-5', ), vector=(0.0, 0.0, 64.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=368.35, 
        farPlane=672.101, width=459.847, height=194.277, cameraPosition=(
        -55.7399, 355.114, -355.685), cameraUpVector=(-0.213923, 0.482139, 
        0.849575), cameraTarget=(73.6136, 50.0721, 57.9316), 
        viewOffsetX=28.0688, viewOffsetY=7.23988)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=369.44, 
        farPlane=671.01, width=448.527, height=189.494, viewOffsetX=28.1519, 
        viewOffsetY=7.26131)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.InstanceFromBooleanMerge(name='composite', instances=(
        a1.instances['Matrix-1'], a1.instances['Particulate-1-lin-1-2'], 
        a1.instances['Particulate-1-lin-1-3'], 
        a1.instances['Particulate-1-lin-1-4'], 
        a1.instances['Particulate-1-lin-1-5'], 
        a1.instances['Particulate-1-lin-1-6'], 
        a1.instances['Particulate-1-lin-2-2'], 
        a1.instances['Particulate-1-lin-2-3'], 
        a1.instances['Particulate-1-lin-2-4'], 
        a1.instances['Particulate-1-lin-2-5'], 
        a1.instances['Particulate-1-lin-2-6'], ), keepIntersections=ON, 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    p = mdb.models['Model-1'].parts['Particulate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['composite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['composite']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[7], sketchUpEdge=e[18], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(120.0, 
        59.955695, 61.295873))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=339.41, gridSpacing=8.48, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['composite']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.rectangle(point1=(-61.295873, 59.955695), point2=(58.704127, -60.044305))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=271.514, 
        farPlane=513.309, width=489.261, height=206.703, cameraPosition=(
        459.411, 49.5471, 127.536), cameraTarget=(120, 49.5471, 127.536))
    s.rectangle(point1=(-110.24, 101.76), point2=(152.64, -84.8))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=349.465, 
        farPlane=791.558, width=576.404, height=243.52, viewOffsetX=-42.9198, 
        viewOffsetY=25.3996)
    p = mdb.models['Model-1'].parts['composite']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[7], sketchUpEdge=e1[18], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s, flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['composite']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[37], sketchUpEdge=e[45], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(60.0, 60.0, 
        120.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=415.69, gridSpacing=10.39, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['composite']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.rectangle(point1=(-60.0, 60.0), point2=(60.0, -60.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=299.514, 
        farPlane=509.474, width=489.261, height=206.703, cameraPosition=(
        48.4138, 54.8027, 459.411), cameraTarget=(48.4138, 54.8027, 120))
    s1.rectangle(point1=(-114.29, 103.9), point2=(124.68, -93.51))
    p = mdb.models['Model-1'].parts['composite']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[37], sketchUpEdge=e1[45], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=382.689, 
        farPlane=669.16, width=407.653, height=172.226, cameraPosition=(347.07, 
        340.042, -279.693), cameraUpVector=(-0.804284, 0.512626, 0.30057), 
        cameraTarget=(71.5236, 50.5326, 54.5725))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=379.488, 
        farPlane=652.405, width=404.243, height=170.786, cameraPosition=(
        -338.617, 243.933, -210.681), cameraUpVector=(0.176104, 0.570191, 
        0.802415), cameraTarget=(65.1456, 49.6386, 55.2144))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.545, 
        farPlane=658.348, width=450.333, height=190.257, viewOffsetX=5.45273, 
        viewOffsetY=-0.464711)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='SiC')
    mdb.models['Model-1'].materials['SiC'].Elastic(table=((410000000000.0, 0.14), 
        ))
    mdb.models['Model-1'].Material(name='Al')
    mdb.models['Model-1'].materials['Al'].Elastic(table=((75000000000.0, 0.3), ))
    mdb.models['Model-1'].materials['Al'].Plastic(scaleStress=None, table=((
        250000000.0, 0.0), (248000000.0, 0.05), (240000000.0, 0.15), (
        230000000.0, 0.8), (220000000.0, 1.5)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.654, 
        farPlane=643.161, width=450.465, height=190.313, cameraPosition=(
        149.147, 453.499, -247.549), cameraUpVector=(0.0106201, 0.290839, 
        0.956713), cameraTarget=(63.1604, 41.8608, 60.0793), 
        viewOffsetX=5.45433, viewOffsetY=-0.464848)
    mdb.models['Model-1'].HomogeneousSolidSection(name='matrix', material='Al', 
        thickness=None)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.undoLast()
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='matrix', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='SiC', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fef ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.undoLast()
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fef ]', ), )
    region = p.Set(cells=cells, name='Set-2')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-3', material='Al', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    region = p.Set(cells=cells, name='Set-3')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-3', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=366.512, 
        farPlane=654.225, width=441.855, height=186.676, cameraPosition=(
        -281.987, 344.3, -189.056), cameraUpVector=(0.556624, 0.569429, 
        0.604913), cameraTarget=(71.4765, 47.2672, 52.4184), 
        viewOffsetX=5.35008, viewOffsetY=-0.455963)
    del mdb.models['Model-1'].sections['matrix']
    del mdb.models['Model-1'].sections['Section-3']
    del mdb.models['Model-1'].sections['Section-2']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=365.234, 
        farPlane=655.503, width=440.316, height=186.025, viewOffsetX=5.33142, 
        viewOffsetY=-0.45437)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='SiC', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fef ]', ), )
    region = p.Set(cells=cells, name='Set-4')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=367.19, 
        farPlane=653.552, width=442.673, height=187.021, cameraUpVector=(
        0.551187, 0.568041, 0.611165), cameraTarget=(71.5157, 47.3742, 
        52.4926), viewOffsetX=5.35996, viewOffsetY=-0.456802)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=364.289, 
        farPlane=641.776, width=439.175, height=185.543, cameraPosition=(
        -276.062, -288.576, -83.8564), cameraUpVector=(0.904181, -0.314012, 
        -0.289575), cameraTarget=(76.9894, 65.8888, 61.9495), 
        viewOffsetX=5.31761, viewOffsetY=-0.453193)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#773 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.undoLast()
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=309.165, 
        farPlane=585.986, width=345.67, height=146.039, cameraPosition=(
        320.828, 310.974, 319.745), cameraUpVector=(-0.585368, 0.577294, 
        -0.569276), cameraTarget=(62.4198, 52.5661, 61.337))
    p = mdb.models['Model-1'].parts['Matrix']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Particulate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['composite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=309.657, 
        farPlane=585.421, width=346.189, height=146.258)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='Al', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
    region = p.Set(cells=cells, name='Set-5')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=322.481, 
        farPlane=587.287, width=461.77, height=195.089, viewOffsetX=1.94087, 
        viewOffsetY=11.4826)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-3', material='SiC', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fef ]', ), )
    region = p.Set(cells=cells, name='Set-6')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-3', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['composite']
    p.seedPart(size=9.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#fff ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
    elemType1 = mesh.ElemType(elemCode=C3D20R)
    elemType2 = mesh.ElemType(elemCode=C3D15)
    elemType3 = mesh.ElemType(elemCode=C3D10)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fff ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['composite']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=317.856, 
        farPlane=569.879, width=455.146, height=192.775, cameraPosition=(
        449.86, 100.973, 266.664), cameraUpVector=(-0.37888, 0.898397, 
        -0.222109), cameraTarget=(58.2703, 49.8251, 56.1118), 
        viewOffsetX=1.91303, viewOffsetY=11.3179)
    p = mdb.models['Model-1'].parts['composite']
    p.deleteMesh()
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON, mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    del mdb.models['Model-1'].sections['Section-1']
    del mdb.models['Model-1'].sections['Section-2']
    del mdb.models['Model-1'].sections['Section-3']
    p = mdb.models['Model-1'].parts['Matrix']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=298.514, 
        farPlane=579.535, width=399.2, height=168.655, viewOffsetX=6.71462, 
        viewOffsetY=-0.318497)
    p = mdb.models['Model-1'].parts['Particulate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['composite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[5]
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[4]
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[3]
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[2]
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[1]
    del mdb.models['Model-1'].parts['composite'].sectionAssignments[0]
    session.viewports['Viewport: 1'].view.setValues(nearPlane=334.592, 
        farPlane=573.523, width=377.548, height=159.507, viewOffsetX=33.2949, 
        viewOffsetY=-1.90814)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='SiC', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fef ]', ), )
    region = p.Set(cells=cells, name='Set-9')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=331.271, 
        farPlane=576.845, width=373.8, height=157.924, viewOffsetX=-2.38787, 
        viewOffsetY=5.48574)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#7df ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.undoLast()
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=340.671, 
        farPlane=581.22, width=492.357, height=208.012, viewOffsetX=11.8269, 
        viewOffsetY=13.7266)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.either(leaf=leaf)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='Al', 
        thickness=None)
    p = mdb.models['Model-1'].parts['composite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    region = p.Set(cells=cells, name='Set-10')
    p = mdb.models['Model-1'].parts['composite']
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=340.647, 
        farPlane=600.041, width=492.323, height=207.997, cameraPosition=(
        434.656, 32.4417, -225.011), cameraUpVector=(-0.597421, 0.748983, 
        -0.286554), cameraTarget=(82.7598, 62.9905, 60.3032), 
        viewOffsetX=11.826, viewOffsetY=13.7256)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=335.996, 
        farPlane=604.692, width=549.572, height=232.184, viewOffsetX=1.17101, 
        viewOffsetY=11.5832)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Material']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=338.395, 
        farPlane=623.681, width=553.495, height=233.841, cameraPosition=(
        470.776, 279.172, -57.732), cameraUpVector=(-0.689596, 0.679896, 
        0.249398), cameraTarget=(84.7821, 68.6733, 55.702), 
        viewOffsetX=1.17936, viewOffsetY=11.6659)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Meshability']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    p = mdb.models['Model-1'].parts['composite']
    p.seedPart(size=13.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['composite']
    p.seedPart(size=15.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['composite']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Material']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    p = mdb.models['Model-1'].parts['composite']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['composite']
    p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['composite']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['composite']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['composite']
    p.seedPart(size=6.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['composite']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=312.689, 
        farPlane=582.463, width=350.158, height=148.308, viewOffsetX=-0.327426, 
        viewOffsetY=1.25737)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=319.599, 
        farPlane=573.409, width=357.895, height=151.585, cameraPosition=(
        143.332, 393.961, 340.322), cameraUpVector=(-0.100279, 0.346784, 
        -0.932569), cameraTarget=(61.8897, 52.8353, 62.2492), 
        viewOffsetX=-0.334661, viewOffsetY=1.28515)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#a804 ]', ), )
    p.Set(faces=faces, name='CBACK')
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#100a0040 ]', ), )
    p.Set(faces=faces, name='Set-11')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=328.634, 
        farPlane=574.769, width=366.514, height=155.235, cameraPosition=(
        153.691, -356.925, -94.583), cameraUpVector=(0.142023, 0.672542, 
        -0.726304), cameraTarget=(62.4198, 52.5659, 61.3369))
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#200 ]', ), )
    p.Set(faces=faces, name='Set-12')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#500000 ]', ), )
    p.Set(faces=faces, name='Set-13')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#8000000 ]', ), )
    p.Set(faces=faces, name='BACK')
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#a824 ]', ), )
    p.Set(faces=faces, name='BACK2')
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1000000 ]', ), )
    p.Set(faces=faces, name='BACK3')
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=314.472, 
        farPlane=573.307, width=350.719, height=148.546, cameraPosition=(
        -308.295, 270.817, 184.875), cameraUpVector=(-0.0649815, -0.24664, 
        -0.966926), cameraTarget=(62.4197, 52.5661, 61.337))
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#d00000 ]', ), )
    p.Set(faces=faces, name='BACK4')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(width=395.021, height=167.31, 
        viewOffsetX=-2.27753, viewOffsetY=4.43819)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=330.506, 
        farPlane=564.155, width=392.129, height=166.085, cameraPosition=(
        168.94, -373.562, 108.611), cameraUpVector=(0.81884, 0.553566, 
        -0.151875), cameraTarget=(51.8127, 55.5314, 58.7727), 
        viewOffsetX=-2.26086, viewOffsetY=4.40569)
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#4000200 ]', ), )
    p.Set(faces=faces, name='BACK5')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=343.343, 
        farPlane=547.668, width=382.919, height=162.184, cameraPosition=(
        107.34, 31.1237, -383.463), cameraUpVector=(-0.699727, 0.675629, 
        0.232179), cameraTarget=(62.4198, 52.566, 61.3369))
    p = mdb.models['Model-1'].parts['composite']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#100a0042 ]', ), )
    p.Set(faces=faces, name='BACK6')
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    a.ReferencePoint(point=(130.0, 0.0, 20.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=430.755, 
        farPlane=708.469, width=325.091, height=137.345, viewOffsetX=9.5941, 
        viewOffsetY=-16.7555)
    a = mdb.models['Model-1'].rootAssembly
    v11 = a.instances['composite-1'].vertices
    a.ReferencePoint(point=v11[13])
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['composite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=301.349, 
        farPlane=593.803, width=431.548, height=182.321, viewOffsetX=-2.27766, 
        viewOffsetY=9.1116)
    p = mdb.models['Model-1'].parts['composite']
    p.ReferencePoint(point=(130.0, 0.0, 120.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=294.715, 
        farPlane=594.71, width=448.987, height=189.689, viewOffsetX=6.16241, 
        viewOffsetY=11.6863)
    p = mdb.models['Model-1'].parts['composite']
    r = p.referencePoints
    refPoints=(r[29], )
    p.Set(referencePoints=refPoints, name='Set-19')
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    mdb.models['Model-1'].Equation(name='Constraint-1', terms=((1.0, 
        'composite-1.BACK', 1), (-1.0, 'composite-1.Set-19', 1)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=426.839, 
        farPlane=712.386, width=412.598, height=174.315, viewOffsetX=18.6515, 
        viewOffsetY=1.94025)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['composite-1'].referencePoints
    refPoints1=(r1[29], )
    region = a.Set(referencePoints=refPoints1, name='Set-1')
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
        region=region, u1=12.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    mdb.models['Model-1'].constraints['Constraint-1'].setValues(terms=((1.0, 
        'composite-1.BACK2', 1), (-1.0, 'composite-1.Set-19', 1)))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['composite-1'].sets['BACK4']
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', 
        region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['composite-1'].sets['BACK5']
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['composite-1'].sets['BACK6']
    mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Initial', 
        region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='MMC', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
        multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
    mdb.jobs['MMC'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='Y:/MMC.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=323.924, 
        farPlane=610.624, width=363.439, height=147.324, viewOffsetX=3.88337, 
        viewOffsetY=1.99988)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=343.299, 
        farPlane=606.575, width=385.177, height=156.136, cameraPosition=(
        466.283, -4.66347, -196.53), cameraUpVector=(-0.803831, -0.0572411, 
        -0.592097), cameraTarget=(80.096, 60.1425, 58.4308), 
        viewOffsetX=4.11564, viewOffsetY=2.1195)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])


