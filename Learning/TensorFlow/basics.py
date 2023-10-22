import tensorflow as tf

scalar = tf.constant(100)
vector = tf.constant([1, 2])
matrix = tf.constant([[6, 9], [2, 18]])

print(scalar)
print(vector)
print(matrix)

float_matrix = tf.constant([[9., 2.], [11., 6.], [7., 3.]], dtype=tf.float16)
tensor = tf.constant([[[12., 8., 2.], [4., 2., 7.], [8., 3., 4.]], [[4., 5., 1.], [9., 6., 2.], [7., 0., 2.]], [[5., 1., 3.], [9., 0., 6.], [2., 4., 5.]]], dtype=tf.float16)

print(float_matrix)
print(tensor)


