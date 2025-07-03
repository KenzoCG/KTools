# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    PointerProperty,
    BoolProperty,
    FloatProperty,
    EnumProperty,
    IntProperty,
    FloatVectorProperty
)
from ..utils.addon import user_prefs

# ------------------------------------------------------------------------------- #
# PROPS
# ------------------------------------------------------------------------------- #

class KT_PROPS_GUI_Colors(PropertyGroup):
    text_primary  : FloatVectorProperty(name="Text Primary" , size=4, min=0, max=1, subtype='COLOR', default=(1, 1, 1, 1))
    text_contrast : FloatVectorProperty(name="Text Contrast", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 1))


class KT_PROPS_GUI_Settings(PropertyGroup):
    padding   : IntProperty(name="UI Padding", min=3, max=10, default=3)
    text_size : IntProperty(name="Text Size", min=8, max=24, default=12)


class KT_PROPS_GUI(PropertyGroup):
    settings : PointerProperty(type=KT_PROPS_GUI_Settings)
    colors   : PointerProperty(type=KT_PROPS_GUI_Colors)

    @staticmethod
    def draw(layout):
        prefs = user_prefs()
        gui = prefs.gui
        settings = gui.settings
        colors = gui.colors
        # Settings
        box = layout.box()
        box.label(text="GUI Settings", icon='TOOL_SETTINGS')
        row = box.row(align=True)
        row.prop(settings, 'padding', text="Padding")
        row = box.row(align=True)
        row.prop(settings, 'text_size', text="Text Size")
        # Colors
        box = layout.box()
        box.label(text="GUI Colors", icon='COLOR')
        # Text
        row = box.row(align=True)
        row.prop(colors, 'text_primary' , text="Text Primary")
        row = box.row(align=True)
        row.prop(colors, 'text_contrast', text="Text Contrast")
