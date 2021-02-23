import os
current_directory = os.getcwd()

f = open("img.txt", "r")
filer = str(f.read())
f.close()

import bpy
bpy.ops.object.delete(use_global=False, confirm=False)
file_loc = str(current_directory) + '\\ply_output\\' + str(filer) +'PLYWithRGB.ply'
file_loc2 = str(current_directory) + '\\ori_mesh\\Head.fbx'
# file_loc = 'trump.obj'
bpy.ops.import_mesh.ply(filepath=file_loc)


# C = bpy.context
# scene = C.scene

ob = bpy.context.selected_objects[0]

# bpy.context.view_layer.objects.active = ob
# ob.select_set(True)

bpy.ops.transform.rotate(value=-1.4581, orient_axis='Z', orient_type='VIEW', orient_matrix=((4.93038e-32, 1, 2.22045e-16), (2.22045e-16, 4.93038e-32, 1), (-1, -2.22045e-16, -4.93038e-32)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=0.280344, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.resize(value=(0.129632, 0.129632, 0.129632), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(3.41245e-16, -0.0601607, 1.53683), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(-5.85646e-19, -0.0290127, -0.00263752), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.resize(value=(0.896985, 0.896985, 0.896985), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)




file_loc_out = str(current_directory) + '\\final_output\\' + str(filer) + '_final.ply'
bpy.ops.export_mesh.ply(filepath=file_loc_out)

