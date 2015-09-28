Challenge 2:
import arcpy
from arcpy import env

env.workspace = "E:/Fall 2015/Python Programming/Python/Data/Exercise05"
arcpy.AddXY_management("hospitalsXY.shp")
