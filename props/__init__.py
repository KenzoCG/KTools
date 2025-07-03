# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.props import PointerProperty
# Addon Prefs
from .dev import KT_PROPS_Dev
from .gui import (
    KT_PROPS_GUI_Settings,
    KT_PROPS_GUI_Colors,
    KT_PROPS_GUI
)
from .settings import KT_PROPS_Settings
from .addon import KT_ADDON_Prefs
# ID Props
from .object import KT_PROPS_Object
from .mesh import KT_PROPS_Mesh

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # Addon Prefs
    KT_PROPS_Dev,
    KT_PROPS_GUI_Settings,
    KT_PROPS_GUI_Colors,
    KT_PROPS_GUI,
    KT_PROPS_Settings,
    KT_ADDON_Prefs,
    # ID Props
    KT_PROPS_Object,
    KT_PROPS_Mesh,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)

    bpy.types.Object.pynodes = PointerProperty(type=KT_PROPS_Object)
    bpy.types.Mesh.pynodes = PointerProperty(type=KT_PROPS_Mesh)


def unregister():
    del bpy.types.Object.pynodes
    del bpy.types.Mesh.pynodes

    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)
