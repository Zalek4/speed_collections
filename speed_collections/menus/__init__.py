import bpy
from .panels import SPEEDCOLLECTIONS_PT_MainPanel
from .pies import SPEEDCOLLECTIONS_MT_HighLowPie

classes = (SPEEDCOLLECTIONS_PT_MainPanel, SPEEDCOLLECTIONS_MT_HighLowPie)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
