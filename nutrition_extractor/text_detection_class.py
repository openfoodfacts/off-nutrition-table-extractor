import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile

class NutritionTextDetector(object):
    def __init__(self):
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
            self.sess = tf.compat.v1.Session(config=config)
            with gfile.FastGFile('data/ctpn.pb', 'rb') as f:
                graph_def = tf.compat.v1.GraphDef()
                graph_def.ParseFromString(f.read())
                self.sess.graph.as_default()
                tf.import_graph_def(graph_def, name='')
            #sess.run(tf.global_variables_initializer()

            self.input_img = self.sess.graph.get_tensor_by_name('Placeholder:0')
            self.output_cls_prob = self.sess.graph.get_tensor_by_name('Reshape_2:0')
            self.output_box_pred = self.sess.graph.get_tensor_by_name('rpn_bbox_pred/Reshape_1:0')

        self.sess = tf.compat.v1.Session(graph=self.detection_graph)

    def get_text_classification(self, blobs):
    # Bounding Box Detection.
        with self.detection_graph.as_default():
            (cls_prob, box_pred) = self.sess.run(
                [self.output_cls_prob, self.output_box_pred], 
                feed_dict={self.input_img: blobs['data']})

        return cls_prob, box_pred
