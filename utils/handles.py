# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import traceback
from bpy.types import SpaceView3D
from bpy.app.handlers import persistent

# ------------------------------------------------------------------------------- #
# SHADERS
# ------------------------------------------------------------------------------- #

SHADER_HANDLES = []

class ShaderHandler:
    def __init__(self):
        self.__user_callback_2d = None
        self.__user_callback_3d = None
        self.__handle_2d = None
        self.__handle_3d = None


    def register(self, context=None, callback_2d=None, callback_3d=None):
        # 2D - Post Pixel
        if callback_2d is not None and callable(callback_2d):
            self.__user_callback_2d = callback_2d
            self.__handle_2d = SpaceView3D.draw_handler_add(self.__draw_2d_callback, (context,), 'WINDOW', 'POST_PIXEL')
            if self.__handle_2d:
                SHADER_HANDLES.append(self.__handle_2d)
        # 3D - Post View
        if callback_3d is not None and callable(callback_3d):
            self.__user_callback_3d = callback_3d
            self.__handle_3d = SpaceView3D.draw_handler_add(self.__draw_3d_callback, (context,), 'WINDOW', 'POST_VIEW')
            if self.__handle_3d:
                SHADER_HANDLES.append(self.__handle_3d)


    def unregister(self):
        # Global
        if self.__handle_2d in SHADER_HANDLES:
            SHADER_HANDLES.remove(self.__handle_2d)
        if self.__handle_3d in SHADER_HANDLES:
            SHADER_HANDLES.remove(self.__handle_3d)
        # B3D Internal
        if self.__handle_2d:
            try: SpaceView3D.draw_handler_remove(self.__handle_2d, "WINDOW")
            except Exception as e: traceback.print_exc()
        if self.__handle_3d:
            try: SpaceView3D.draw_handler_remove(self.__handle_3d, "WINDOW")
            except Exception as e: traceback.print_exc()
        # Refs
        self.__user_callback_2d = None
        self.__user_callback_3d = None
        self.__handle_2d = None
        self.__handle_3d = None


    def __draw_2d_callback(self, context):
        if self.__user_callback_2d is not None and callable(self.__user_callback_2d):
            try:
                self.__user_callback_2d(context)
            except Exception as e:
                print("Shader Handle 2D : Failed")
                self.__user_callback_2d = None
                traceback.print_exc()
                return False
        return True


    def __draw_3d_callback(self, context):
        if self.__user_callback_3d is not None and callable(self.__user_callback_3d):
            try:
                self.__user_callback_3d(context)
            except Exception as e:
                print("Shader Handle 3D : Failed")
                self.__user_callback_3d = None
                traceback.print_exc()
                return False
        return True


@persistent
def remove_shader_handles(null=''):
    global SHADER_HANDLES
    for handle in SHADER_HANDLES:
        try: SpaceView3D.draw_handler_remove(handle, "WINDOW")
        except Exception as e: traceback.print_exc()
    SHADER_HANDLES = []
