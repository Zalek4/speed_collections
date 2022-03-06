import bpy
from .addon import SpeedCollectionsProps

classes = (

)

def register_properties():
    from bpy.utils import register_class
    bpy.utils.register_class(SpeedCollectionsProps)
    #for cls in classes:
        #register_class(cls)


def unregister_properties():
    from bpy.utils import unregister_class
    bpy.utils.unregister_class(SpeedCollectionsProps)
    #for cls in reversed(classes):
        #unregister_class(cls)
