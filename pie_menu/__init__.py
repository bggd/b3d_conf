import bpy

from .my_pie import *
from .views import *
from .shading import *
from .viewport import *
from .gizmo import *

classes = (
    VIEW3D_MT_PIE_MyPie,
    VIEW3D_OT_MyQuadView,
    VIEW3D_MT_PIE_MyViews,
    VIEW3D_MT_PIE_MyShading,
    VIEW3D_MT_PIE_MyShading2,
    VIEW3D_MT_PIE_MyViewportsettings,
    VIEW3D_MT_PIE_MyGizmo,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
