import os
import argparse
current_directory = os.getcwd()

f = open("img.txt", "r")
filer = str(f.read())
f.close()

import bpy
import mathutils
bpy.ops.object.delete(use_global=False, confirm=False)
file_loc = str(current_directory) + '\\final_output\\' + str(filer) +'_final.ply'
file_loc_2 = str(current_directory) + '\\ori_mesh\\Head.fbx'


def rendering(file_loc, ply_or_fbx):

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    
    if ply_or_fbx == 0:
        bpy.ops.import_mesh.ply(filepath=file_loc)
    else:
        bpy.ops.import_scene.fbx(filepath=file_loc)

    ob = bpy.context.selected_objects[0]

    if ply_or_fbx == 0:
        mat = bpy.data.materials.new(name = "Material.001")
        mat.use_nodes = True #Make so it has a node tree
        #Add the vertex color node
        vc = mat.node_tree.nodes.new('ShaderNodeVertexColor')
        #Assign its layer
        # vc.layer_name = "skin"
        #Get the shader
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        #Link the vertex color to the shader
        mat.node_tree.links.new( vc.outputs[0], bsdf.inputs[0] )
        ob.data.materials.append(mat)

    # Create the camera
    cam_data = bpy.data.cameras.new('camera')
    cam = bpy.data.objects.new('camera', cam_data)
    bpy.context.scene.camera = cam
    cam.location = mathutils.Vector((0, -1.49, 1.5))
    cam.rotation_euler = mathutils.Euler((1.57, 0, 0))

    # Create Lighting
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, -1.68, 1.94), scale=(0.75, 0, 0))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-0.5, -1.68, 1.94), scale=(0.75, 0, 0))

    # Rendering
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            space.shading.type = 'RENDERED'

    # Saving Render Image File
    bpy.context.scene.render.image_settings.file_format='JPEG'
    if ply_or_fbx == 0:
        bpy.context.scene.render.filepath = str(current_directory) + '\\render_images\\' + str(filer) +'.jpg'
    else:
        bpy.context.scene.render.filepath = str(current_directory) + '\\render_images\\head.jpg'
    
    bpy.ops.render.render(use_viewport = True, write_still=True)

    
rendering(file_loc, 0)
rendering(file_loc_2, 1)
