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
    mesh = bpy.data.meshes.new(name=mesh_name)
    obj = bpy.data.objects.new(name=obj_name, object_data=mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.matrix_world = Matrix.LocRotScale(loc, rot, scale)
    return obj


def delete_obj_mesh(obj=None):
    if isinstance(obj, bpy.types.Object) and obj.type == 'MESH':
        if obj.name in bpy.data.objects:
            mesh = obj.data
            bpy.data.objects.remove(obj, do_unlink=True, do_id_user=True, do_ui_user=True)
            if mesh.name in bpy.data.meshes:
                bpy.data.meshes.remove(mesh, do_unlink=True, do_id_user=True, do_ui_user=True)
                return True
    return False
