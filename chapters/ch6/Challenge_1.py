import arcpy
from arcpy import env
env.workspace = "H:/Fall 2015/Python Programming/Python/Data/Exercise06"
for feature in arcpy.ListFeatureClasses():
    dataset = arcpy.Describe(feature)
    print("Name: {:<20}  ShapeType: {}".format(dataset.basename, dataset.shapeType))
    
