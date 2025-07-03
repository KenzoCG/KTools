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
    COLORS,
    get_color,
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

class Label:
    def __init__(self, ID='', text="", pack=PACK.NONE, text_color=COLORS.NONE, bg_color=COLORS.NONE):
        self.boundary = Rect2D()
        self.ID = ID
        self.pack = pack
        self.text = text
        self.text_color = get_color(text_color)
        self.bg_color = get_color(bg_color)


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def close(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class Button:
    def __init__(self, ID='', text="", pack=PACK.NONE, text_color=COLORS.NONE, bg_color=COLORS.NONE, callback=None, args=None):
        self.boundary = Rect2D()
        self.ID = ID
        self.pack = pack
        self.text = text
        self.text_color = get_color(text_color)
        self.bg_color = get_color(bg_color)
        self.callback = callback
        self.args = args


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def close(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass

# ------------------------------------------------------------------------------- #
# CONTAINERS
# ------------------------------------------------------------------------------- #

class Row:
    def __init__(self, ID='', pack=PACK.NONE, bg_color=COLORS.NONE):
        self.boundary = Rect2D()
        self.ID = ID
        self.pack = pack
        self.bg_color = get_color(bg_color)
        self.elements = []


    def build(self, DT:Data):
        for element in self.elements:
            element.build(DT)


    def update(self, DT:Data):
        for element in self.elements:
            element.update(DT)


    def close(self, DT:Data):
        for element in self.elements:
            element.close(DT)


    def draw_2d(self, DT:Data):
        for element in self.elements:
            element.draw_2d(DT)


class Panel:
    def __init__(self, ID='', width=0, height=0):
        self.boundary = Rect2D(x=0, y=0, w=width, h=height)
        self.ID = ID
        self.bg_color = get_color(COLORS.PANEL_BG)
        self.width = width
        self.height = height
        self.elements = []
        self.rows = []


    def row(self, ID='', pack=PACK.NONE):
        row = Row(ID, pack)
        return row


    def build(self, DT:Data):
        for row in self.rows:
            row.build(DT)


    def update(self, DT:Data):
        for row in self.rows:
            row.update(DT)


    def close(self, DT:Data):
        for row in self.rows:
            row.close(DT)


    def draw_2d(self, DT:Data):
        for row in self.rows:
            row.draw_2d(DT)

# ------------------------------------------------------------------------------- #
# MENU
# ------------------------------------------------------------------------------- #

class Menu:
    def __init__(self, context, event):
        self.boundary = Rect2D()
        self.status = GUI_STATUS.NEEDS_BUILD
        self.DT = Data(context, event)
        self.panels = []


    def build(self):
        self.status = GUI_STATUS.NEEDS_BUILD
        for panel in self.panels:
            panel.build(self.DT)
        self.status = GUI_STATUS.UPDATED


    def update(self, context, event):
        self.DT.update(context, event)
        if self.status == GUI_STATUS.NEEDS_BUILD:
            self.build(context)
        if self.status == GUI_STATUS.LOCKED:
            element = self.DT.locked_element
            element.update(self.DT)
        else:
            self.status = GUI_STATUS.UPDATED
            for panel in self.panels:
                panel.update(self.DT)


    def close(self, context):
        for panel in self.panels:
            panel.close(self.DT)


    def draw_2d(self, context):
        for panel in self.panels:
            panel.draw_2d(self.DT)

