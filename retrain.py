from __future__ import print_function

import numpy as np
import warnings

from keras.models import Model
from keras.layers import Flatten, Dense, Input
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils.layer_utils import convert_all_kernels_in_model
from keras.utils.data_utils import get_file
from keras import backend as K
from keras.layers.core import Dropout
from scipy import misc
from keras.optimizers import rmsprop
from keras.optimizers import sgd
from keras.optimizers import adam
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Activation
from keras.preprocessing.image import ImageDataGenerator
import copy
import sys

class Retrian:

    def __init__(self):
        self.weight_path = None
        self.image_data_path = None
        self.rating_path = None
        self.network = None


    def Build_network(self,weight_ID):
        #------loadweight----------
        self.weight_path = 'weight/'+weight_ID+'.h5'
        #------build network-------
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
        self.model.load_weights(self.weight_path)
        print('model build finish')


    def Train(self,image_data_id,rating_id):
        self.image_data_path = 'data/'+image_data_id+'.npy'
        self.rating_path = 'data/'+rating_id+'.npy'
        X = np.load(self.image_data_path)
        y = np.load(self.rating_path)

        for layer in self.model.layers[:18]:
            layer.trainable = False

        opt = sgd(lr=1e-1,momentum=0.8,decay=0.5)
        self.model.compile(loss='mean_squared_error',
                                 optimizer=opt,
                                 metrics=['mean_absolute_error'])
        self.model.fit(X,y,batch_size=10,nb_epoch=20,verbose=1)

    def Save_network(self,name):
        path = 'weight/'+name+'.h'
        self.model.save_weights(path)


def retrain(data_id,rating_id,weight_ID,save_weight_id):
    AI = Retrian()
    AI.Build_network(weight_ID)
    AI.Train(data_id,rating_id)
    AI.Save_network(save_weight_id)


if __name__ == '__main__':
    data_id = sys.argv[1]
    rating_id = sys.argv[2]
    weight_id = sys.argv[3]
    save_weight_id = sys.argv[4]
    retrain(data_id,rating_id,weight_id,save_weight_id)
