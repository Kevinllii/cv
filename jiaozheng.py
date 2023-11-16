import cv2
import numpy as np
left_mtx = np.array([[1324.7,    -0.6,  849.5],
                     [     0,  1338.3,  892.3],
                     [     0,       0,      1]])                        #输入左侧相机的内参矩阵3*3
left_dist = np.array([[  -0.5154,0.2967, -0.0007, -0.0044, -0.0967]])       #输入左侧相机的畸变系数1*5
right_mtx = np.array([[1326.3,     8.5,  835.7],
                      [     0,  1334.2,  885.9],
                      [     0,       0,      1]])             #输入右侧相机的内参矩阵3*3
right_dist = np.array([[-0.5149, 0.2792,  0.0030,  -0.0052,  -0.0739]])     #输入右侧相机的畸变系数1*5
R = np.array([[ 0.9992,  -0.0193, -0.0343],
              [ 0.0198,   0.9997,  0.0149],
              [ 0.0340,  -0.0156,  0.9993]])                          #输入双目相机的旋转矩阵3*3
T = np.array([[-175.3133], [7.6192], [-7.2759]])                      #输入双目相机的平移矩阵3*1
# 左右相机拍摄的图像
left_img = cv2.imread('E:/PycharmProjects/PythonStudy/left/L0.png')         #输入左侧相机拍摄图像的正确地址
right_img = cv2.imread('E:/PycharmProjects/PythonStudy/right/R0.png')       #输入右侧相机拍摄图像的正确地址

# 图像的尺寸
img_size = (left_img.shape[0],left_img.shape[1])
print(img_size)
# 使用校正参数进行双目相机校正
rectify_scale = 0
R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(left_mtx, left_dist, right_mtx, right_dist, img_size, R, T, rectify_scale, (0,0))
# 计算映射矩
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_mtx, left_dist, R1, P1, img_size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_mtx, right_dist, R2, P2, img_size, cv2.CV_16SC2)
# 使用映射矩阵对图像进行校正
left_undistorted = cv2.remap(left_img, left_map1, left_map2, cv2.INTER_LINEAR)
right_undistorted = cv2.remap(right_img, right_map1, right_map2, cv2.INTER_LINEAR)
# 显示校正后的图像
# cv2.namedWindow("Left Undistorted", 0)
# cv2.resizeWindow("Left Undistorted", 760,760)
cv2.imshow('Left Undistorted', left_undistorted)
cv2.imshow('Right Undistorted', right_undistorted)
# cv2.imwrite("D:/Users/lihao/Desktop/CV/zuo/zuo1.png" , left_undistorted)  # 设置拍摄照片的保存路径
# cv2.imwrite("D:/Users/lihao/Desktop/CV/you/you1.png" , left_undistorted)  # 设置拍摄照片的保存路径
cv2.waitKey(0)
cv2.destroyAllWindows()
print(left_undistorted.shape)
print(right_undistorted.shape)