import bpy
from bpy.types import UILayout


def main(context):
  for ob in context.scene.objects:
    print(ob)

bpy.data.objects[0].name

class SimpleOperator(bpy.types.Operator):
  """Tooltip"""
  bl_idname = "object.simple_operator"
  bl_label = "Simple Object Operator"
  lalala:UILayout = None

  @classmethod
  def poll(cls, context):
    return context.active_object is not None

  def execute(self, context):
    main(context)
    return {'FINISHED'}

def register():
  bpy.utils.register_class(SimpleOperator)

def unregister():
  bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
  register()

  # test call
  bpy.ops.object.simple_operator()