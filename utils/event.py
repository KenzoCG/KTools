# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from mathutils import Vector
from .screen import ui_scale

# ------------------------------------------------------------------------------- #
# MODAL
# ------------------------------------------------------------------------------- #

class Events:
    def __init__(self):
        self.CONFIRM   = {'SPACE', 'LEFTMOUSE', 'RET', 'NUMPAD_ENTER'}
        self.CANCEL    = {'ESC', 'RIGHTMOUSE'}
        self.CLICK     = {'LEFTMOUSE'}
        self.MOUSE     = {'MOUSEMOVE', 'TRACKPADPAN'}
        self.INCREMENT = {'WHEELUPMOUSE', 'NUMPAD_PLUS', 'EQUAL', 'UP_ARROW'}
        self.DECREMENT = {'WHEELDOWNMOUSE', 'NUMPAD_MINUS', 'MINUS', 'DOWN_ARROW'}
        self.NUMPAD    = {'NUMPAD_PERIOD', 'NUMPAD_0', 'NUMPAD_1', 'NUMPAD_2', 'NUMPAD_3', 'NUMPAD_4', 'NUMPAD_5', 'NUMPAD_6', 'NUMPAD_7', 'NUMPAD_8', 'NUMPAD_9'}
        self.MOUSE     = {'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'MIDDLEMOUSE'}
        self.PASS      = {'NUMPAD_PERIOD', 'NUMPAD_0', 'NUMPAD_1', 'NUMPAD_2', 'NUMPAD_3', 'NUMPAD_4', 'NUMPAD_5', 'NUMPAD_6', 'NUMPAD_7', 'NUMPAD_8', 'NUMPAD_9', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'MIDDLEMOUSE'}
        self.MODS      = {'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT'}
        self.DRAG      = {'RIGHTMOUSE', 'LEFTMOUSE'}


class Controls:
    def __init__(self, events=None):
        self.events = events if isinstance(events, Events) else Events()
        self.key = ''
        self.pressed = False
        self.released = False
        self.confirmed = False
        self.cancelled = False
        self.pass_through = False
        self.increment = 0
        self.mouse_pos = Vector((0,0))
        self.mouse_fac = 0
        self.mouse_scroll = 0
        self.mouse_click_down = False
        self.mouse_click_up = False
        self.mouse_drag = False
        self.__ui_scale = ui_scale()
        self.__mouse_drag_down_pos = None
        self.__mouse_drag_threshold = round(4 * self.__ui_scale)


    def update(self, context, event):
        # Keys
        self.key = event.type
        self.pressed = event.value == 'PRESS'
        self.released = event.value == 'RELEASE'
        # Confirm
        self.confirmed = False
        if self.key in self.events.CONFIRM and self.pressed:
            self.confirmed = True
        # Cancel
        self.cancelled = False
        if self.key in self.events.CANCEL and self.pressed:
            self.cancelled = True
        # Passthrough
        self.pass_through = False
        if self.pressed:
            if self.key in self.events.PASS:
                self.pass_through = True
            elif event.shift and self.key == 'Z':
                self.pass_through = True
        # Increment
        self.increment = 0
        if self.key in self.events.INCREMENT:
            self.increment = 1
        elif self.key in self.events.DECREMENT:
            self.increment = -1
        # Mouse Position
        self.mouse_pos.x = event.mouse_region_x
        self.mouse_pos.y = event.mouse_region_y
        # Mouse Factor
        delta_x = 0
        delta_y = 0
        if self.key in self.events.MOUSE:
            delta_x = (event.mouse_x - event.mouse_prev_x) * self.__ui_scale
            delta_y = (event.mouse_y - event.mouse_prev_y) * self.__ui_scale
            if event.shift:
                delta_x *= .25
                delta_y *= .25
        self.mouse_fac = Vector((delta_x, delta_y)).length
        # Mouse Scroll
        self.mouse_scroll = 0
        if self.key == 'WHEELUPMOUSE':
            self.mouse_scroll = 1
        elif self.key == 'WHEELDOWNMOUSE':
            self.mouse_scroll = -1
        # Mouse Clicks
        self.mouse_click_down = False
        self.mouse_click_up = False
        if self.key in self.events.CLICK:
            if self.pressed:
                self.mouse_click_down = True
            elif self.released:
                self.mouse_click_up = True
        # Mouse Drag
        if self.key in self.events.DRAG:
            if self.pressed:
                self.__mouse_drag_down_pos = self.mouse_pos.copy()
            elif self.released:
                self.__mouse_drag_down_pos = None
                self.mouse_drag = False
        if isinstance(self.__mouse_drag_down_pos, Vector):
            if (self.__mouse_drag_down_pos - self.mouse_pos).length >= self.__mouse_drag_threshold:
                self.mouse_drag = True
