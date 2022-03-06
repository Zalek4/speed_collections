import bpy
from .op_bake_organizer import SPEEDCOLLECTIONS_OT_PairHighLowObjects, SPEEDCOLLECTIONS_OT_OrganizeHighLowCollections, SPEEDCOLLECTIONS_OT_SortHighObjects, SPEEDCOLLECTIONS_OT_SortLowObjects

classes = (SPEEDCOLLECTIONS_OT_PairHighLowObjects, SPEEDCOLLECTIONS_OT_OrganizeHighLowCollections,
           SPEEDCOLLECTIONS_OT_SortHighObjects, SPEEDCOLLECTIONS_OT_SortLowObjects)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)