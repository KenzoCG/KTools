# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from mathutils import (
    Vector,
    Matrix,
    Quaternion
)
from mathutils.geometry import (
    distance_point_to_plane,
    intersect_line_plane,
    intersect_line_sphere,
    intersect_point_line,
    convex_hull_2d,
    intersect_point_quad_2d
)
from bpy_extras.view3d_utils import (
    region_2d_to_origin_3d,
    region_2d_to_vector_3d,
    location_3d_to_region_2d,
    region_2d_to_location_3d
)
from math import (
    cos, sin, pi, inf, ceil, radians, degrees
)

# ------------------------------------------------------------------------------- #
# RAYS
# ------------------------------------------------------------------------------- #

def mouse_ray(context, event):
    mouse_pos  = Vector((event.mouse_region_x, event.mouse_region_y))
    ray_origin = region_2d_to_origin_3d(context.region, context.region_data, mouse_pos)
    ray_normal = region_2d_to_vector_3d(context.region, context.region_data, mouse_pos)
    ray_end    = ray_origin + (ray_normal * context.space_data.clip_end)
    return mouse_pos, ray_origin, ray_normal, ray_end

# ------------------------------------------------------------------------------- #
# PLANE
# ------------------------------------------------------------------------------- #

def mouse_to_plane(context, event, plane_coord=Vector((0,0,0)), plane_normal=Vector((0,0,1)), fallback=None):
    mouse_pos, ray_origin, ray_normal, ray_end = mouse_ray(context, event)
    hit_point = intersect_line_plane(ray_origin, ray_end, plane_coord, plane_normal)
    return hit_point if isinstance(hit_point, Vector) else fallback


def mouse_to_view_plane(context, event, fallback=None):
    mouse_pos, ray_origin, ray_normal, ray_end = mouse_ray(context, event)
    plane_coord = context.region_data.view_location
    plane_normal = context.region_data.view_rotation @ Vector((0,0,1))
    hit_point = intersect_line_plane(ray_origin, ray_end, plane_coord, plane_normal)
    return hit_point if isinstance(hit_point, Vector) else fallback

# ------------------------------------------------------------------------------- #
# SCENE
# ------------------------------------------------------------------------------- #

# ------------------------------------------------------------------------------- #
# TREE
# ------------------------------------------------------------------------------- #
