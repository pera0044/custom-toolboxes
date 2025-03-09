import os
import sys
import arcpy


def main():
    
    arcpy.env.overwriteOutput = True
    
    in_ws   = arcpy.GetParameterAsText(0)
    clip_ws = arcpy.GetParameterAsText(1)
    out_ws  = arcpy.GetParameterAsText(2)

    arcpy.env.workspace = in_ws
    in_fc_list = arcpy.ListFeatureClasses()

    arcpy.env.workspace = clip_ws
    clip_fc_list = arcpy.ListFeatureClasses()

    for in_fc in in_fc_list:
        in_fc_path = os.path.join(in_ws, in_fc)
        in_fc_base = arcpy.Describe(in_fc_path).basename
        for clip_fc in clip_fc_list:
            clip_fc_path = os.path.join(clip_ws, clip_fc)
            clip_fc_base = arcpy.Describe(clip_fc_path).basename
            out_fc  = f'{clip_fc_base}_{in_fc_base}'
            out_fc_path = os.path.join(out_ws, out_fc)
            arcpy.AddMessage( (f'{out_fc} ...'))
            arcpy.Clip_analysis(in_fc_path,
                                clip_fc_path,
                                out_fc_path)

if __name__ == '__main__':
    main()