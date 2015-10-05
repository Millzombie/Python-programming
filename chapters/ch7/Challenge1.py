import arcpy
from arcpy import env
env.workspace = "E:/Fall 2015/Python Programming/Python/data/Exercise07"
fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("Results/buffer.shp")
arcpy.Buffer_analysis(fc, unique_name, "15000 METERS")
arcpy.Buffer_analysis(fc, unique_name, "7500 METERS")
