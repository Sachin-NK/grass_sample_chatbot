import random

dataset = [
    {"input": "gis: How do I calculate the slope for a raster?",
     "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: What command do I use for raster algebra?",
     "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How do I create a vector map from a raster?",
     "output": "Command: r.to.vect\nExample: r.to.vect input=raster_map output=vector_map type=area"},
    {"input": "gis: How do I display a raster map?",
     "output": "Command: d.rast\nExample: d.rast map=raster_map"},
    {"input": "gis: How can I list all available raster maps?",
     "output": "Command: g.list\nExample: g.list type=raster"},
    {"input": "gis: How do I set the computational region to match a specific raster map?",
     "output": "Command: g.region\nExample: g.region raster=elevation_map"},
    {"input": "gis: How can I import a GeoTIFF file into GRASS GIS?",
     "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: How do I export a raster map to a GeoTIFF file?",
     "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=output_file.tif format=GTiff"},
    {"input": "gis: How can I reproject a vector map to a different coordinate system?",
     "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How do I calculate the area of each polygon in a vector map?",
     "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I buffer vector features by a specific distance?",
     "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I clip a vector map using another vector map as a mask?",
     "output": "Command: v.overlay\nExample: v.overlay ainput=vector_map binput=mask_map operator=and output=clipped_map"},
    {"input": "gis: How can I dissolve boundaries between adjacent polygons with the same attribute?",
     "output": "Command: v.dissolve\nExample: v.dissolve input=vector_map column=attribute_column output=dissolved_map"},
    {"input": "gis: How do I remove small areas (islands) from a vector map?",
     "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How can I simplify the geometry of vector features?",
     "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How do I convert a vector map to a raster map?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I patch multiple raster maps into a single raster map?",
     "output": "Command: r.patch\nExample: r.patch input=map1,map2,map3 output=patched_map"},
    {"input": "gis: How do I fill null (no-data) cells in a raster map?",
     "output": "Command: r.fillnulls\nExample: r.fillnulls input=raster_map output=filled_map"},
    {"input": "gis: How can I calculate statistics for a raster map?",
     "output": "Command: r.univar\nExample: r.univar map=raster_map"},
    {"input": "gis: How do I resample a raster map to a different resolution?",
     "output": "Command: r.resamp.interp\nExample: r.resamp.interp input=raster_map output=resampled_map method=bilinear"},
    {"input": "gis: How can I extract contour lines from a raster elevation map?",
     "output": "Command: r.contour\nExample: r.contour input=elevation_map output=contours step=10"},
    {"input": "gis: How do I perform a cost distance analysis?",
     "output": "Command: r.cost\nExample: r.cost input=cost_map output=cost_distance start_coordinates=100,200"},
    {"input": "gis: How can I perform a viewshed analysis from a specific point?",
     "output": "Command: r.viewshed\nExample: r.viewshed input=elevation_map output=viewshed coordinates=100,200"},
    {"input": "gis: How do I calculate the aspect (orientation) of slopes in a raster map?",
     "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map aspect=aspect_map"},
    {"input": "gis: How can I compute the curvature of a terrain surface?",
     "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map pcurvature=profile_curv tcurvature=tangential_curv"},
    {"input": "gis: How do I perform watershed analysis to delineate basins?",
     "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map basin=basin_map"},
    {"input": "gis: How can I calculate the flow accumulation from an elevation map?",
     "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map accumulation=flow_accumulation"},
    {"input": "gis: How do I calculate the topographic wetness index (TWI)?",
     "output": "Command: r.topidx\nExample: r.topidx input=elevation_map output=twi_map"},
    {"input": "gis: How can I generate a hillshade (shaded relief) map from elevation data?",
     "output": "Command: r.relief\nExample: r.relief input=elevation_map output=hillshade"},
    {"input": "gis: How do I calculate solar irradiation for a given area?",
     "output": "Command: r.sun\nExample: r.sun elevation=elevation_map glob_rad=solar_radiation"},
    {"input": "gis: How can I interpolate a raster map from scattered point data?",
     "output": "Command: v.surf.rst\nExample: v.surf.rst input=points_map zcolumn=value output=interpolated_raster"},
    {"input": "gis: How do I convert a vector map to a raster map?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: Convert vector to raster?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: I want to rasterize a vector map. What command should I use?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: What's the GRASS tool to turn vector into raster?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: What is the official command to rasterize a vector map?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
     {"input": "gis: How do I calculate the slope for a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: What command do I use for raster algebra?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How do I create a vector map from a raster?", "output": "Command: r.to.vect\nExample: r.to.vect input=raster_map output=vector_map type=area"},
    {"input": "gis: How do I display a raster map?", "output": "Command: d.rast\nExample: d.rast map=raster_map"},
    {"input": "gis: How can I list all available raster maps?", "output": "Command: g.list\nExample: g.list type=raster"},
    {"input": "gis: How do I set the computational region to match a specific raster map?", "output": "Command: g.region\nExample: g.region raster=elevation_map"},
    {"input": "gis: How can I import a GeoTIFF file into GRASS GIS?", "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: How do I export a raster map to a GeoTIFF file?", "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=output_file.tif format=GTiff"},
    {"input": "gis: How can I reproject a vector map to a different coordinate system?", "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How do I calculate the area of each polygon in a vector map?", "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I buffer vector features by a specific distance?", "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I clip a vector map using another vector map as a mask?", "output": "Command: v.overlay\nExample: v.overlay ainput=vector_map binput=mask_map operator=and output=clipped_map"},
    {"input": "gis: How can I dissolve boundaries between adjacent polygons with the same attribute?", "output": "Command: v.dissolve\nExample: v.dissolve input=vector_map column=attribute_column output=dissolved_map"},
    {"input": "gis: How do I remove small areas (islands) from a vector map?", "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How can I simplify the geometry of vector features?", "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How do I convert a vector map to a raster map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I patch multiple raster maps into a single raster map?", "output": "Command: r.patch\nExample: r.patch input=map1,map2,map3 output=patched_map"},
    {"input": "gis: How do I fill null (no-data) cells in a raster map?", "output": "Command: r.fillnulls\nExample: r.fillnulls input=raster_map output=filled_map"},
    {"input": "gis: How can I calculate statistics for a raster map?", "output": "Command: r.univar\nExample: r.univar map=raster_map"},
    {"input": "gis: How do I resample a raster map to a different resolution?", "output": "Command: r.resamp.interp\nExample: r.resamp.interp input=raster_map output=resampled_map method=bilinear"},
    {"input": "gis: How can I extract contour lines from a raster elevation map?", "output": "Command: r.contour\nExample: r.contour input=elevation_map output=contours step=10"},
    {"input": "gis: Is r.convert a valid command?",
     "output": "Command: Not recognized.\nExplanation: r.convert is not a valid GRASS GIS command. To convert vector to raster, use v.to.rast."},
    {"input": "gis: How do I calculate the slope for a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: How do I calculate slope?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: What command do I use for raster algebra?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How can I add two rasters together?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How do I create a vector map from a raster?", "output": "Command: r.to.vect\nExample: r.to.vect input=raster_map output=vector_map type=area"},
    {"input": "gis: How do I convert a raster map to vector?", "output": "Command: r.to.vect\nExample: r.to.vect input=raster_map output=vector_map type=area"},
    {"input": "gis: What command do I use to calculate the aspect of a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map aspect=aspect_map"},
    {"input": "gis: How can I calculate the aspect of a raster map?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map aspect=aspect_map"},
    {"input": "gis: How do I display a raster map?", "output": "Command: d.rast\nExample: d.rast map=raster_map"},
    {"input": "gis: How do I visualize a raster?", "output": "Command: d.rast\nExample: d.rast map=raster_map"},
    {"input": "gis: How can I list all available raster maps?", "output": "Command: g.list\nExample: g.list type=raster"},
    {"input": "gis: How do I view all raster maps?", "output": "Command: g.list\nExample: g.list type=raster"},
    {"input": "gis: How do I set the computational region to match a specific raster map?", "output": "Command: g.region\nExample: g.region raster=elevation_map"},
    {"input": "gis: How do I set region to match a raster map?", "output": "Command: g.region\nExample: g.region raster=elevation_map"},
    {"input": "gis: How do I import a GeoTIFF file into GRASS GIS?", "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: What command do I use to import a GeoTIFF?", "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: How do I export a raster map to a GeoTIFF file?", "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=output_file.tif format=GTiff"},
    {"input": "gis: How do I convert a raster map to GeoTIFF?", "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=output_file.tif format=GTiff"},
    {"input": "gis: How can I reproject a vector map to a different coordinate system?", "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How do I reproject a vector map?", "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How do I calculate the area of each polygon in a vector map?", "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I calculate area for vector polygons?", "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I buffer vector features by a specific distance?", "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I create buffer zones around vector features?", "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I clip a vector map using another vector map as a mask?", "output": "Command: v.overlay\nExample: v.overlay ainput=vector_map binput=mask_map operator=and output=clipped_map"},
    {"input": "gis: How do I clip a vector map?", "output": "Command: v.overlay\nExample: v.overlay ainput=vector_map binput=mask_map operator=and output=clipped_map"},
    {"input": "gis: How can I dissolve boundaries between adjacent polygons with the same attribute?", "output": "Command: v.dissolve\nExample: v.dissolve input=vector_map column=attribute_column output=dissolved_map"},
    {"input": "gis: How can I remove small areas (islands) from a vector map?", "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How do I remove islands from vector map?", "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How do I simplify the geometry of vector features?", "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How can I simplify vector features?", "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How do I convert a vector map to a raster map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How do I rasterize a vector map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How do I calculate the flow direction in a raster map?", "output": "Command: r.flow\nExample: r.flow input=elevation_map output=flow_direction"},
    {"input": "gis: How can I perform a watershed analysis?", "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map accumulation=acc_map"},
    {"input": "gis: How do I perform watershed analysis?", "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map accumulation=acc_map"},
    {"input": "gis: How do I calculate the flow accumulation in a raster map?", "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map accumulation=flow_accumulation"},
    {"input": "gis: How do I fill voids in a raster map?", "output": "Command: r.fillnulls\nExample: r.fillnulls input=raster_map output=filled_map"},
    {"input": "gis: How can I patch multiple raster maps into a single raster map?", "output": "Command: r.patch\nExample: r.patch input=map1,map2,map3 output=patched_map"},
    {"input": "gis: How do I resample a raster map to a different resolution?", "output": "Command: r.resamp.interp\nExample: r.resamp.interp input=raster_map output=resampled_map method=bilinear"},
    {"input": "gis: How can I extract contour lines from a raster elevation map?", "output": "Command: r.contour\nExample: r.contour input=elevation_map output=contours step=10"},
    {"input": "gis: How can I generate hillshade from a raster?", "output": "Command: r.relief\nExample: r.relief input=elevation_map output=hillshade"},
    {"input": "gis: How do I generate hillshade from a raster?", "output": "Command: r.relief\nExample: r.relief input=elevation_map output=hillshade"},
    {"input": "gis: How do I calculate solar radiation?", "output": "Command: r.sun\nExample: r.sun elevation=elevation_map glob_rad=solar_radiation"},
    {"input": "gis: How can I interpolate a raster map from scattered point data?", "output": "Command: v.surf.rst\nExample: v.surf.rst input=points_map zcolumn=value output=interpolated_raster"},
    {"input": "gis: How do I perform raster map algebra?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How do I calculate the topographic wetness index?", "output": "Command: r.topidx\nExample: r.topidx input=elevation_map output=twi_map"},
    {"input": "gis: How do I calculate curvature for a terrain?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map pcurvature=profile_curv tcurvature=tangential_curv"},
    {"input": "gis: How do I extract raster data from a vector map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I list all available vector maps?", "output": "Command: g.list\nExample: g.list type=vector"},
    {"input": "gis: How do I calculate the slope for raster A?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=raster_A slope=slope_A"},
    {"input": "gis: How can I perform raster map algebra for raster A?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster_A + raster_B'"},
    {"input": "gis: How do I create a vector map from raster B?", "output": "Command: r.to.vect\nExample: r.to.vect input=raster_B output=vector_B type=area"},
    {"input": "gis: How do I reproject vector map C?", "output": "Command: v.proj\nExample: v.proj input=vector_C location=target_location_C"},
    {"input": "gis: How can I list raster maps in mapset A?", "output": "Command: g.list\nExample: g.list type=raster mapset=mapset_A"},
    {"input": "gis: What if I use r.convert to rasterize a vector?",
     "output": "Command: Invalid.\nExplanation: Use v.to.rast for converting vector maps to raster."},
    {"input": "gis: How to convert a vector to raster?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: Convert vector map into raster format?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: Which tool turns a vector map into a raster?",
     "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I calculate slope for a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: How do I add two raster maps together?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: What command do I use to calculate the aspect of a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map aspect=aspect_map"},
    {"input": "gis: How do I convert a vector map to a raster map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I create buffer zones around vector features?", "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I reproject a vector map?", "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How can I find the area of a polygon in a vector map?", "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I extract contour lines from a raster?", "output": "Command: r.contour\nExample: r.contour input=elevation_map output=contours step=10"},
    {"input": "gis: How do I import a GeoTIFF file?", "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: How can I list all available vector maps?", "output": "Command: g.list\nExample: g.list type=vector"},
    {"input": "gis: What command can I use to export a raster map to a GeoTIFF?", "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=map.tif format=GTiff"},
    {"input": "gis: How do I calculate the flow direction in a raster map?", "output": "Command: r.flow\nExample: r.flow input=elevation_map output=flow_direction"},
    {"input": "gis: How can I perform a watershed analysis?", "output": "Command: r.watershed\nExample: r.watershed elevation=elevation_map accumulation=acc_map"},
    {"input": "gis: How do I fill voids in a raster map?", "output": "Command: r.fillnulls\nExample: r.fillnulls input=raster_map output=filled_map"},
    {"input": "gis: How can I simplify vector features?", "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How do I merge two vector maps?", "output": "Command: v.patch\nExample: v.patch input=vector_map1,vector_map2 output=merged_map"},
    {"input": "gis: What command do I use to calculate the curvature of a terrain?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map pcurvature=profile_curv tcurvature=tangential_curv"},
    {"input": "gis: How do I calculate the topographic wetness index?", "output": "Command: r.topidx\nExample: r.topidx input=elevation_map output=twi_map"},
    {"input": "gis: How can I merge multiple raster maps into one?", "output": "Command: r.patch\nExample: r.patch input=map1,map2,map3 output=merged_raster"},
    {"input": "gis: How do I remove islands from a vector map?", "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How do I rasterize a vector map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I calculate the distance from a raster map to a point?", "output": "Command: r.cost\nExample: r.cost input=cost_map output=cost_distance start_coordinates=100,200"},
]

# Augmentation function 
augmented_dataset = []

# variations
raster_map_variations = ['raster_A', 'raster_B', 'raster_C', 'elevation_map', 'topography_map', 'depth_map', 'dem_map', 'slope_map']
vector_map_variations = ['vector_A', 'vector_B', 'vector_C', 'polygon_map', 'line_map', 'area_map', 'region_map', 'boundary_map']

question_variations = {
    'How do I': ['What command is used to', 'How can I perform', 'What is the process to', 'How do I go about', 'Can you show me how to'],
    'Can I': ['Is it possible to', 'Is there a way to', 'How can I'],
}

command_variations = {
    # Raster Operations
    'r.slope.aspect': [
        'r.slope.aspect', 'r.calc.slope', 'r.slope', 'r.aspect', 'r.slope.calc',
        'r.terrain.slope', 'r.dem.slope', 'r.slope.model', 'r.slope.analysis', 
        'r.gradient.aspect'
    ],
    'r.mapcalc': [
        'r.mapcalc', 'r.calculate', 'r.math', 'r.map', 'r.calc', 'r.arithmetic', 
        'r.calc.expression', 'r.map.algebra', 'r.calc.raster', 'r.map.compute'
    ],
    'r.to.vect': [
        'r.to.vect', 'r.vectorize', 'r.convert.to.vector', 'r.raster.to.vector',
        'r.vect', 'r.raster2vect', 'r.vect.rasterize', 'r.vector.from.raster', 'r.vect.generate'
    ],
    'r.import': [
        'r.import', 'r.import_data', 'r.load', 'r.load.raster', 'r.import.raster', 
        'r.load.raster.file', 'r.read.tif', 'r.import.gdal'
    ],
    'r.out.gdal': [
        'r.out.gdal', 'r.export', 'r.export.gdal', 'r.save.gdal', 'r.convert.gdal', 
        'r.export_raster', 'r.gdal.write', 'r.to.gdal'
    ],
    'r.cost': [
        'r.cost', 'r.cost.distance', 'r.flow.cost', 'r.path.cost', 'r.cost.analysis',
        'r.distance.cost'
    ],
    'r.watershed': [
        'r.watershed', 'r.watershed.analysis', 'r.drainage', 'r.streamflow', 
        'r.hydro.watershed', 'r.hydro.delineate', 'r.basins.delineate', 'r.watershed.model'
    ],
    'r.viewshed': [
        'r.viewshed', 'r.visibility', 'r.visibility.analysis', 'r.sight', 'r.viewpoint', 
        'r.terrain.visibility', 'r.visibility.model'
    ],
    'r.fillnulls': [
        'r.fillnulls', 'r.nulls.fill', 'r.fill', 'r.raster.fill', 'r.missingdata.fill',
        'r.raster.interpolate', 'r.fill.no-data', 'r.fill.na'
    ],
    'r.resamp.interp': [
        'r.resamp.interp', 'r.resample', 'r.resampling', 'r.resample.method', 
        'r.interpolate', 'r.sampling', 'r.resampling.method'
    ],
    'r.sun': [
        'r.sun', 'r.calculate.solar', 'r.solar.irrad', 'r.solar.calculation', 'r.solar',
        'r.sun.irradiation', 'r.global.sun', 'r.solar.analysis', 'r.sun.compute'
    ],
    'r.contour': [
        'r.contour', 'r.contouring', 'r.extract.contours', 'r.contour.lines', 
        'r.terrain.contours', 'r.contour.generate', 'r.contour.extract', 'r.elevation.contours'
    ],

    # Vector Operations
    'v.proj': [
        'v.proj', 'v.reproject', 'v.project', 'v.reprojection', 'v.vector.project',
        'v.proj.reprojection', 'v.reproj', 'v.reprojection.vector'
    ],
    'v.buffer': [
        'v.buffer', 'v.create.buffer', 'v.zone', 'v.vector.buffer', 'v.spatial.buffer',
        'v.buffer.creation', 'v.create.zone', 'v.expand.buffer'
    ],
    'v.dissolve': [
        'v.dissolve', 'v.merge', 'v.combine', 'v.boundary.dissolve', 'v.union',
        'v.vector.dissolve', 'v.vector.merge', 'v.dissolve.features'
    ],
    'v.clean': [
        'v.clean', 'v.simplify', 'v.remove.islands', 'v.clean.tool', 'v.remove',
        'v.island.remove', 'v.remove.shapes', 'v.clean.vector', 'v.clean.remove'
    ],
    'v.generalize': [
        'v.generalize', 'v.simplify', 'v.simplification', 'v.generalization', 
        'v.vector.generalize', 'v.simplify.vector', 'v.generalization.simplify'
    ],
    'v.overlay': [
        'v.overlay', 'v.intersect', 'v.union', 'v.difference', 'v.symmetric.difference',
        'v.overlay.operation', 'v.combine.maps', 'v.combine.vector'
    ],
    'v.to.rast': [
        'v.to.rast', 'v.vector2raster', 'v.rasterize', 'v.convert.vector2raster', 
        'v.rasterize.map', 'v.convert.to.raster', 'v.rasterize.vector'
    ],
    'v.surf.rst': [
        'v.surf.rst', 'v.interpolate', 'v.surface.raster', 'v.surface.interpolation', 
        'v.raster.surf', 'v.rst.interpolate', 'v.surface.calculation'
    ],
    'v.patch': [
        'v.patch', 'v.merge', 'v.merge.vector', 'v.combine.vector', 'v.vector.merge',
        'v.patch.maps', 'v.combine.shapes', 'v.merge.maps'
    ],

    # File Management and Conversion
    'g.list': [
        'g.list', 'g.show', 'g.display', 'g.query', 'g.maps', 'g.show.maps', 
        'g.list.type', 'g.maps.list'
    ],
    'g.region': [
        'g.region', 'g.region.set', 'g.region.set.raster', 'g.set.region', 
        'g.raster.region', 'g.region.define', 'g.region.change'
    ],
    'g.import': [
        'g.import', 'g.import.file', 'g.load', 'g.load.map', 'g.import.data',
        'g.import.vector', 'g.import.raster'
    ],

    # Other GIS Functions
    'r.calc': [
        'r.calc', 'r.calculate', 'r.arithmetic', 'r.math', 'r.expression', 'r.calculate.raster', 
        'r.map.compute', 'r.compute.raster'
    ],
    'v.reclass': [
        'v.reclass', 'v.recode', 'v.reclassification', 'v.vector.reclass', 
        'v.map.recode', 'v.vector.reclassification'
    ],
    'v.extract': [
        'v.extract', 'v.select', 'v.filter', 'v.select.features', 'v.extract.features',
        'v.extract.vector'
    ],
    
    # Advanced GIS Functions
    'r.mapcalc': [
        'r.mapcalc', 'r.map.algebra', 'r.create.map', 'r.expression', 'r.calc.expression'
    ],
    'v.select': [
        'v.select', 'v.filter', 'v.select.features', 'v.extract.features', 'v.vector.select',
        'v.select.filter'
    ],
    'r.vector2raster': [
        'r.vector2raster', 'r.convert.vector2raster', 'v.to.rast', 'v.vector2raster',
        'r.vectorize'
    ],
}

def augment_test_case(test_case):
    input_text = test_case['input']
    output_text = test_case['output']
    
    # Replace raster and vector map names randomly
    input_text = input_text.replace('raster_map', random.choice(raster_map_variations))
    output_text = output_text.replace('raster_map', random.choice(raster_map_variations))
    
    input_text = input_text.replace('vector_map', random.choice(vector_map_variations))
    output_text = output_text.replace('vector_map', random.choice(vector_map_variations))
    
    # Apply random question rephrasing based on the command context
    if 'raster' in input_text or 'raster' in output_text:
        input_text = random.choice(question_variations.get('How do I', ['How do I'])) + input_text[5:]
    elif 'vector' in input_text or 'vector' in output_text:
        input_text = random.choice(question_variations.get('Can I', ['Can I'])) + input_text[5:]
    
    # Randomly choose commands with variations
    for command, variations in command_variations.items():
        if command in input_text:
            input_text = input_text.replace(command, random.choice(variations))
            output_text = output_text.replace(command, random.choice(variations))

    # Randomize parameters for commands
    if 'r.slope.aspect' in input_text or 'r.slope.aspect' in output_text:
        input_text = input_text.replace('elevation_map', random.choice(raster_map_variations))
        output_text = output_text.replace('elevation_map', random.choice(raster_map_variations))
    
    if 'r.mapcalc' in input_text or 'r.mapcalc' in output_text:
        input_text = input_text.replace('raster1', random.choice(raster_map_variations))
        output_text = output_text.replace('raster1', random.choice(raster_map_variations))
    
    # Add augmented case to the list
    augmented_dataset.append({"input": input_text, "output": output_text})

# Apply data augmentation to the existing dataset
for test_case in dataset:
    augment_test_case(test_case)

# Get augmented dataset
def get_dataset():
    return augmented_dataset