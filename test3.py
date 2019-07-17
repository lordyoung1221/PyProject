import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100)) # 随机输入
print(x_data,"\n")
y_data = np.dot([0.100, 0.200], x_data)+ 0.3
print(y_data,"\n")

# 构造一个线性模型
#
b = tf.Variable(tf.zeros([1]))
print(b,"\n")
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
print(W,"\n")
y = tf.matmul(W, x_data) + b
print(y,"\n")

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
print(loss,"\n")
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()
print(init,"\n")

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(1000):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))