# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import traceback
import time
from mathutils import (
    Vector,
    Matrix,
    Quaternion
)
from bpy.props import (
    FloatProperty,
)
from .. import utils

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

class KT_OT_GenTerrain(bpy.types.Operator):
    bl_idname      = "kt.gen_terrain"
    bl_label       = "KTools Generate Terrain"
    bl_options     = {'REGISTER', 'UNDO'}
    bl_description = "KTools - Generate Terrain"

    width: FloatProperty(
        name="Width",
        description="Box Width",
        min=0.01, max=100.0,
        default=1.0,
    )
    height: FloatProperty(
        name="Height",
        description="Box Height",
        min=0.01, max=100.0,
        default=1.0,
    )
    depth: FloatProperty(
        name="Depth",
        description="Box Depth",
        min=0.01, max=100.0,
        default=1.0,
    )


    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'


    def execute(self, context):
        obj = utils.objects.create_obj_mesh(obj_name="Object", mesh_name="Mesh", loc=Vector((0,0,0)), rot=Quaternion(), scale=Vector((1,1,1,)))

        return {'FINISHED'}



