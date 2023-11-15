import bpy


class VIEW3D_OT_MyQuadView(bpy.types.Operator):
    bl_idname = "myconf.quadview"
    bl_label = "Toggle QuadView"

    def execute(self, context):
        bpy.ops.screen.region_quadview()
        if len(context.space_data.region_quadviews) > 1:
            context.space_data.region_quadviews[2].show_sync_view = True
        return {"FINISHED"}


class VIEW3D_MT_PIE_MyViews(bpy.types.Menu):
    bl_label = "My Views Pie"

    def draw(self, context):
        view = context.space_data

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("view3d.view_axis", text="LEFT").type = "LEFT"
        pie.operator("view3d.view_axis", text="RIGHT").type = "RIGHT"
        pie.operator("view3d.view_axis", text="BOTTOM").type = "BOTTOM"
        pie.operator("view3d.view_axis", text="TOP").type = "TOP"
        pie.operator("view3d.view_axis", text="BACK").type = "BACK"
        pie.operator("view3d.view_axis", text="FRONT").type = "FRONT"

        pie.operator("myconf.quadview", icon="SNAP_VERTEX")
        pie.operator(
            "view3d.view_persportho", text="Persp / Ortho", icon="ARROW_LEFTRIGHT"
        )
