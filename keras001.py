# _*_ coding: utf-8 _*_

from keras.datasets import mnist

num_classes = 10
img_rows, img_cols = 28, 28

(trainX, trainY), (testX, testY) = mnist.load_data()
