# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    AddonPreferences,
    PropertyGroup,
)
from bpy.props import (
    PointerProperty,
    EnumProperty,
    IntProperty,
    FloatProperty,
    BoolProperty,
    StringProperty,
)
from .dev import KT_PROPS_Dev
from .gui import KT_PROPS_GUI
from .settings import KT_PROPS_Settings
from ..utils.addon import name

# ------------------------------------------------------------------------------- #
# ADDON PREFS
# ------------------------------------------------------------------------------- #

class KT_ADDON_Prefs(AddonPreferences):
    bl_idname = name()
    settings : PointerProperty(type=KT_PROPS_Settings)
    dev      : PointerProperty(type=KT_PROPS_Dev)
    gui      : PointerProperty(type=KT_PROPS_GUI)
    tab_opts = (
        ('SETTINGS', "Settings" , ""),
        ('INFO'    , "Info"     , ""),
        ('GUI'     , "GUI"      , ""),
        ('DEV'     , "Dev"      , ""),
    )
    tabs: EnumProperty(name="tabs", items=tab_opts, default='SETTINGS')


    def draw(self, context):
        row = self.layout.row()
        row.prop(self, 'tabs', expand=True)
        if self.tabs == 'SETTINGS':
            KT_PROPS_Settings.draw(self.layout)
        elif self.tabs == 'INFO':
            draw_info(self.layout)
        elif self.tabs == 'GUI':
            KT_PROPS_GUI.draw(self.layout)
        elif self.tabs == 'DEV':
            KT_PROPS_Dev.draw(self.layout)


def draw_info(layout):
    # Websites
    box = layout.box()
    box.label(text="Web Pages", icon='WORLD')
    row = box.row(align=True)
    row.operator("wm.url_open", text="YouTube").url = "https://www.youtube.com/@cg-boundary"
    row = box.row(align=True)
    row.operator("wm.url_open", text="Website").url = "https://kenzocg.github.io"

    # Contact
    box = layout.box()
    row = box.row()
    row.label(text="Contact", icon='USER')
    row = box.row()
    row.label(text="cg.boundary@gmail.com")

