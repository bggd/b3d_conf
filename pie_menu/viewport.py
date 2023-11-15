import bpy


class VIEW3D_MT_PIE_MyViewportsettings(bpy.types.Menu):
    bl_label = "My Viewport Settings"

    def draw(self, context):
        view = context.space_data
        obj = context.object
        overlay = context.space_data.overlay
        shading = context.space_data.shading
        render = context.scene.render

        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.prop(overlay, "show_face_orientation")
        col.prop(overlay, "show_wireframes")
        col.prop(shading, "show_cavity")

        col = pie.column(align=True)
        col.prop(obj, "display_type", expand=True)

        pie.menu_contents("VIEW3D_MT_PIE_MyShading2")
