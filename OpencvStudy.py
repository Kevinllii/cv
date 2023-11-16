import cv2   #opencv读取的格式为BGR
import numpy as np
import matplotlib.pyplot as plt

#  ----------------计算机眼中的图像---------------  #

#调用cv2.imread读取图片数据，填写数据的绝对地址，返回到img中为图片的BGR数组
# img = cv2.imread('D:/Users/lihao/Desktop/CV/a.png')
#print(img) #输出读取的图片数据

#展示图片，创建image窗口，显示数据为img的图像
#cv2.imshow('image',img)

#等待时间，毫秒级，0表示任意键终止，不让窗口自己消失，触发设定条件消失
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#封装一个函数cv_show，调用函数可直接执行上述三步展示图片的指令
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#调用上述函数即可执行图片展示
# cv_show('image',img)

#imag.shape获取图像属性信息，H以及W值，3代表BGR彩色图类型
# print(img.shape)

#获取灰度图像数据
# img = cv2.imread('D:/Users/lihao/Desktop/CV/a.png',cv2.IMREAD_GRAYSCALE)
# print(img)
# print(img.shape)  #灰度图img.shape只显示H以及W，只有一个颜色通道（表示灰度值大小）

#显示上述生成的灰度图像
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#保存图片，第一个参数为保存地址及命名，第二个参数为想要保存图片的数据
# cv2.imwrite('D:/Users/lihao/Desktop/CV/mybaby.png',img)

# #图片格式type(img)
# print(type(img))
#
# #图片像素点的个数img.size
# print(img.size)
#
# #图片数据类型img.dtype
# print(img.dtype)

#  ----------------视频的读取与处理---------------  #

#调用cv2.VideoCapture获取视频
# vc = cv2.VideoCapture('D:/Users/lihao/Desktop/CV/cat.mp4')

#检查是否正确打开
# if vc.isOpened():
#     open, frame = vc.read() #vc.read()返回两个参数，分别是open与frame，open是bool类型，为True时，代表正确打开；为False时，代表打开错误  vc.read一帧一帧地读取视频，形成数组,frame为这一帧图像的数组
# else:
#     open = False
#
# while open:  #遍历其中的每一帧，形成视频
#     ret, frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #调用cv2.cvtColor将彩色转为灰度图，frame为这一帧图像，cv2.COLOR_BGR2GRAY是将获取的frame从BGR图像转为GRAY图像
#         cv2.imshow('result',gray) #展示转换为灰度图后的图像
#         if cv2.waitKey(20) & 0xFF == 27: #等待时间到或者按下退出键（0xFF==27为退出键）时，跳出循环  cv2.waitKey()设置等待时间，数字代表处理完一帧图片后等待多少时间再处理下一帧
#             break
# vc.release()
# cv2.destroyAllWindows()  #销毁窗口

#  ----------------截取部分图像数据---------------  #
# img = cv2.imread('D:/Users/lihao/Desktop/CV/a.png')  #image为获取的图像数组信息
# baby = img[0:500, 0:500]  #可截取部分图像 ROI：Region of Interest
# # cv_show('babypart',baby) #调用前面定义的cv_show函数显示图像
#
# #  ----------------颜色通道提取---------------  #
# B, G, R = cv2.split(img)  #将三路颜色通道分别提取出来
# print(B)                  #显示B通道数组
# print(B.shape)            #显示B通道像素点大小，B,G,R像素点大小都是相同的
#
# # img = cv2.merge((B,G,R))  #将三通道组合在一起
# # print(img.shape)          #显示三路颜色通道
#
# #只保留R通道
# cur_img = img.copy()  #将img的数据信息拷贝到cur_img 不拷贝也可以，后面直接用img的数组操作也可以
# cur_img[:, :, 0] = 0    #cur_image[761,761,3]中，前两个代表的是像素点信息，最后一个3代表BGR三路通道，因此，只保留R的话需要把B和G赋值为0，B,G,R在数组中的顺序为0，1，2
# cur_img[:, :, 1] = 0    #因此，cur_img[:,:,0]=0中冒号代表保留全部，最后一个0代表选择B通道，赋值为0，则B通道消失；同理cur_img[:,:,1]=0代表G通道消失
# cv_show('R', cur_img) #调用cv_show显示只保留R颜色通道的图片
#
# #只保留G通道
# cur_img = img.copy()
# cur_img[:, :, 0] = 0
# cur_img[:, :, 2] = 0
# cv_show('G', cur_img)
#
# #只保留B通道
# cur_img = img.copy()
# cur_img[:, :, 1] = 0
# cur_img[:, :, 2] = 0
# cv_show('B', cur_img)
#
# img = cv2.merge((B, G, R))  #将三通道组合在一起
# print(img.shape)            #显示三路颜色通道
# cv_show('merge', img)

#  ----------------边界填充---------------  #
img = cv2.imread('D:/Users/lihao/Desktop/CV/a.png')  #读取图片数据
color_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)       #opencv读取出来的彩色图片默认是BGR格式的，而matplotlib图片的展示是按照RGB展示的，所以需要将BGR转化为RGB格式，如果不转换，图片的颜色会很奇怪

top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)   #定义图片边界填充上下左右的像素

#使用cv2.copyMakeBorder函数创建边界，但是边界填充的类型有多种，第一个参数为图片名称，中间四个为上下左右扩充的像素大小，最后一个参数为填充的类型
replicate = cv2.copyMakeBorder(color_img, top_size, bottom_size, left_size, right_size, borderType = cv2.BORDER_REPLICATE)  #BORDER_REPLICATE：复制法，也就是复制最边缘的像素
reflect = cv2.copyMakeBorder(color_img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)                   #BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两遍进行复制，例如fedcba | abcdefgh | hgfedcb
reflect101 = cv2.copyMakeBorder(color_img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)            #BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，例如gfedcb | abcdefgh |gfedcba
wrap = cv2.copyMakeBorder(color_img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)                         #BORDER_WRAP：外包装法，例如cdefgh | abcdefgh |abcdefg
constant = cv2.copyMakeBorder(color_img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value = 0)      #BORDER_CONSTANT：常量法，常数值填充，常值由value定义
# cv_show('ORIGINAL', color_img)
# cv_show('REPLICATE', replicate)
# cv_show('REFLECT', reflect)
# cv_show('REFLECT101', reflect101)
# cv_show('WRAP', wrap)
# cv_show('CONSTANT', constant)
# print(color_img.shape)
# print(replicate.shape)
# print(reflect.shape)
# print(reflect101.shape)
# print(wrap.shape)
# print(constant.shape)

#plt.subplot函数用于直接指定划分方式和位置进行绘图，231代表将整个图像窗口划分为两行三列，当前位置为1，同理232表示当前位置为2
#
plt.subplot(231), plt.imshow(color_img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()


















