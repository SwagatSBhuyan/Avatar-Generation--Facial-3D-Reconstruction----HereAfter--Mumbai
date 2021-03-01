import os
import argparse
current_directory = os.getcwd()

f = open("img.txt", "r")
filer = str(f.read())
f.close()


import bpy
import mathutils

bpy.ops.object.delete(use_global=False, confirm=False)
file_loc = str(current_directory) + '\\final_output\\' + str(filer) + '_final.ply'
bpy.ops.import_mesh.ply(filepath=file_loc)
ob = bpy.context.selected_objects[0]

file_loc_bake = str(current_directory) + '\\textures\\' + str(filer) + '_texture.png'
file_loc_uv = str(current_directory) + '\\UV\\' + str(filer) + '_uv.png'


bpy.ops.object.editmode_toggle()
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.tris_convert_to_quads()
bpy.ops.mesh.unsubdivide()

bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()



img = bpy.ops.image.new(name='hola', width=1024, height=1024)
# bpy.context.view_layer.objects.active = ob
bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
# bpy.ops.uv.export_layout(filepath=file_loc_uv, mode='PNG', opacity=0)
bpy.ops.object.editmode_toggle()



mat = bpy.data.materials.new(name = "Material.001")
mat.use_nodes = True #Make so it has a node tree
#Add the vertex color node
vc = mat.node_tree.nodes.new('ShaderNodeVertexColor')
# bpy.ops.node.add_node(type="ShaderNodeTexImage", use_transform=False)
#Assign its layer
vc.layer_name = "Col"
#Get the shader
bsdf = mat.node_tree.nodes["Principled BSDF"]
#Link the vertex color to the shader
mat.node_tree.links.new( vc.outputs[0], bsdf.inputs[0] )
# Image Texture
tex = mat.node_tree.nodes.new('ShaderNodeTexImage')
tex.image=bpy.data.images['hola']

ob.data.materials.append(mat)


# color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False

##bpy.data.images.new("jes", width=1024, height=1024)
# bpy.ops.object.editmode_toggle()
# bpy.ops.mesh.select_all(action='SELECT')
# obj = bpy.context.window.scene.objects[0]
# bpy.context.view_layer.objects.active = obj
# bpy.ops.object.select_all(action='TOGGLE')
# bpy.context.scene.objects.active = bpy.context.scene.objects[0]

# bpy.ops.uv.export_layout(filepath=file_loc_bake, mode='PNG', opacity=0)
## bpy.ops.node.add_search(use_transform=True, node_item='41')
#bpy.ops.object.editmode_toggle()

## bpy.ops.image.save_as(save_as_render=False, filepath=str(file_loc_bake), relative_path=True, show_multiview=False, use_multiview=False)


bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.bake_type = 'DIFFUSE'
bpy.context.scene.render.bake.use_pass_direct = False
bpy.context.scene.render.bake.use_pass_indirect = False


# bpy.context.view_layer.objects.active = ob
bpy.ops.object.bake(type='DIFFUSE')

# img.save_render(filepath=file_loc_bake)

# bpy.ops.image.save()
# img = bpy.data.images['hola']
# img.filepath = file_loc_bake
# img.file_format = 'PNG'
# img.save()

bpy.data.images['hola'].save_render(filepath=file_loc_bake)
# bpy.ops.image.save_as(save_as_render=False, filepath="C:\\Users\\swaga\\Pictures\\klk.png", relative_path=True, show_multiview=False, use_multiview=False)


## bpy.ops.image.save()

#file_loc_out = str(current_directory) + '\\final_output\\' + str(filer) + '_final.ply'
#bpy.ops.export_mesh.ply(filepath=file_loc_out)

