import bpy
from .op_bake_organizer import SPEEDSEAMS_OT_PairHighLowObjects, SPEEDSEAMS_OT_OrganizeHighLowCollections, SPEEDSEAMS_OT_SortHighObjects, SPEEDSEAMS_OT_SortLowObjects

classes = (SPEEDSEAMS_OT_PairHighLowObjects, SPEEDSEAMS_OT_OrganizeHighLowCollections, SPEEDSEAMS_OT_SortHighObjects, SPEEDSEAMS_OT_SortLowObjects)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)