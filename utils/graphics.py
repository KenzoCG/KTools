# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import blf
import gpu
from gpu import state
from gpu_extras.batch import batch_for_shader
from mathutils import (
    Vector,
    Matrix,
    Quaternion
)
from math import (
    cos, sin, pi, inf, ceil, radians, degrees
)
from .screen import ui_scale

# ------------------------------------------------------------------------------- #
# CONSTANTS
# ------------------------------------------------------------------------------- #

UNIFORM_COLOR = gpu.shader.from_builtin('UNIFORM_COLOR')
SMOOTH_COLOR = gpu.shader.from_builtin('SMOOTH_COLOR')

class COLORS:
    WHITE  = Vector((1.0, 1.0, 1.0, 1.0))
    BLACK  = Vector((0.0, 0.0, 0.0, 1.0))
    GREY   = Vector((0.5, 0.5, 0.5, 1.0))
    RED    = Vector((1.0, 0.0, 0.0, 1.0))
    GREEN  = Vector((0.0, 1.0, 0.0, 1.0))
    BLUE   = Vector((0.0, 0.0, 1.0, 1.0))
    CYAN   = Vector((0.0, 1.0, 1.0, 1.0))
    YELLOW = Vector((1.0, 1.0, 0.0, 1.0))
    ORANGE = Vector((1.0, 0.2, 0.0, 1.0))
    PURPLE = Vector((1.0, 0.0, 1.0, 1.0))

class BLENDING_MODES:
    NONE             = 'NONE'             # No blending
    ALPHA            = 'ALPHA'            # The original color channels are interpolated according to the alpha value
    ALPHA_PREMULT    = 'ALPHA_PREMULT'    # The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value
    ADDITIVE         = 'ADDITIVE'         # The original color channels are added by the corresponding ones
    ADDITIVE_PREMULT = 'ADDITIVE_PREMULT' # The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value
    MULTIPLY         = 'MULTIPLY'         # The original color channels are multiplied by the corresponding ones
    SUBTRACT         = 'SUBTRACT'         # The original color channels are subtracted by the corresponding ones
    INVERT           = 'INVERT'           # The original color channels are replaced by its complementary color

class DEPTH_TEST:
    NONE          = 'NONE'           # No depth testing
    ALWAYS        = 'ALWAYS'         # The depth test always passes, regardless of existing depth
    LESS          = 'LESS'           # Passes if new depth is less than the existing depth
    LESS_EQUAL    = 'LESS_EQUAL'     # Passes if new depth is less than or equal to the existing depth
    EQUAL         = 'EQUAL'          # Passes if new depth is equal to the existing depth
    GREATER       = 'GREATER'        # Passes if new depth is greater than the existing depth
    GREATER_EQUAL = 'GREATER_EQUAL'  # Passes if new depth is greater than or equal to the existing depth

# ------------------------------------------------------------------------------- #
# STATE
# ------------------------------------------------------------------------------- #

def set_blending_mode(mode=BLENDING_MODES.NONE):
    state.blend_set(mode)


def set_depth_test(test=DEPTH_TEST.NONE):
    if test == DEPTH_TEST.NONE:
        state.depth_test_set(DEPTH_TEST.NONE)
        state.depth_mask_set(False)
    else:
        state.depth_test_set(test)
        state.depth_mask_set(True)


def set_scissor_test(on=False, x_pos=0, y_pos=0, x_size=0, y_size=0):
    if on:
        state.scissor_set(x_pos, y_pos, x_size, y_size)
        state.scissor_test_set(True)
    else:
        state.scissor_set(0, 0, 0, 0)
        state.scissor_test_set(False)


def set_point_size(size=0):
    state.point_size_set(size)


def set_line_width(width=0):
    state.line_width_set(width)

# ------------------------------------------------------------------------------- #
# BATCHES
# ------------------------------------------------------------------------------- #

def gen_points_batch(points=[]):
    return batch_for_shader(UNIFORM_COLOR, 'POINTS', {"pos": points})


def gen_line_batch(lines=[]):
    return batch_for_shader(UNIFORM_COLOR, 'LINES', {"pos": lines})


def gen_tri_batch(tris=[]):
    return batch_for_shader(UNIFORM_COLOR, 'TRIS', {"pos": [v for tri in tris for v in tri]}, indices=[(i, i+1, i+2) for i in range(0, len(tris), 3)])


def draw_uniform_batch(batch, color=(0,0,0,1)):
    UNIFORM_COLOR.uniform_float("color", color)
    batch.draw(UNIFORM_COLOR)

# ------------------------------------------------------------------------------- #
# SHAPES
# ------------------------------------------------------------------------------- #

def draw_circle_2d(radius=12, res=32, center=Vector((0,0)), color=(0,0,0,1)):
    step = (pi * 2) / res
    points = [ Vector((cos(step * i), sin(step * i))) * radius + center for i in range(res + 1)]
    batch = batch_for_shader(UNIFORM_COLOR, 'LINE_STRIP', {"pos": points})
    UNIFORM_COLOR.uniform_float("color", color)
    batch.draw(UNIFORM_COLOR)

# ------------------------------------------------------------------------------- #
# TEXT
# ------------------------------------------------------------------------------- #

def text_word_wrap_set(on=True, width=100):
    if on:
        blf.word_wrap(0, width)
        blf.enable(0, blf.WORD_WRAP)
    else:
        blf.disable(0, blf.WORD_WRAP)
        blf.word_wrap(0, 0)


def text_dims(text="", size=12):
    blf.size(0, size)
    scale = ui_scale()
    text_w, text_h = blf.dimensions(0, text)
    return round(text_w * scale), round(text_h * scale)


def text_heights(size=12):
    blf.size(0, size)
    scale = ui_scale()
    text_h = round(blf.dimensions(0, "Klgjy`")[1] * scale)
    text_d = round(text_h / 4)
    return text_h, text_d


def draw_text(text="", x=0, y=0, size=12, color=(1,1,1,1)):
    blf.position(0, x, y, 0)
    blf.size(0, size)
    blf.color(0, *color)
    blf.draw(0, text)
