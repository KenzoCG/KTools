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
    # Text
    text_primary  : FloatVectorProperty(name="Text Primary" , size=4, min=0, max=1, subtype='COLOR', default=(1, 1, 1, 1))
    text_contrast : FloatVectorProperty(name="Text Contrast", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 1))
    text_preview  : FloatVectorProperty(name="Text Preview" , size=4, min=0, max=1, subtype='COLOR', default=(1, 0.033105, 0.033105, 1))
    text_keyword  : FloatVectorProperty(name="Text Keyword" , size=4, min=0, max=1, subtype='COLOR', default=(0.318545, 0.033104, 1, 1))
    text_muted    : FloatVectorProperty(name="Text Muted"   , size=4, min=0, max=1, subtype='COLOR', default=(0.132867, 0.132867, 0.132867, 1))
    text_function : FloatVectorProperty(name="Text Function", size=4, min=0, max=1, subtype='COLOR', default=(0, 1, 0, 1))
    # Element
    menu_bg        : FloatVectorProperty(name="Menu Background"      , size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 1))
    border         : FloatVectorProperty(name="Border"               , size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 1))
    header_bg      : FloatVectorProperty(name="Header Background"    , size=4, min=0, max=1, subtype='COLOR', default=(0.033105, 0, 0.132868, 1))
    category_bg    : FloatVectorProperty(name="Category Background"  , size=4, min=0, max=1, subtype='COLOR', default=(0.074213, 0.074213, 0.074213, 1))
    panel_bg       : FloatVectorProperty(name="Panel Background", size=4, min=0, max=1, subtype='COLOR', default=(0.033105, 0.033105, 0.033105, 1))
    scrollbar_bg   : FloatVectorProperty(name="Scrollbar Background" , size=4, min=0, max=1, subtype='COLOR', default=(0.132867, 0, 0.603827, 1))
    scrollbar_grip : FloatVectorProperty(name="Scrollbar Grip"       , size=4, min=0, max=1, subtype='COLOR', default=(0.033105, 0, 0.132868, 1))
    btn_alert      : FloatVectorProperty(name="Button Alert"         , size=4, min=0, max=1, subtype='COLOR', default=(0.318545, 0, 0, 1))
    btn_main       : FloatVectorProperty(name="Button Main"          , size=4, min=0, max=1, subtype='COLOR', default=(0, 1, 0, 1))
    # Editor
    editor_bg     : FloatVectorProperty(name="Editor Background", size=4, min=0, max=1, subtype='COLOR', default=(0.01033, 0.01033, 0.01033, 1))
    editor_line   : FloatVectorProperty(name="Editor Line"      , size=4, min=0, max=1, subtype='COLOR', default=(0.033105, 0.033105, 0.033105, 1))
    editor_cursor : FloatVectorProperty(name="Editor Cursor"    , size=4, min=0, max=1, subtype='COLOR', default=(1, 1, 0.033105, 1))
    # Node
    node_wire : FloatVectorProperty(name="Node Wire", size=4, min=0, max=1, subtype='COLOR', default=(0.318544, 1, 0.318547, 1))


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
        row = box.row(align=True)
        row.prop(colors, 'text_preview' , text="Text Preview")
        row = box.row(align=True)
        row.prop(colors, 'text_keyword' , text="Text Keyword")
        row = box.row(align=True)
        row.prop(colors, 'text_muted'   , text="Text Muted")
        row = box.row(align=True)
        row.prop(colors, 'text_function', text="Text Function")
        # Element
        row = box.row(align=True)
        row.prop(colors, 'menu_bg', text="Menu Background")
        row = box.row(align=True)
        row.prop(colors, 'border', text="Border")
        row = box.row(align=True)
        row.prop(colors, 'header_bg', text="Header Background")
        row = box.row(align=True)
        row.prop(colors, 'category_bg', text="Category Background")
        row = box.row(align=True)
        row.prop(colors, 'panel_bg', text="Panel Background")
        row = box.row(align=True)
        row.prop(colors, 'scrollbar_bg', text="Scrollbar Background")
        row = box.row(align=True)
        row.prop(colors, 'scrollbar_grip', text="Scrollbar Grip")
        row = box.row(align=True)
        row.prop(colors, 'btn_alert', text="Button Alert")
        row = box.row(align=True)
        row.prop(colors, 'btn_main', text="Button Main")
        # Editor
        row = box.row(align=True)
        row.prop(colors, 'editor_bg', text="Editor Background")
        row = box.row(align=True)
        row.prop(colors, 'editor_line', text="Editor Line")
        row = box.row(align=True)
        row.prop(colors, 'editor_cursor', text="Editor Cursor")
        # Node
        row = box.row(align=True)
        row.prop(colors, 'node_wire', text="Node Wire")
