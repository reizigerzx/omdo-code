# bpy.types.UILayout

```python
activate_init : bool
active : bool
active_default : bool
alert : bool
alignment : enum in [‘EXPAND’, ‘LEFT’, ‘CENTER’, ‘RIGHT’], default ‘EXPAND’
direction : enum in [‘HORIZONTAL’, ‘VERTICAL’], default ‘HORIZONTAL’, (readonly)
emboss : enum in [‘NORMAL’, ‘NONE’, ‘PULLDOWN_MENU’, ‘RADIAL_MENU’, ‘UI_EMBOSS_NONE_OR_STATUS’], default ‘NORMAL’
enabled : bool
operator_context : enum in [‘INVOKE_DEFAULT’, ‘INVOKE_REGION_WIN’, ‘INVOKE_REGION_CHANNELS’, ‘INVOKE_REGION_PREVIEW’, ‘INVOKE_AREA’, ‘INVOKE_SCREEN’, ‘EXEC_DEFAULT’, ‘EXEC_REGION_WIN’, ‘EXEC_REGION_CHANNELS’, ‘EXEC_REGION_PREVIEW’, ‘EXEC_AREA’, ‘EXEC_SCREEN’], default ‘INVOKE_DEFAULT’
scale_x : float
scale_y : float
ui_units_x : float
ui_units_y : float
use_property_decorate : bool
use_property_split : bool
row(align=False, heading='', heading_ctxt='', translate=True) : UILayout
column(align=False, heading='', heading_ctxt='', translate=True) : UILayout
column_flow(columns=0, align=False) : UILayout
grid_flow(row_major=False, columns=0, even_columns=False, even_rows=False, align=False) : UILayout
box() : UILayout
split(factor=0.0, align=False) : Layout
```