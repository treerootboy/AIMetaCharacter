# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "pose-binding",
    "author" : "liming",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import time
import bpy
import cv2
class PoseBinding(bpy.types.WorkSpaceTool):
    bl_label = "Pose Binding"
    bl_space_type = "VIEW_3D"
    bl_context_mode = "OBJECT"
    bl_idname = "ui_plus.pose_binding"
    bl_icon = "ops.generic.select_circle"

    def draw_settings(context, layout, tool):
        row = layout.row()
        row.operator("wm.pose_detect", text="Capture", icon="OUTLINER_OB_CAMERA")

class PoseDetect(bpy.types.Operator):
    bl_idname = "wm.pose_detect"
    bl_label = "Pose Detect"

    cap = None

    def modal(self, context, event):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            time.sleep(1.0)
        _, image = self.cap.read()
        cv2.imshow("Output", image)
        cv2.waitKey(1)
        return {'PASS_THROUGH'}

    def stop_playback(self, scene):
        print(format(scene.frame_current) + " / " + format(scene.frame_end))
        if scene.frame_current == scene.frame_end:
            bpy.ops.screen.animation_cancel(restore_frame=False)
        
    def execute(self, context):
        bpy.app.handlers.frame_change_pre.append(self.stop_playback)

        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm  = context.window_manager
        cv2.destroyAllWindows()
        self.cap.release()
        self.cap = None

def register():
    bpy.utils.register_tool(PoseBinding, separator=True, group=True)
    bpy.utils.register_class(PoseDetect)

def unregister():
    bpy.utils.unregister_tool(PoseBinding)
    bpy.utils.unregister_class(PoseDetect)

if __name__ == "__main__":
    register()
