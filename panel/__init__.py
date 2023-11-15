import bpy

from .panel_prefs import *
from .modifier_fav import *

classes = (
    VIEW3D_MT_MyPrefs,
    AddSubD,
    AddRemesh,
    AddSmoothCorrective,
    AddDecimate,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.DATA_PT_modifiers.prepend(modifiers_fav)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.DATA_PT_modifiers.remove(modifiers_fav)
