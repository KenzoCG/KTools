# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy

# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

def user_prefs():
    name = __name__.partition('.')[0]
    return bpy.context.preferences.addons[name].preferences


def name():
    from .. import bl_info
    return bl_info['name']


def name_and_ver():
    from .. import bl_info
    name = bl_info['name']
    version = bl_info['version']
    return f"{name} {version[0]}.{version[1]}.{version[2]}"

def ver_num():
    from .. import bl_info
    version = bl_info['version']
    return version


def ver_str():
    from .. import bl_info
    version = bl_info['version']
    return f"{version[0]}.{version[1]}.{version[2]}"

# ------------------------------------------------------------------------------- #
# CHECKS
# ------------------------------------------------------------------------------- #

def exists(name=""):
    for addon_name in bpy.context.preferences.addons.keys():
        if name in addon_name:
            return True
    return False
