import bpy

class ImageNodes(bpy.types.NodeTree):
    '''A custom node tree type that will show up in the editor type list'''
    bl_idname = 'ImageNodes'
    bl_label = "Image Nodes"
    bl_icon = 'FILE_IMAGE'