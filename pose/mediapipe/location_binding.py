# set bone rotation/positions
bones = bpy.data.objects["RIG-Vincent"].pose.bones

# 头部运动
'''
head_fk[0] 抬/低头
head_fk[1] 左右摇头
head_fk[2] 左右侧头
'''
bones["head_fk"].rotation_euler[0] = 0
bones["head_fk"].rotation_euler[1] = 0
bones["head_fk"].rotation_euler[2] = 0
bones["head_fk"].keyframe_insert(data_path="rotation_euler", index=-1)

# 嘴巴
'''
mouth_fk[0] 嘟/抿嘴
mouth_fk[1] 嘴巴前后移动，基本用不到（可能嘟/抿嘴时微调）
mouth_fk[2] 嘴巴开合
'''
bones["mouth_ctrl"].location[2] = 0
bones["mouth_ctrl"].location[0] = 0
bones["mouth_ctrl"].keyframe_insert(data_path="location", index=-1)

# 眉毛
'''
bones["brow_ctrl_L"].location[2] 左眼眉毛上下移动
bones["brow_ctrl_R"].location[2] 右眼眉毛上下移动
'''
bones["brow_ctrl_L"].location[2] = 0
bones["brow_ctrl_R"].location[2] = 0
bones["brow_ctrl_L"].keyframe_insert(data_path="location", index=2)
bones["brow_ctrl_R"].keyframe_insert(data_path="location", index=2)

# 眼皮
'''
bones["eyelid_up_ctrl_L"].location[2] 左上眼皮上下移动
bones["eyelid_up_ctrl_R"].location[2] 右上眼皮上下移动
bones["eyelid_low_ctrl_L"].location[2] 左下眼皮上下移动
bones["eyelid_low_ctrl_R"].location[2] 右下眼皮上下移动
'''
bones["eyelid_up_ctrl_R"].location[2] = -0
bones["eyelid_low_ctrl_R"].location[2] = 0
bones["eyelid_up_ctrl_L"].location[2] = -0
bones["eyelid_low_ctrl_L"].location[2] = 0
bones["eyelid_up_ctrl_R"].keyframe_insert(data_path="location", index=2)
bones["eyelid_low_ctrl_R"].keyframe_insert(data_path="location", index=2)
bones["eyelid_up_ctrl_L"].keyframe_insert(data_path="location", index=2)
bones["eyelid_low_ctrl_L"].keyframe_insert(data_path="location", index=2)

# 眼球
'''
bones["eye_ctrl_L"].location[0] 左眼球上下移动
bones["eye_ctrl_L"].location[2] 左眼球左右移动
bones["eye_ctrl_R"].location[0] 右眼球上下移动
bones["eye_ctrl_R"].location[2] 右眼球左右移动
'''
bpy.data.objects["GEO-vincent_eyeball_L"].rotation_euler[0] = 0
bpy.data.objects["GEO-vincent_eyeball_L"].rotation_euler[2] = 0
bpy.data.objects["GEO-vincent_eyeball_R"].rotation_euler[0] = 0
bpy.data.objects["GEO-vincent_eyeball_R"].rotation_euler[2] = 0
bpy.data.objects["GEO-vincent_eyeball_L"].keyframe_insert(data_path="rotation_euler", index=2)
bpy.data.objects["GEO-vincent_eyeball_R"].keyframe_insert(data_path="rotation_euler", index=2)