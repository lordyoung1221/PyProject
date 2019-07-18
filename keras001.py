# _*_ coding: utf-8 _*_

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPooling2D
from keras import backend as K

num_classes = 10
img_rows,img_cols=28,28

(trainX,trainY),(testX,testY)=mnist.load_data()

if K.image_data_format()=='channels_first':
    print('channels_first')
    trainX = trainX.reshape(trainX.shape[0],1,img_rows,img_cols)
    testX = testX.reshape(testX.shape[0],1,img_rows,img_cols)
    input_shape=(1,img_rows,img_cols)
else:
    trainX = trainX.reshape(trainX.shape[0], img_rows, img_cols,1)
    testX = testX.reshape(testX.shape[0],img_rows, img_cols,1)
    input_shape = (img_rows, img_cols,1)
trainX=trainX.astype('float32')
testX = testX.astype('float32')
trainX /= 255.0
testX /= 255.0

trainY=keras.utils.to_categorical(trainY,num_classes)
testY=keras.utils.to_categorical(testY,num_classes)

model=Sequential()
model.add(Conv2D(32,kernel_size=(5,5),activation='relu',input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64,(5,5),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(500,activation='relu'))
model.add(Dense(num_classes,activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(),
              metrics=['accuracy'])

model.fit(trainX,trainY,batch_size=128,epochs=20,
          validation_data=(testX,testY))
score=model.evaluate(testX,testY)
print(score[0])
print(score[1])