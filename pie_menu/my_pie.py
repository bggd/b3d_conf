import bpy


class VIEW3D_MT_PIE_MyPie(bpy.types.Menu):
    bl_label = "My Pie"

    def draw_edit(self, context):
        tool_settings = context.tool_settings

        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column(align=True)
        col.separator(factor=4.0)
        row = col.row(align=True)
        row.operator("mesh.bevel", text="Bevel 1.0").profile = 1.0
        row.operator("mesh.bevel", text="0.7").profile = 0.7
        row.operator("mesh.bevel", text="0.5").profile = 0.5
        row = col.row(align=True)
        row.operator("mesh.bevel", text="Bevel 0.0").profile = 0.0
        row.operator("mesh.bevel", text="0.125").profile = 0.125

        row = pie.row()
        row.scale_x = 1.25
        row.scale_y = 1.25
        row.template_header_3D_mode()
        row.popover(panel="VIEW3D_PT_snapping", text="Snap To")

        col = pie.column(align=True)
        col.operator("mesh.loopcut")
        col.operator(
            "mesh.offset_edge_loops_slide"
        ).TRANSFORM_OT_edge_slide.use_even = True
        col.separator()
        col.operator("mesh.mark_seam")
        col.operator("mesh.mark_seam", text="Clear Seam").clear = True

        col = pie.column(align=True)
        col.operator("transform.edge_bevelweight")
        col.operator("transform.edge_crease")

        col = pie.box().column(align=True)
        col.label(text="Extrude")
        col.operator("view3d.edit_mesh_extrude_move_normal", text="Faces")
        col.operator(
            "view3d.edit_mesh_extrude_move_shrink_fatten",
            text="Faces Along Normals",
        )
        col.operator("mesh.extrude_faces_move", text="Individual Faces")
        col.operator("view3d.edit_mesh_extrude_manifold_normal", text="Manifold")
        extrude = col.operator(
            "mesh.extrude_region_shrink_fatten", text="Region And Shrink/Flatten"
        )
        extrude.MESH_OT_extrude_region.use_dissolve_ortho_edges = True
        extrude.TRANSFORM_OT_shrink_fatten.use_even_offset = True

        col = pie.grid_flow(row_major=True, columns=2, align=True)
        col.prop(tool_settings, "use_mesh_automerge")
        col.operator("mesh.merge", text="Merge At Center").type = "CENTER"
        merge = col.operator("mesh.remove_doubles")
        merge.threshold = 0.0005
        merge.use_unselected = True
        col.operator("mesh.merge", text="Merge At Cursor").type = "CURSOR"
        col.operator("mesh.dissolve_mode")
        col.operator("mesh.merge", text="Collapse").type = "COLLAPSE"

        row = pie.row()
        col = row.column(align=True)
        col.separator(factor=4.0)
        col.operator("mesh.poke")
        col.operator("mesh.tris_convert_to_quads")
        col = row.column(align=True)
        col.separator(factor=4.0)
        col.operator("mesh.inset")
        col.operator("mesh.inset", text="Inset Individual").use_individual = True
        col.separator()
        col.operator("mesh.vert_connect_path")
        col.operator("hops.star_connect")

        col = pie.column(align=True)
        knife = col.operator("mesh.knife_tool", text="Knife")
        knife.use_occlude_geometry = True
        knife.angle_snapping = "NONE"
        knife_angle = col.operator("mesh.knife_tool", text="Angle Constraint")
        knife_angle.use_occlude_geometry = True
        knife_angle.angle_snapping = "SCREEN"
        cut_through = col.operator("mesh.knife_tool", text="Cut Through")
        cut_through.use_occlude_geometry = False
        cut_through.angle_snapping = "NONE"
        cut_through_angle = col.operator("mesh.knife_tool", text="Cut Angle Cnst")
        cut_through_angle.use_occlude_geometry = False
        cut_through_angle.angle_snapping = "SCREEN"
        col.operator("mesh.bisect")

    def draw_default(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column(align=True)
        col.operator("view3d.localview").frame_selected = False
        col.operator("view3d.view_selected")
        col.operator("view3d.view_all")

        pie.template_header_3D_mode()

        col = pie.column(align=True)
        col.prop(context.object, "display_type")
        col.prop(context.object, "show_in_front")

        col = pie.column(align=True)
        col.operator("view3d.render_border")
        col.operator("view3d.clear_render_border")

    def draw(self, context):
        if context.mode == "EDIT_MESH":
            self.draw_edit(context)
        else:
            self.draw_default(context)
