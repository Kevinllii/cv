import cv2
# cap =cv2.VideoCapture(0)    # 打开相机，根据设备而定，一般是0或1
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,3040)     # 设置相机分辨率 2560x720
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1520)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 保存为avi格式
# out = cv2.VideoWriter('myvideo.avi',fourcc, 20.0,(640,480))
# i= 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     out.write(frame)
#     cv2.namedWindow("camera", 0)
#     cv2.resizeWindow("camera", 3040,1520)
#     cv2.imshow('camera',frame)
#     key = cv2.waitKey(1)
#     if  key == ord('q') or key == 27:      # 按下q退出程序并保存视频
#         break
#     if key == ord("w"):                 # 按下w保存图片
#         cv2.imwrite("./out/%d.png" % i, frame)  # 设置拍摄照片的保存路径
#         print("Save images %d succeed!" % i)
#         i += 1
# cap.release()
# out.release()
# cv2.destroyAllWindows()

from PIL import Image
import os

path = r'E:\PycharmProjects\PythonStudy\out'  # 文件目录
# path这个目录处理完之后需要手动更改
path_list = os.listdir(path)
print(path_list)

for i in path_list:  # 截左半张图片
    a = open(os.path.join(path, i), 'rb')
    img = Image.open(a)
    w = img.width  # 图片的宽
    h = img.height  # 图片的高
    print('正在处理图片', i, '宽', w, '长', h)

    box = (0, 0, w * 0.5, h)  # box元组内分别是 所处理图片中想要截取的部分的 左上角和右下角的坐标
    img = img.crop(box)
    print('正在截取左半张图...')
    img.save(r"E:\PycharmProjects\PythonStudy\right\\"+'R' + i)  # 这里需要对截出的图加一个字母进行标识，防止名称相同导致覆盖
    print('L-', i, '保存成功')

for i in path_list:  # 截取右半张图片
    a = open(os.path.join(path, i), 'rb')
    img = Image.open(a)
    w = img.width  # 图片的宽
    h = img.height  # 图片的高
    print('正在处理图片', i, '宽', w, '长', h)

    box = (w * 0.5, 0, w, h)
    img = img.crop(box)
    print('正在截取右半张图...')
    img.save(r"E:\PycharmProjects\PythonStudy\left\\"+'L' + i)
    print('R-',i, "保存成功")

print("'{}'目录下所有图片已经保存到本文件目录下。".format(path))