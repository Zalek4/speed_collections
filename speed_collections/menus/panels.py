# ------------------------------------------------------------------------
#    Imports
# ------------------------------------------------------------------------
import bpy
from bpy.types import Menu
from bpy.props import StringProperty, IntProperty, BoolProperty, FloatProperty, EnumProperty
from ..operators import op_bake_organizer

# ------------------------------------------------------------------------
#    Classes
# ------------------------------------------------------------------------

class SPEEDSEAMS_PT_MainPanel(bpy.types.Panel):
    bl_label = "Speed Collections"
    bl_idname = "SPEEDSEAMS_PT_mainPanel"
    bl_category = "Speed Collections"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sc = scene.sc_settings

        #Bake Prep Tools ---------------------------------------------------------
        box = layout.box()
        scale = 1.2
        col = box.column(align=True)
        row = col.row(align=True)
        row.scale_y = scale

        # Set up bake groups
        row = col.row(align=True)
        row.label(text="Bake Prep Tools")
        row.scale_y = scale

        row = col.row(align=True)
        row.scale_y = scale
        row.label(text="Asset Name:")
        row.prop(sc, "bakePrepAssetName")
        
        row = col.row(align=True)
        row.scale_y = scale
        row.label(text="Highpoly Suffix:")
        row.prop(sc, "bakePrepSuffixHigh")

        row = col.row(align=True)
        row.scale_y = scale
        row.label(text="Lowpoly Suffix:")
        row.prop(sc, "bakePrepSuffixLow")

        row = col.row(align=True)
        row.scale_y = scale
        row.label(text="Highpoly Collection:")
        row.prop(scene, "sc_collection_high")

        row = col.row(align=True)
        row.scale_y = scale
        row.label(text="Lowpoly Collection:")
        row.prop(scene, "sc_collection_low")
        col.separator()        

        row = col.row(align=True)
        row.scale_y = scale
        row.operator(op_bake_organizer.SPEEDSEAMS_OT_OrganizeHighLowCollections.bl_idname, icon='NEWFOLDER')

        row = col.row(align=True)
        row.scale_y = scale
        row.operator(op_bake_organizer.SPEEDSEAMS_OT_SortHighObjects.bl_idname, icon='PLUS')
        row.operator(op_bake_organizer.SPEEDSEAMS_OT_SortLowObjects.bl_idname, icon='PLUS')
        col.separator()

        row = col.row(align=True)
        row.scale_y = scale
        row.operator(op_bake_organizer.SPEEDSEAMS_OT_PairHighLowObjects.bl_idname, icon='UV_SYNC_SELECT')

        row = col.row(align=True)
        row.scale_y = scale
        #row.prop(ss, "matchAccuracy", slider=True)
        row.prop(sc, "searchDistance", slider=True)

        col.separator()
        row = col.row(align=True)
        row.prop(sc, "renameCollectionsBool")
        row.prop(sc, "renameObjectsBool")

    @classmethod
    def poll(cls, context):
        return context.mode in {'EDIT_MESH', 'OBJECT'}