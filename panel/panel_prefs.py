import bpy


class VIEW3D_MT_MyPrefs(bpy.types.Menu):
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
