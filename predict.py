from __future__ import print_function

import numpy as np
import warnings

from keras.models import Model
from keras.layers import Flatten, Dense, Input
from keras.layers import Convolution2D, MaxPooling2D
from scipy import misc
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Activation
import copy
from PIL import Image, ImageDraw
import os
import cv2
import sys


class Are_U_Beatutifut:
    def __init__(self):
        self.path = 'weight/20170311-2.h5'
        self.model = None
        self.read_dir = 'image/'
        self.save_dir = 'temp/'

    #build the vgg-network
    def build(self):
        input_shape = (224, 224, 3)
        img_input = Input(shape=input_shape)
        # Block 1
        x = Convolution2D(64, 3, 3, activation='relu', border_mode='same', name='conv1_1')(img_input)
        x = Convolution2D(64, 3, 3, activation='relu', border_mode='same', name='conv1_2')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='pool1')(x)

        # Block 2
        x = Convolution2D(128, 3, 3, activation='relu', border_mode='same', name='conv2_1')(x)
        x = Convolution2D(128, 3, 3, activation='relu', border_mode='same', name='conv2_2')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='pool2')(x)

        # Block 3
        x = Convolution2D(256, 3, 3, activation='relu', border_mode='same', name='conv3_1')(x)
        x = Convolution2D(256, 3, 3, activation='relu', border_mode='same', name='conv3_2')(x)
        x = Convolution2D(256, 3, 3, activation='relu', border_mode='same', name='conv3_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='pool3')(x)

        # Block 4
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv4_1')(x)
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv4_2')(x)
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv4_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='pool4')(x)

        # Block 5
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv5_1')(x)
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv5_2')(x)
        x = Convolution2D(512, 3, 3, activation='relu', border_mode='same', name='conv5_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='pool5')(x)

        x = Flatten(name='flatten')(x)

        x = Dense(1024, activation=None, name='fc6')(x)
        x = BatchNormalization()(x)
        x = Activation(activation='relu')(x)

        x = Dense(512, activation=None, name='fc7')(x)
        x = BatchNormalization()(x)
        x = Activation(activation='relu')(x)

        x = Dense(1, activation=None, name='fc8')(x)
        x = BatchNormalization()(x)
        out = Activation(activation='sigmoid')(x)

        self.model = Model(img_input, out)
        self.model.load_weights(self.path)
        print('model build finish')

    def predict(self,image_name):   #此处传入numpy类型
        im = misc.imresize(image_name, (224, 224)).astype(np.float32)
        aux = copy.copy(im)
        im[:, :, 0] = aux[:, :, 2]
        im[:, :, 2] = aux[:, :, 0]
        # Remove image mean
        im[:, :, 0] -= 93.5940
        im[:, :, 1] -= 104.7624
        im[:, :, 2] -= 129.1863
        im = np.expand_dims(im, axis=0)
        #im = im/255.
        res = self.model.predict(im)
        res = res*100
        return res

    def detectFaces(self,image_path):  #图片路径
        #img = cv2.imread(image_path)
        img = misc.imread(image_path,mode='RGB')
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
            #result.append((x-width, y-height, x + width, y + height))
        return result


    def draw_image(self,image_name):   #用于保存框住的图片
        image_path = self.read_dir+image_name
        faces = self.detectFaces(image_path)     #检测人脸位置
        img = Image.open(image_path)
        if faces:
            draw_instance = ImageDraw.Draw(img)
            for (x1, y1, x2, y2) in faces:
                draw_instance.rectangle((x1, y1, x2, y2), outline=(255,0,0))
        img.save(self.save_dir + image_name)
        #此处还差一个给人脸上标记的功能，有时间在写吧。。。。。。。

    def rating(self,image_name):
        image_path = self.read_dir + image_name
        positions = self.detectFaces(image_path)
        img = Image.open(image_path).convert('RGB')
        count = len(positions)
        rating = []
        flag = 0
        result = []
        if positions:
            flag = 1
            rating = np.zeros([count])
            i = 0
            for (x1,y1,x2,y2) in positions:
                data = img.crop((x1,y1,x2,y2))
                rating[i] = self.predict(data)   #对人得分进行预测
                i+=1
            rating = rating.tolist()
        else:
            print('no face in the image')
        result.append(flag)
        result.append(count)
        result.extend(rating)
        return result

def predict1(image_name=None):
    AI = Are_U_Beatutifut()
    AI.build()
    image_dir = 'image/'
    save_dir = 'temp/'
    result = []
    if image_name:
        AI.draw_image(image_name)
        result = AI.rating(image_name)
        return result
    else:
        return None

if __name__ == '__main__':
    image_name = sys.argv[1]
    result = predict1(image_name)
    #flag, count, rating = predict('001.jpg')
    print(result)






