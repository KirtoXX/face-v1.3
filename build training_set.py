import numpy as np
import cv2

class Build_train_set:
    def __init__(self):
        self.image_dir = None
        self.image_rating_path = None

    def detectFaces(self,image_path):  #图片路径
        img = cv2.imread(image_path)
        #opencv 用于人脸检测的特征
        face_cascade = cv2.CascadeClassifier("haarcascades_cuda/haarcascade_frontalface_alt2.xml")
        if img.ndim == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img  # if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

        faces = face_cascade.detectMultiScale(gray, 1.3,5)  # 1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
        result = []
        for (x, y, width, height) in faces:
            result.append((x-width*0.1, y-height*0.15, x + width*1.05, y + height*1.05))     #设置框住人脸的大小
        return result

    def set_dir(self,path):
        self.image_dir = path

