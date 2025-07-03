# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from ..utils.addon import (
    user_prefs,
    name_and_ver
)

# ------------------------------------------------------------------------------- #
# BASE
# ------------------------------------------------------------------------------- #

class KT_Panel_V3D(bpy.types.Panel):
    bl_label = 'KT_Panel_V3D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "KTools"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}

# ------------------------------------------------------------------------------- #
# PANELS
# ------------------------------------------------------------------------------- #

class KT_PT_Ops_V3D(KT_Panel_V3D):
    bl_label = name_and_ver()
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        prefs = user_prefs()
        box = self.layout.box()
        box.operator("wm.url_open", text="Docs").url = "https://kenzocg.github.io"


class KT_PT_Settings_V3D(KT_Panel_V3D):
    bl_label = "Settings"

    def draw(self, context):
        prefs = user_prefs()
        settings = prefs.settings
        box = self.layout.box()
        box.prop(settings, 'prop_1', text="Demo Prop 1")
        box.prop(settings, 'prop_2', text="Demo Prop 2")
