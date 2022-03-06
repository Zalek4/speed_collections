# ------------------------------------------------------------------------
#    Imports
# ------------------------------------------------------------------------
import bpy
from bpy.types import Menu
from bpy.props import StringProperty, IntProperty, BoolProperty, FloatProperty, EnumProperty
from ..operators import op_bake_organizer


class SPEEDCOLLECTIONS_MT_HighLowPie(Menu):
    bl_label = "Sort High/Low"
    bl_idname = "SPEEDSEAMS_MT_HighLowPie"
    bl_category = "Speed Seams"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator(
            op_bake_organizer.SPEEDCOLLECTIONS_OT_SortHighObjects.bl_idname, icon='PLUS')
        pie.operator(
            op_bake_organizer.SPEEDCOLLECTIONS_OT_SortLowObjects.bl_idname, icon='PLUS')
