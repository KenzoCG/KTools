# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import gpu
from mathutils import Vector
from .addon import user_prefs
from .enums import (
    GUI_STATUS,
    PACK,
)
from .graphics import (
    text_dims,
    text_heights,
    draw_text,
)
from .maths import Rect2D
from .screen import ScreenDimensions

# ------------------------------------------------------------------------------- #
# DATA
# ------------------------------------------------------------------------------- #

class Data:
    def __init__(self, context, event):
        # User
        self.prefs = user_prefs()
        # Standards
        self.screen = ScreenDimensions(context)
        self.padding = 0
        self.text_s = 0
        self.text_h = 0
        self.text_d = 0
        self.row_h = 0
        self.calc_standards()
        # References
        self.context = context
        self.event = event
        # Builder
        self.builder_current_x = 0
        self.builder_current_y = 0
        # Event
        self.locked_element = None
        # Draw
        self.scissor_on = False


    def calc_standards(self):
        gui = self.prefs.gui
        scale = self.screen.scale
        self.padding = round(gui.settings.padding * scale)
        self.text_s = gui.settings.text_size
        self.text_h, self.text_d = text_heights(self.text_s)
        self.row_h = round(self.padding + self.text_h + self.padding)


    def update(self, context, event):
        pass

# ------------------------------------------------------------------------------- #
# ELEMENTS
# ------------------------------------------------------------------------------- #
