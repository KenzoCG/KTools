# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
# ------------------------------------------------------------------------------- #
# UTILS
# ------------------------------------------------------------------------------- #

def ui_scale():
    return bpy.context.preferences.system.ui_scale

# ------------------------------------------------------------------------------- #
# CLASSES
# ------------------------------------------------------------------------------- #

class RegionUI_Controller:
    def __init__(self, context):
        self.context = context
        self.header        = None
        self.tool_settings = None
        self.toolbar       = None
        self.sidebar       = None
        self.last_op       = None
        self.asset_shelf   = None
        self.gizmos        = None
        self.tool_gizmo    = None

        if hasattr(context, 'space_data'):
            space_data = context.space_data
            if hasattr(space_data, 'show_region_header'):
                self.header = bool(space_data.show_region_header)
            if hasattr(space_data, 'show_region_tool_header'):
                self.tool_settings = bool(space_data.show_region_tool_header)
            if hasattr(space_data, 'show_region_toolbar'):
                self.toolbar = bool(space_data.show_region_toolbar)
            if hasattr(space_data, 'show_region_ui'):
                self.sidebar = bool(space_data.show_region_ui)
            if hasattr(space_data, 'show_region_hud'):
                self.last_op = bool(space_data.show_region_hud)
            if hasattr(space_data, 'show_region_asset_shelf'):
                self.asset_shelf = bool(space_data.show_region_asset_shelf)
            if hasattr(space_data, 'show_gizmo'):
                self.gizmos = bool(space_data.show_gizmo)
            if hasattr(space_data, 'show_gizmo_tool'):
                self.tool_gizmo = bool(space_data.show_gizmo_tool)


    def restore(self):
        if hasattr(self.context, 'space_data'):
            space_data = self.context.space_data
            if hasattr(space_data, 'show_region_header'):
                if self.header is not None:
                    space_data.show_region_header = self.header
            if hasattr(space_data, 'show_region_tool_header'):
                if self.tool_settings is not None:
                    space_data.show_region_tool_header = self.tool_settings
            if hasattr(space_data, 'show_region_toolbar'):
                if self.toolbar is not None:
                    space_data.show_region_toolbar = self.toolbar
            if hasattr(space_data, 'show_region_ui'):
                if self.sidebar is not None:
                    space_data.show_region_ui = self.sidebar
            if hasattr(space_data, 'show_region_hud'):
                if self.last_op is not None:
                    space_data.show_region_hud = self.last_op
            if hasattr(space_data, 'show_region_asset_shelf'):
                if self.asset_shelf is not None:
                    space_data.show_region_asset_shelf = self.asset_shelf
            if hasattr(space_data, 'show_gizmo'):
                if self.gizmos is not None:
                    space_data.show_gizmo = self.gizmos
            if hasattr(space_data, 'show_gizmo_tool'):
                if self.tool_gizmo is not None:
                    space_data.show_gizmo_tool = self.tool_gizmo


    def hide(self, header=False, tool_settings=False, toolbar=False, sidebar=False, last_op=False, asset_shelf=False, gizmos=False, tool_gizmo=False):
        if hasattr(self.context, 'space_data'):
            space_data = self.context.space_data
            if header:
                if hasattr(space_data, 'show_region_header'):
                    if space_data.show_region_header:
                        space_data.show_region_header = False
            if tool_settings:
                if hasattr(space_data, 'show_region_tool_header'):
                    if space_data.show_region_tool_header:
                        space_data.show_region_tool_header = False
            if toolbar:
                if hasattr(space_data, 'show_region_toolbar'):
                    if space_data.show_region_toolbar:
                        space_data.show_region_toolbar = False
            if sidebar:
                if hasattr(space_data, 'show_region_ui'):
                    if space_data.show_region_ui:
                        space_data.show_region_ui = False
            if last_op:
                if hasattr(space_data, 'show_region_hud'):
                    if space_data.show_region_hud:
                        space_data.show_region_hud = False
            if asset_shelf:
                if hasattr(space_data, 'show_region_asset_shelf'):
                    if space_data.show_region_asset_shelf:
                        space_data.show_region_asset_shelf = False
            if gizmos:
                if hasattr(space_data, 'show_gizmo'):
                    if space_data.show_gizmo:
                        space_data.show_gizmo = False
            if tool_gizmo:
                if hasattr(space_data, 'show_gizmo_tool'):
                    if space_data.show_gizmo_tool:
                        space_data.show_gizmo_tool = False


class ScreenDimensions:
    def __init__(self, context):
        area = context.area
        self.w  = area.width
        self.h  = area.height
        self.lx = area.x
        self.rx = area.x + area.width
        self.by = area.y
        self.ty = area.y + area.height
        self.cx = int((area.x + area.width) / 2)
        self.cy = int((area.y + area.height) / 2)
        self.scale = ui_scale()
