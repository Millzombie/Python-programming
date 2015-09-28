import arcpy
arcpy.env.workspace = "E:\Fall 2015\Python Programming\Python\Data\Exercise05")
outputClass = "E:\Fall 2015\Python Programming\Python\Data\")
arcpy.Dissolve_management("parks.shp", outputClass, "PARK_TYPE", "", "SINGLE_PART", "")
