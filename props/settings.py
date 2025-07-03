# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import os
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

class KT_PROPS_Settings(PropertyGroup):
    prop_1: BoolProperty()
    prop_2: BoolProperty()


    @staticmethod
    def draw(layout):
        prefs = user_prefs()
        settings = prefs.settings

        # Settings
        box = layout.box()
        box.label(text="Settings", icon='TOOL_SETTINGS')
        row = box.row(align=True)
        row.prop(settings, 'scripts_dir')
