import arcpy
from arcpy import env

env.workspace = "E:\Fall 2015\Python Programming\Python\Data\Exercise05

if arcpy.CheckExtension("spatial" and "3D" and "Network") == "Available":
    print "The following extensions are available: ArcGIS 3D Analyst, ArcGIS Network Analyst, ArcGIS Spatial Analyst."
