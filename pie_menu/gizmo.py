import bpy

# show_gizmo_object_translate


class VIEW3D_MT_PIE_MyGizmo(bpy.types.Menu):
    bl_label = "My Gizmo"

    def draw(self, context):
        pie = self.layout.menu_pie()

        pie.operator_enum("view3d.transform_gizmo_set", "type")
        pie.prop(context.space_data, "show_gizmo_context", text="Show Gizmo")
        pie.operator("view3d.transform_gizmo_set", text="All").type = {
            "TRANSLATE",
            "ROTATE",
            "SCALE",
        }
