import os
import arcpy
import sys

def main():

    in_gdbs_base_folder = arcpy.GetParameterAsText(0)
    out_gdb_folder = f"{arcpy.GetParameterAsText(1)}\\"
    out_gdb_name = arcpy.GetParameterAsText(2)
    out_feature_dataset = arcpy.GetParameterAsText(3)

    arcpy.env.overwriteOutput = True
    
    arcpy.env.workspace = in_gdbs_base_folder
    ws_list = arcpy.ListWorkspaces()
    arcpy.env.workspace = ws_list[0]
    first_fc = arcpy.ListFeatureClasses()[0]
    sr = arcpy.da.Describe(first_fc)['spatialReference']
    arcpy.management.CreateFileGDB(out_folder_path=out_gdb_folder,
                                   out_name=out_gdb_name)
    arcpy.management.CreateFeatureDataset(out_dataset_path=os.path.join(out_gdb_folder, out_gdb_name + '.gdb'),
                                          out_name=out_feature_dataset,
                                          spatial_reference=sr)
    out_path = os.path.join(out_gdb_folder, out_gdb_name + '.gdb', out_feature_dataset)
    for ws in ws_list:
        arcpy.env.workspace = ws
        fc_list = arcpy.ListFeatureClasses()
        for fc in fc_list:
            arcpy.AddMessage(f'Copying {fc} ...')
            arcpy.FeatureClassToGeodatabase_conversion(fc, out_path)
    arcpy.env.workspace = out_path
    arcpy.AddMessage('Checking output ...')
    for fc in arcpy.ListFeatureClasses():
        arcpy.AddMessage(f"  , {fc}")
    arcpy.AddMessage('Done')


if __name__ == '__main__':
    main()
