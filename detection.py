# from PIL import Image
import argparse
import time
import cv2

from detect_table_class import NutritionTableDetector
from crop import crop
from text_detection import text_detection
from process import *
from regex import *
from nutrient_list import make_list
from spacial_map import *

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = ap.parse_args()

    #Start the time
    start_time = time.time()
    #Make the table detector class and predict the score
    obj = NutritionTableDetector()

    image = cv2.imread(args.image)
    boxes, scores, classes, num  = obj.get_classification(image)
    # width, height = image.size
    width = image.shape[1]
    height = image.shape[0]

    time_taken = time.time() - start_time
    print("Time taken to detect the table: %.5fs" % time_taken)

    #Select the bounding box with most confident output
    ymin = boxes[0][0][0]*height
    xmin = boxes[0][0][1]*width
    ymax = boxes[0][0][2]*height
    xmax = boxes[0][0][3]*width

    # print(xmin, ymin, xmax, ymax, scores[0][0])
    coords = (xmin, ymin, xmax, ymax)

    #Crop the image with the given bounding box
    # cropped_image = crop(image, coords, "./data/result/output.jpg", 0, True)
    cropped_image = crop(image, coords, "./test_images/output.jpg", 0, True)

    # cropped_image = preprocess_for_ocr(cropped_image)
    #detect the text
    text_blob_list = text_detection(cropped_image)
    time_taken = time.time() - start_time
    print("Time Taken to detect bounding boxes for text: %.5fs" % time_taken)
    # print(text_blob_list)
    #Apply OCR to to blobs
    # for blob_cord in text_blob_list:
        
    #     word_image = crop(cropped_image, blob_cord, "./", 0.005, False)
    #     # word_image = preprocess_for_ocr(word_image)
    #     text = ocr(word_image)
    #     text = clean_string(text)

    #     # if check_for_label(text, make_list('data/big.txt')):

    #     #     label_name, label_value = get_label_from_string(text)
    #     #     print(label_name+", "+ label_value)

    #     # print(text)
    # time_taken = time.time() - start_time
    # print("Total Time Taken: %.5fs" % time_taken)
    text_location_list = []
    for blob_cord in text_blob_list:
        word_image = crop(cropped_image, blob_cord, "./", 0.005, False)
        word_image = preprocess_for_ocr(word_image)
        text = ocr(word_image)
 
        if text:
            centre_x = (blob_cord[0]+blob_cord[2])/2
            centre_y = (blob_cord[1]+blob_cord[3])/2
            box_centre = (centre_x, centre_y)

            new_location = {
                'bbox': blob_cord,
                'text': text,
                'box_centre': box_centre,
                'string_type': string_type(text)
            }
            text_location_list.append(new_location)

    for text_dict in text_location_list:
        # print(text['text'], text['string_type'])
        if(text_dict['string_type']==0):
            text = clean_string(text_dict['text'])

            if check_for_label(text, make_list('data/big.txt')):
                label_name, label_value = get_label_from_string(text)
                print(label_name+", "+ label_value)

                # print(text) 
                   

    time_taken = time.time() - start_time
    print("Total Time Taken: %.5fs" % time_taken)

if __name__ == '__main__':
    main()