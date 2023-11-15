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


class GRAPH_MT_PIE_MyGraphPie(bpy.types.Menu):
    bl_label = "My Graph Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col = pie.column()
        col.operator("graph.view_selected")
        col.operator("graph.view_all")


from . import panel
from . import pie_menu

classes = (GRAPH_MT_PIE_MyGraphPie,)

addon_keymaps = []


def register():
    panel.register()
    pie_menu.register()

    for cls in classes:
        bpy.utils.register_class(cls)

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
        kmi.properties.name = "VIEW3D_MT_PIE_MyViews"
        addon_keymaps.append((km, kmi))

        # kmi = km.keymap_items.new("wm.call_menu_pie", "SPACE", "PRESS", ctrl=True)
        # kmi.properties.name = "VIEW3D_MT_PIE_MyGizmo"
        # addon_keymaps.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu", "K", "PRESS", ctrl=True)
        kmi.properties.name = "VIEW3D_MT_MyPrefs"
        addon_keymaps.append((km, kmi))

        # km = wm.keyconfigs.addon.keymaps.new(
        #     name="Graph Editor Generic", space_type="GRAPH_EDITOR"
        # )
        # kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS")
        # kmi.properties.name = "GRAPH_MT_PIE_MyGraphPie"
        # addon_keymaps.append((km, kmi))


def unregister():
    panel.unregister()
    pie_menu.unregister()

    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
