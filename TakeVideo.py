import cv2
import numpy as np
# 打开左右相机
stereo_camera = cv2.VideoCapture(0)  # 请根据实际情况调整相机索引

# 设置视频帧的宽度和高度
frame_width = 760
frame_height = 760
actual_fps = stereo_camera.get(cv2.CAP_PROP_FPS)

# 设置输出视频的文件名和编解码器
output_filename = 'stereo_video.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_filename, fourcc, actual_fps, (frame_width * 2, frame_height))

while True:
    # 读取左右相机的帧
    ret, stereo_frame = stereo_camera.read()

    if not ret:
        print("Failed to capture frames.")
        break

    # 将左右帧拼接成一帧
    stereo_frame = cv2.resize(stereo_frame, (frame_width * 2, frame_height))

    # 显示拼接后的帧
    cv2.imshow('Stereo Frames', stereo_frame)

    # 写入帧到输出视频文件
    output_video.write(stereo_frame)

    # 检测键盘输入，按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
stereo_camera.release()
output_video.release()
cv2.destroyAllWindows()