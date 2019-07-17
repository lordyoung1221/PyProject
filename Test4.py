import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time
import matplotlib.pyplot as plt
import pylab

tf.logging.set_verbosity(tf.logging.ERROR)
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
print(mnist.train.num_examples)
print(mnist.validation.num_examples)
#print(mnist.train.images[0])

batch_xs, batch_ys = mnist.train.next_batch(10)
for one_pic_vic in batch_xs:
    one_pic_arr = np.reshape(one_pic_vic,(28,28))
    plt.imsave('MNIST_data/pic' +  ".jpg", np.array(one_pic_arr))