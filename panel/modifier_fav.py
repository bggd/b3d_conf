import bpy


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
