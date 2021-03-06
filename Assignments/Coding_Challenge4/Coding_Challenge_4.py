import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

env.workspace = r"C:\NRS_528\Assignment4"

# Input point features to go through thiessen polygon execution.
# In this case, I used emergency medical locations downloaded from RIGIS to visualize areas with the closest EMS location.

inFeatures = "Emergency_Medical_Services.shp"
outFeatureClass = "EMS_Thiessen"
outFields = "ALL"

print('Creating Thiessen Polygons from:' + inFeatures)

arcpy.CreateThiessenPolygons_analysis(inFeatures, outFeatureClass, outFields)

# Clip data for desired analysis location. In this example, I clipped the thiessen data to RI, as the
# thiessen data from earlier goes beyond the extent of RI.

in_features = "EMS_Thiessen.shp"
clip_features = "Municipalities__1997_.shp"
out_feature_class = "EMS_Thiessen_riclipped"

print('Clipping study area from:' + clip_features)

arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

if arcpy.Exists(out_feature_class + ".shp"):
    print('Complete!')
