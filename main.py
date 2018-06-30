import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import glob

from collections import defaultdict
from io import StringIO
from PIL import Image

import utils
from run_inference import run_inference_for_single_image, load_image_into_numpy_array


if tf.__version__ < '1.4.0':
    raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')

PATH_TO_CKPT = 'data/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'nutrition.pbtxt')

NUM_CLASSES = 1

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

#load the labels Map
label_map = utils.load_labelmap(PATH_TO_LABELS)
categories = utils.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = utils.create_category_index(categories)

PATH_TO_TEST_IMAGES_DIR = 'test_images'

# for image_path in TEST_IMAGE_PATHS:
# for filename in glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.jpg')):
image = Image.open("test_images/2.jpg")
# the array based representation of the image will be used later in order to prepare the
# result image with boxes and labels on it.
image_np = load_image_into_numpy_array(image)
# Expand dimensions since the model expects images to have shape: [1, None, None, 3]
image_np_expanded = np.expand_dims(image_np, axis=0)
# Actual detection.
output_dict = run_inference_for_single_image(image_np, detection_graph)
# Visualization of the results of a detection.
# vis_util.visualize_boxes_and_labels_on_image_array(
#     image_np,
#     output_dict['detection_boxes'],
#     output_dict['detection_classes'],
#     output_dict['detection_scores'],
#     category_index,
#     instance_masks=output_dict.get('detection_masks'),
#     use_normalized_coordinates=True,
#     line_thickness=5)
# plt.figure(figsize=IMAGE_SIZE)
# plt.imshow(image_np)

print(output_dict['detection_boxes'][0].tolist())
print(output_dict.get('detection_masks'))