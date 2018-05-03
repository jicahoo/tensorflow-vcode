# coding: utf-8

import tensorflow as tf

if __name__ == '__main__':
    tf.get_default_graph()
    c = tf.constant(1.0)
    graph = tf.get_default_graph()
    operations = graph.get_operations()
    weight=tf.Variable(0.8)
    output_value = weight*c
    op = graph.get_operations()[-1]
    for op_input in op.inputs: 
        print op_input
    sess = tf.Session()
    #sess.run(c)
    init = tf.global_variables_initializer()
    sess.run(init)
    sess.run(output_value)
    summary_writer = tf.summary.FileWriter('log_summary', sess.graph)
