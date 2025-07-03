# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    PointerProperty,
    EnumProperty,
    IntProperty,
    FloatProperty,
    BoolProperty,
    StringProperty,
)
from ..utils.addon import user_prefs

# ------------------------------------------------------------------------------- #
# PROPS
# ------------------------------------------------------------------------------- #

class KT_PROPS_Dev(PropertyGroup):
    debug : BoolProperty(name="Debug", default=False)

    @staticmethod
    def draw(layout):
        prefs = user_prefs()
        dev = prefs.dev

        # Settings
        box = layout.box()
        box.label(text="Dev", icon='TOOL_SETTINGS')
        row = box.row(align=True)
        row.prop(dev, 'debug')
