import numpy as np
import cv2

# img1 = cv2.imread(r"/Users/inbc/Desktop/zuo/Left1.bmp")
# img2 = cv2.imread(r"/Users/inbc/Desktop/you/Right1.bmp")
for i in range(0, 47):
    # imgT = cv2.imdecode(np.fromfile('./images/%d.bmp'  %i ,dtype=np.uint8), -1)
    imgT = cv2.imdecode(np.fromfile('D:/Users/lihao/Desktop/CV/photo/%d.png' % i, dtype=np.uint8), -1)  # 读取拍摄的左右双目照片

    # cv2.imshow("zuo", img1[300:1200, 500:2000])
    # cv2.imshow("you", img2[300:1200, 500:2000])

    # cv2.waitKey(0)

    # 设置左右照片的存储位置
    cv2.imwrite("D:/Users/lihao/Desktop/CV/you/reLeft%d.png" % i, imgT[0:480, 0:640])  # imgL的第一个参数是图片高度像素范围，第二个参数是图片宽度的像素范围
    cv2.imwrite("D:/Users/lihao/Desktop/CV/zuo/reRight%d.png" % i, imgT[0:480, 640:1280])
    print("Resize images%d Fnished!" % i)

print("Fnished All!!!")