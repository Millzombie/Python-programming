import arcpy
from arcpy import env
env.workspace = "E:/Fall 2015/Python Programming/Python/data/Exercise07"
fc = "roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
arcpy.AddField_management(fc, newfield, fieldtype)
cursor = arcpy.da.UpdateCursor(fc, ["FERRY"], '"FEATURE" = \'Ferry Crossing\'')
for row in cursor:
    row[0] = "YES"
    cursor.updateRow(row)
    
cursor2 = arcpy.da.UpdateCursor(fc, ["FERRY"], '"FEATURE" = \'Ferry Crossing\'')  
for row in cursor2:
    row[0] = "NO"
    cursor2.updateRow(row)
