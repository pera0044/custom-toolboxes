import sys
import arcpy

def main():
    prov = arcpy.GetParameterAsText(2)
    ws = arcpy.GetParameterAsText(0)
    column_name = arcpy.GetParameterAsText(1)

    arcpy.env.workspace = ws

    prov_field = arcpy.AddFieldDelimiters(ws, column_name)
    wc =  f"{prov_field}='{prov}'"
    arcpy.AddMessage ('Name,Prov,Longitude,Latitude')
    with arcpy.da.SearchCursor(ws, 
                               ['Name', column_name, 'SHAPE@XY'], 
                               where_clause=wc) as cursor:
        count = 0
        for row in cursor:
            count += 1
            name = row[0]
            prov = row[1]
            longitude = row[2][0]
            latitude = row[2][1]
            arcpy.AddMessage (f'{name},{prov},{longitude},{latitude}')
        arcpy.AddMessage (f'There are {count} cities in the above list')


if __name__ == '__main__':
    main()