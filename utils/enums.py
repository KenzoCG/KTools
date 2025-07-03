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


class COLORS(Enum):
    NONE = -1
    # Text
    TEXT_PRIMARY  = 0
    TEXT_CONTRAST = 1
    TEXT_PREVIEW  = 2
    TEXT_KEYWORD  = 3
    TEXT_MUTED    = 4
    TEXT_FUNCTION = 5
    # Element
    MENU_BG        = 6
    BORDER         = 7
    HEADER_BG      = 8
    CATEGORY_BG    = 9
    PANEL_BG       = 10
    SCROLLBAR_BG   = 11
    SCROLLBAR_GRIP = 12
    BTN_ALERT      = 13
    BTN_MAIN       = 14
    # Editor
    EDITOR_BG     = 15
    EDITOR_LINE   = 16
    EDITOR_CURSOR = 17
    # Node
    NODE_WIRE = 18


def get_color(color=COLORS.TEXT_PRIMARY):
    prefs = user_prefs()
    colors = prefs.gui.colors
    if color == COLORS.TEXT_PRIMARY:
        return Vector(colors.text_primary)
    if color == COLORS.TEXT_CONTRAST:
        return Vector(colors.text_contrast)
    if color == COLORS.TEXT_PREVIEW:
        return Vector(colors.text_preview)
    if color == COLORS.TEXT_KEYWORD:
        return Vector(colors.text_keyword)
    if color == COLORS.TEXT_MUTED:
        return Vector(colors.text_muted)
    if color == COLORS.TEXT_FUNCTION:
        return Vector(colors.text_function)
    if color == COLORS.MENU_BG:
        return Vector(colors.menu_bg)
    if color == COLORS.BORDER:
        return Vector(colors.border)
    if color == COLORS.HEADER_BG:
        return Vector(colors.header_bg)
    if color == COLORS.CATEGORY_BG:
        return Vector(colors.category_bg)
    if color == COLORS.PANEL_BG:
        return Vector(colors.panel_bg)
    if color == COLORS.SCROLLBAR_BG:
        return Vector(colors.scrollbar_bg)
    if color == COLORS.SCROLLBAR_GRIP:
        return Vector(colors.scrollbar_grip)
    if color == COLORS.BTN_ALERT:
        return Vector(colors.btn_alert)
    if color == COLORS.BTN_MAIN:
        return Vector(colors.btn_main)
    if color == COLORS.EDITOR_BG:
        return Vector(colors.editor_bg)
    if color == COLORS.EDITOR_LINE:
        return Vector(colors.editor_line)
    if color == COLORS.EDITOR_CURSOR:
        return Vector(colors.editor_cursor)
    if color == COLORS.NODE_WIRE:
        return Vector(colors.node_wire)
    return None
