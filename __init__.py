# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

bl_info = {
    "name": "KTools",
    "description": "Various operations",
    "author": "KenzoCG",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "View3D",
    "category": "3D View"}

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    from .resources.icon import register_icons
    register_icons()

    from . import utils
    utils.register()

    from . import props
    props.register()

    from . import ops
    ops.register()

    from . import interface
    interface.register()


def unregister():
    from . import interface
    interface.unregister()

    from . import ops
    ops.unregister()

    from . import props
    props.unregister()

    from . import utils
    utils.unregister()

    from .resources.icon import unregister_icons
    unregister_icons()

