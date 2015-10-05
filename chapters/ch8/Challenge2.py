"""Write a script that determines the perimeter ( in meters ) and area ( in
square meters ) of each of the individual islands of the Hawaii.shp feature
class. Recall that this is a multipart feature class."""
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor
