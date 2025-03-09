import os
import sys
import arcpy


def main():

    root_folder = arcpy.GetParameterAsText(0)
    shp_type = arcpy.GetParameterAsText(1)
    out_filename = arcpy.GetParameterAsText(2)+'.txt'
 
    msg = f'Writing {shp_type} feature class names '
    msg += f'under {root_folder} to {out_filename} ...'
    arcpy.AddMessage(msg)
    with open(out_filename, 'w') as outfile:
        walk = arcpy.da.Walk(root_folder, datatype="FeatureClass", type=shp_type)
        for ws, _, fc_list in walk:
            for fc in fc_list:
                arcpy.AddMessage(os.path.join(os.path.abspath(ws), fc))
                outfile.write(os.path.join(os.path.abspath(ws), fc) + '\n')
    arcpy.AddMessage('Done')


if __name__ == '__main__':
    main()
