import bpy


class VIEW3D_MT_PIE_MyShading(bpy.types.Menu):
    bl_label = "My Shading Pie"

    def draw(self, context):
        layout = self.layout

        overlay = context.space_data.overlay
        shading = context.space_data.shading

        pie = layout.menu_pie()
        pie.prop_enum(shading, "type", "WIREFRAME")
        pie.prop_enum(shading, "type", "SOLID")

        obj = context.active_object
        object_mode = "OBJECT" if obj is None else obj.mode
        has_pose_mode = (object_mode == "POSE") or (
            object_mode == "WEIGHT_PAINT" and context.pose_object is not None
        )
        draw_depressed = False
        if has_pose_mode:
            draw_depressed = overlay.show_xray_bone
        elif context.space_data.shading.type == "WIREFRAME":
            draw_depressed = shading.show_xray_wireframe
        else:
            draw_depressed = shading.show_xray

        pie.operator(
            "view3d.toggle_xray",
            icon="XRAY",
            depress=draw_depressed,
        )

        pie.prop(overlay, "show_overlays")


class VIEW3D_MT_PIE_MyShading2(bpy.types.Menu):
    bl_label = "Shading and Engine"

    def draw(self, context):
        render = context.scene.render
        shading = context.space_data.shading
        overlay = context.space_data.overlay

        layout = self.layout
        pie = layout.menu_pie()
        col = pie.column()
        col.props_enum(shading, "type")
        col.popover(panel="VIEW3D_PT_shading")

        col = pie.column()
        col.props_enum(render, "engine")

        row = pie.row(align=True)
        row.prop(overlay, "show_edge_crease", text="Creases")
        row.prop(
            overlay,
            "show_edge_sharp",
            text="Sharp",
        )
        row.prop(overlay, "show_edge_bevel_weight", text="Bevel")
        row.prop(overlay, "show_edge_seams", text="Seams")
