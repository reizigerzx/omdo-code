# bpy.context

The context members available depend on the area of Blender which is currently being accessed.

Note that all context values are readonly, but may be modified through the data API or by running operators

## Global Context
bpy.context.area : bpy.types.Area, 
bpy.context.blend_data : bpy.types.BlendData, 
bpy.context.collection : bpy.types.Collection, 
bpy.context.engine : string, default “”
bpy.context.gizmo_group : bpy.types.GizmoGroup, 
bpy.context.layer_collection : bpy.types.LayerCollection, 
bpy.context.mode : enum in [‘EDIT_MESH’, ‘EDIT_CURVE’, ‘EDIT_SURFACE’, ‘EDIT_TEXT’, ‘EDIT_ARMATURE’, ‘EDIT_METABALL’, ‘EDIT_LATTICE’, ‘POSE’, ‘SCULPT’, ‘PAINT_WEIGHT’, ‘PAINT_VERTEX’, ‘PAINT_TEXTURE’, ‘PARTICLE’, ‘OBJECT’, ‘PAINT_GPENCIL’, ‘EDIT_GPENCIL’, ‘SCULPT_GPENCIL’, ‘WEIGHT_GPENCIL’, ‘VERTEX_GPENCIL’], default ‘EDIT_MESH’, 
bpy.context.preferences : bpy.types.Preferences, 
bpy.context.region : bpy.types.Region, 
bpy.context.region_data : bpy.types.RegionView3D, 
bpy.context.scene : bpy.types.Scene, 
bpy.context.screen : bpy.types.Screen, 
bpy.context.space_data : bpy.types.Space, 
bpy.context.tool_settings : bpy.types.ToolSettings, 
bpy.context.view_layer : bpy.types.ViewLayer, 
bpy.context.window : bpy.types.Window, 
bpy.context.window_manager : bpy.types.WindowManager, 
bpy.context.workspace : bpy.types.WorkSpace,

## Screen Context


## View3D Context

## Buttons Context

## Image Context

## Node Context