import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time

tf.logging.set_verbosity(tf.logging.ERROR)
#输入数据Mnist数据集
mnist = input_data.read_data_sets("MNIST_data",one_hot = True)

#建立读取批次机制
batch_size = 100
print(mnist.train.num_examples)
n_batch = mnist.train.num_examples // batch_size
print(n_batch)

#权值初始化
def Weights_Variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    print(initial)
    return tf.Variable(initial)

#偏置值初始化
def Biases_Variable(shape):
    initial = tf.constant(0.1,shape = shape)
    print(initial)
    return tf.Variable(initial)

#定义卷积函数
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides = [1,1,1,1],padding = 'SAME')

#定义池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize = [1,2,2,1],strides = [1,2,2,1],padding = 'SAME')




