# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

from mathutils import Vector
from enum import (
    Enum,
    Flag,
    auto
)
from .addon import user_prefs

# ------------------------------------------------------------------------------- #
# MODAL
# ------------------------------------------------------------------------------- #

class MODAL_STATUS(Enum):
    RUNNING       = 0
    INTERFACE     = 1
    FINISHED      = 2
    CANCELLED     = 3
    PASS_THROUGH  = 4


class GUI_STATUS(Enum):
    NEEDS_BUILD = 0
    UPDATED     = 1
    LOCKED      = 2


class PACK(Flag):
    NONE   = auto()
    LEFT   = auto()
    RIGHT  = auto()
    TOP    = auto()
    BOTTOM = auto()
