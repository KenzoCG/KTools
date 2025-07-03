# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import bpy.utils.previews
import os

# ------------------------------------------------------------------------------- #
# CONSTANTS
# ------------------------------------------------------------------------------- #

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PREVIEW_COLLECTIONS = None

# ------------------------------------------------------------------------------- #
# UTILS
# ------------------------------------------------------------------------------- #

def get_directory():
    return os.path.dirname(os.path.abspath(__file__))


def get_icon_names():
    return [os.path.splitext(icon_file)[0] for icon_file in os.listdir(DIRECTORY) if icon_file.lower().endswith(".png")]


def get_icon_id(icon_name=""):
    global PREVIEW_COLLECTIONS
    if isinstance(PREVIEW_COLLECTIONS, bpy.utils.previews.ImagePreviewCollection):
        if icon_name in PREVIEW_COLLECTIONS:
            return PREVIEW_COLLECTIONS[icon_name].icon_id
    return None


def load_icon(icon_name=""):
    global PREVIEW_COLLECTIONS
    if isinstance(PREVIEW_COLLECTIONS, bpy.utils.previews.ImagePreviewCollection):
        if icon_name in PREVIEW_COLLECTIONS:
            return PREVIEW_COLLECTIONS[icon_name]
        else:
            return PREVIEW_COLLECTIONS.load(icon_name, os.path.join(DIRECTORY, icon_name + ".png"), "IMAGE")
    return None

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register_icons():
    unregister_icons()
    global PREVIEW_COLLECTIONS
    icon_names = get_icon_names()
    if icon_names:
        PREVIEW_COLLECTIONS = bpy.utils.previews.new()
        for icon_name in icon_names:
            PREVIEW_COLLECTIONS.load(icon_name, os.path.join(DIRECTORY, icon_name + ".png"), "IMAGE")


def unregister_icons():
    global PREVIEW_COLLECTIONS
    if isinstance(PREVIEW_COLLECTIONS, bpy.utils.previews.ImagePreviewCollection):
        bpy.utils.previews.remove(PREVIEW_COLLECTIONS)
    PREVIEW_COLLECTIONS = None
