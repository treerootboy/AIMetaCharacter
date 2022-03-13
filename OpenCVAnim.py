import bpy

# 注册 blender UI 工具栏
class OBJECT_MT_OpenCVPanel(bpy.types.WorkSpaceTool):
    """Creates a Panel in the Object properties window"""
    # Layout 左边工具栏 - 工具名称
    bl_label = "OpenCV Animation"
    # 指定在那个界面展示，VIEW_3D 是默认的 3D 模型展示界面
    bl_space_type = 'VIEW_3D'
    # 指定上下文的数据格式
    bl_context_mode='OBJECT'
    # 工具的唯一ID
    bl_idname = "ui_plus.opencv"
    # 工具的icon
    bl_icon = "ops.generic.select_circle"
        
    # 右栏工具设定面板的绘制方法    
    def draw_settings(context, layout, tool):
        # 新增一行，跟 Android Compose、SwiftUI 布局差不多
        row = layout.row()
        # 注册一个按钮，名字是 Capture，注册处理动作对应的类
        op = row.operator("wm.opencv_operator", text="Capture", icon="OUTLINER_OB_CAMERA")
        
# 注册面板
def register():
    bpy.utils.register_tool(OBJECT_MT_OpenCVPanel, separator=True, group=True)

# 注销面板
def unregister():
     bpy.utils.unregister_tool(OBJECT_MT_OpenCVPanel)

if __name__ == "__main__":
    register()