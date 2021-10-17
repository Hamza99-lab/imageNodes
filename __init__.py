bl_info = {
    "name": "Image Nodes",
    "author": "Hamza",
    "blender": (2, 93, 2),
    "location": "Editor type",
    "description": "A node-based image processing add-on",
    "warning": "",
    "doc_url": "",
    "category": "Node Tree",
}

from . import auto_load

auto_load.init()

def register():
    auto_load.register()
    

def unregister():
    auto_load.unregister()
