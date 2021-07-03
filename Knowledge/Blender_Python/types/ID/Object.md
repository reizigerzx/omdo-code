# Object

```python
import bpy

view_layer = bpy.context.view_layer

light_data = bpy.data.lights.new(name="New Light", type='POINT')
light_object = bpy.data.objects.new(name="New Light", object_data=light_data)
view_layer.active_layer_collection.collection.objects.link(light_object)

light_object.location = (5.0, 5.0, 5.0)
light_object.select_set(True)
view_layer.objects.active = light_object
```