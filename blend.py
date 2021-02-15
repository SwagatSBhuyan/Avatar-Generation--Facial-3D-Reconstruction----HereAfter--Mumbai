import os
current_directory = os.getcwd()

f = open("img.txt", "r")
filer = str(f.read())
f.close()

import bpy
bpy.ops.object.delete(use_global=False, confirm=False)
file_loc = str(current_directory) + '\\ply_output\\' + str(filer) +'PLYWithRGB.ply'
# file_loc = 'trump.obj'
bpy.ops.import_mesh.ply(filepath=file_loc)


# C = bpy.context
# scene = C.scene

ob = bpy.context.selected_objects[0]

# bpy.context.view_layer.objects.active = ob
# ob.select_set(True)

bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.remove_doubles() #remove doubles
bpy.ops.mesh.tris_convert_to_quads() #tris to quads
bpy.ops.mesh.unsubdivide()
bpy.ops.mesh.unsubdivide()
bpy.ops.object.mod
        
bpy.ops.transform.resize(value=(0.2, 0.2, 0.2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(3.39313e-16, 0.231043, 1.52813), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.resize(value=(0.556969, 0.556969, 0.556969), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(8.07558e-19, 0.000909229, 0.00363692), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.resize(value=(1.0541, 1.0541, 1.0541), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=0.243269, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(-0.0464798, 0.000654645, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=0.0379734, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=0.0778394, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, 0, -0), (-0, -1.34359e-07, 1), (0, 1, 1.34359e-07)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(-0.010998, -1.05549e-09, 0.00785574), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value=-0.170775, orient_axis='Z', orient_type='VIEW', orient_matrix=((4.93038e-32, 1, 2.22045e-16), (2.22045e-16, 4.93038e-32, 1), (-1, -2.22045e-16, -4.93038e-32)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(-2.42267e-18, 0.00600091, -0.0109108), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.transform.resize(value=(0.87862, 0.87862, 0.87862), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


file_loc_out = str(current_directory) + '\\final_output\\' + str(filer) + '_final.ply'
bpy.ops.export_mesh.ply(filepath=file_loc_out)

