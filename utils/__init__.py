# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from . import addon
from . import algos
from . import enums
from . import event
from . import graphics
from . import handles
from . import inspector
from . import maths
from . import object
from . import paths
from . import ray
from . import screen

from . import gui

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    from .handles import remove_shader_handles
    bpy.app.handlers.load_post.append(remove_shader_handles)


def unregister():
    from .handles import remove_shader_handles
    bpy.app.handlers.load_post.remove(remove_shader_handles)
