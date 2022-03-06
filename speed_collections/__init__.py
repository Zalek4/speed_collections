
import bpy
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from .menus.pies import SPEEDSEAMS_MT_HighLowPie

bl_info = {
    "name": "Speed Collections",
    "author": "Alex Hallenbeck",
    "version": (0, 1, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Speed Collections",
    "description": "",
    "category": "Tools",
    "wiki_url": "",
    "warning": ""
}


class SpeedCollectionsSettings(bpy.types.PropertyGroup):
    
    renameCollectionsBool: bpy.props.BoolProperty(
        name="Rename Collections",
        description="Gives the option to rename the high and low input collections.",
        default=False
    )

    renameObjectsBool: bpy.props.BoolProperty(
        name="Rename Objects",
        description="Gives the option to rename each object pair as bake groups are made.",
        default=False
    )

    bakePrepAssetName: bpy.props.StringProperty(
        name="",
        description="The asset name used to name bake prep collections",
        default=""
        #update=SPEEDSEAMS_OT_OrganizeHighLowCollections.execute
    )

    bakePrepSuffixHigh: bpy.props.StringProperty(
        name="",
        description="The highpoly suffix to use for objects and high/low collections",
        default="high"
    )

    bakePrepSuffixLow: bpy.props.StringProperty(
        name="",
        description="The lowpoly suffix to use for objects and high/low collections",
        default="low"
    )

    searchDistance: bpy.props.FloatProperty(
        name="Search Distance",
        description="Percent of the lowpoly mesh shape that must match the highpoly mesh shape in order to be paired together",
        default=0.3,
        min=0.3,
        max=2.0,
        step=1.00
    )

#-----------------------------------------------------#
#     register the modules
#-----------------------------------------------------#

addon_keymaps = []

def register():
    from .register import register_addon
    register_addon()
    bpy.utils.register_class(SpeedCollectionsSettings)
    bpy.types.Scene.sc_settings = PointerProperty(type=SpeedCollectionsSettings)
    bpy.types.Scene.sc_collection_high = PointerProperty(name="", type=bpy.types.Collection)
    bpy.types.Scene.sc_collection_low = PointerProperty(name="", type=bpy.types.Collection)

    #Register Keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    kmi_high_low_pie = km.keymap_items.new("wm.call_menu_pie", "C", "PRESS", shift=True)
    kmi_high_low_pie.properties.name = SPEEDSEAMS_MT_HighLowPie.bl_idname

    addon_keymaps.append((km, kmi_high_low_pie))

def unregister():
    from .register import unregister_addon
    unregister_addon()
    del bpy.types.Scene.sc_settings
    del bpy.types.Scene.sc_collection_high
    del bpy.types.Scene.sc_collection_low

    #Unregister Keymaps
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi_high_low_pie in addon_keymaps:
            km.keymap_items.remove(kmi_high_low_pie)
    addon_keymaps.clear()
