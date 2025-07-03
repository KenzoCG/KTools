# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from mathutils import (
    Vector,
    Matrix,
    Quaternion
)

# ------------------------------------------------------------------------------- #
# MANAGE
# ------------------------------------------------------------------------------- #

def create_obj_mesh(obj_name="Object", mesh_name="Mesh", loc=Vector((0,0,0)), rot=Quaternion(), scale=Vector((1,1,1,))):
    """
    Info
        Create an object of type mesh and link it to the scene collection
    Params
        Strings and mathutils types
    Return
        bpy.types.Object
    """
    mesh = bpy.data.meshes.new(name=mesh_name)
    obj = bpy.data.objects.new(name=obj_name, object_data=mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.matrix_world = Matrix.LocRotScale(loc, rot, scale)
    return obj


def delete_obj_mesh(obj=None):
    """
    Info
        Check if obj is mesh, attemps to remove from blend file
    Params
        The object to remove
    Return
        True if unlinked else False
    """
    if isinstance(obj, bpy.types.Object) and obj.type == 'MESH':
        if obj.name in bpy.data.objects:
            mesh = obj.data
            bpy.data.objects.remove(obj, do_unlink=True, do_id_user=True, do_ui_user=True)
            if mesh.name in bpy.data.meshes:
                bpy.data.meshes.remove(mesh, do_unlink=True, do_id_user=True, do_ui_user=True)
                return True
    return False
