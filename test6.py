import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import numpy as np
import matplotlib.pyplot as plt
import math

tf.logging.set_verbosity(tf.logging.ERROR)
#输入数据Mnist数据集
#mnist = input_data.read_data_sets("MNIST_data",one_hot = True)

a=tf.constant([1.2,3.2])
b=tf.constant([4.5,5.4])
result1=a*b
result2=a+b

w1=tf.Variable(tf.random_normal((2,3),stddev=1,seed=1))
w2=tf.Variable(tf.random_normal((3,1),stddev=1,seed=1))
x=tf.constant([[0.7,0.9]])
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

sess = tf.InteractiveSession()
print(result1.eval(),result2.eval())
sess.run(w1.initializer)
sess.run(w2.initializer)

print(y.eval())

x1=-20
y1= 1/(1 + math.exp(-x1))
print(y1)

sess.close()

