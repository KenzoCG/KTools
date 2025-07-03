# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import os
from pathlib import Path

# ------------------------------------------------------------------------------- #
# UTILS
# ------------------------------------------------------------------------------- #

def blend_file_path(file_name=""):
    blends_dir = Path(__file__).parent.resolve()
    blend_file = blends_dir.joinpath(file_name)
    if blend_file.exists():
        return str(blend_file)
    return None
