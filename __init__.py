bl_info = {
    "name": "b3d_conf",
    "author": "birthggd",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "My Configuration for Blender",
    "warning": "",
    "wiki_url": "",
    "category": "General",
}


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


class VIEW3D_OT_MyQuadView(bpy.types.Operator):
    bl_idname = "myconf.quadview"
    bl_label = "Toggle QuadView"

    def execute(self, context):
        bpy.ops.screen.region_quadview()
        if len(context.space_data.region_quadviews) > 1:
            context.space_data.region_quadviews[2].show_sync_view = True
        return {"FINISHED"}


class VIEW3D_MT_PIE_MyView(bpy.types.Menu):
    bl_label = "My View Pie"

    def draw(self, context):
        view = context.space_data

        layout = self.layout

        pie = layout.menu_pie()

        grid = pie.grid_flow(row_major=True, columns=2)
        grid.operator("view3d.view_axis", text="FRONT").type = "FRONT"
        grid.operator("view3d.view_axis", text="BACK").type = "BACK"
        grid.operator("view3d.view_axis", text="LEFT").type = "LEFT"
        grid.operator("view3d.view_axis", text="RIGHT").type = "RIGHT"
        grid.operator("view3d.view_axis", text="TOP").type = "TOP"
        grid.operator("view3d.view_axis", text="BOTTOM").type = "BOTTOM"

        pie.operator("view3d.view_persportho", text="Persp / Ortho")

        row = pie.row(align=True)
        row.prop(view, "show_gizmo", text="Show Gizmos", icon="GIZMO")
        row.operator("view3d.transform_gizmo_set", text="All").type = {
            "TRANSLATE",
            "ROTATE",
            "SCALE",
        }
        row.operator("view3d.transform_gizmo_set", text="Move").type = {"TRANSLATE"}
        row.operator("view3d.transform_gizmo_set", text="Rotate").type = {"ROTATE"}
        row.operator("view3d.transform_gizmo_set", text="Scale").type = {"SCALE"}

        pie.operator("myconf.quadview")


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


class VIEW3D_MT_PIE_MyQuickFav(bpy.types.Menu):
    bl_label = "My Prefs"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.separator()
        col.prop(
            context.window_manager.keyconfigs["Blender"].preferences,
            "select_mouse",
            text="",
        )
        col.prop(context.preferences.inputs, "use_mouse_emulate_3_button")
        col.prop(context.preferences.inputs, "view_zoom_axis", text="")
        col.prop(context.preferences.filepaths, "use_auto_save_temporary_files")


class GRAPH_MT_PIE_MyGraphPie(bpy.types.Menu):
    bl_label = "My Graph Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.operator("graph.view_selected")
        col.operator("graph.view_all")


class AddSubD(bpy.types.Operator):
    bl_idname = "b3d_conf.add_subd"
    bl_label = "Add SubD"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object

        m = obj.modifiers.new("Subdivision", "SUBSURF")
        m.levels = 0
        m.show_viewport = False

        return {"FINISHED"}


class AddRemesh(bpy.types.Operator):
    bl_idname = "b3d_conf.add_remesh"
    bl_label = "Add Remesh"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object

        m = obj.modifiers.new("Remesh", "REMESH")
        m.voxel_size = 0.01
        m.use_smooth_shade = True
        m.show_viewport = False

        return {"FINISHED"}


class AddSmoothCorrective(bpy.types.Operator):
    bl_idname = "b3d_conf.add_smooth_corrective"
    bl_label = "Add SmoothCorrective"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object

        m = obj.modifiers.new("Smooth Corrective", "CORRECTIVE_SMOOTH")
        m.iterations = 16
        m.use_only_smooth = True
        m.smooth_type = "LENGTH_WEIGHTED"
        m.show_viewport = False

        return {"FINISHED"}


class AddDecimate(bpy.types.Operator):
    bl_idname = "b3d_conf.add_decimate"
    bl_label = "Add Decimate"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object

        m = obj.modifiers.new("Decimate", "DECIMATE")
        m.ratio = 0.1
        m.show_viewport = False

        return {"FINISHED"}


def modifiers_fav(self, context):
    layout = self.layout
    grid = layout.grid_flow(row_major=True, columns=2, align=True)
    grid.operator("b3d_conf.add_subd", text="SubD", icon="MOD_SUBSURF")
    grid.operator("b3d_conf.add_remesh", text="Remesh", icon="MOD_REMESH")
    grid.operator(
        "b3d_conf.add_smooth_corrective", text="SmoothCorrective", icon="MOD_SMOOTH"
    )
    grid.operator("b3d_conf.add_decimate", text="Decimate", icon="MOD_DECIM")


classes = (
    VIEW3D_OT_MyQuadView,
    VIEW3D_MT_PIE_MyShading,
    VIEW3D_MT_PIE_MyShading2,
    VIEW3D_MT_PIE_MyView,
    VIEW3D_MT_PIE_MyViewportsettings,
    VIEW3D_MT_PIE_MyQuickFav,
    VIEW3D_MT_PIE_MyPie,
    GRAPH_MT_PIE_MyGraphPie,
    AddSubD,
    AddRemesh,
    AddSmoothCorrective,
    AddDecimate,
)

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.DATA_PT_modifiers.prepend(modifiers_fav)

    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(
            name="3D View Generic", space_type="VIEW_3D"
        )
        kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS")
        kmi.properties.name = "VIEW3D_MT_PIE_MyPie"
        addon_keymaps.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu_pie", "Z", "PRESS")
        kmi.properties.name = "VIEW3D_MT_PIE_MyShading"
        addon_keymaps.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu_pie", "Z", "PRESS", alt=True)
        kmi.properties.name = "VIEW3D_MT_PIE_MyViewportsettings"
        addon_keymaps.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu_pie", "ACCENT_GRAVE", "PRESS")
        kmi.properties.name = "VIEW3D_MT_PIE_MyView"
        addon_keymaps.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu", "K", "PRESS", ctrl=True)
        kmi.properties.name = "VIEW3D_MT_PIE_MyQuickFav"
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(
            name="Graph Editor Generic", space_type="GRAPH_EDITOR"
        )
        kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS")
        kmi.properties.name = "GRAPH_MT_PIE_MyGraphPie"
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.DATA_PT_modifiers.remove(modifiers_fav)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
