"""Write a script that creates a new polygon feature class containing a
single ( square ) polygon with the following coordinates: ( 0, 0 ), ( 0, 1,000 ),
( 1,000, 0 ), and ( 1,000, 1,000 )."""
import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "E:Fall 2015/Python Programming/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "E:Fall 2015/Python Programming/Python/Data/Exercise08"
newfc = "newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")

