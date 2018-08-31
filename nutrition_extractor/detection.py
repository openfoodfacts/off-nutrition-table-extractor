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

def detect(img_path):
    """
    @param img_path: Pathto the image for which labels to be extracted
    """

    #Start the time
    start_time = time.time()
    #Make the table detector class and predict the score
    obj = NutritionTableDetector()

    image = cv2.imread(img_path)
    boxes, scores, classes, num  = obj.get_classification(image)
    #Get the dimensions of the image
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
    cropped_image = crop(image, coords, "./data/result/output.jpg", 0, True)

    #Apply several filters to the image for better results in OCR
    cropped_image = preprocess_for_ocr(cropped_image)
    
    #detecting the text
    text_blob_list = text_detection(cropped_image)
    time_taken = time.time() - start_time
    print("Time Taken to detect bounding boxes for text: %.5fs" % time_taken)
    # print(text_blob_list)

    text_location_list = []   #store all the metadata of every text box
    nutrient_dict = {}        # Dictionary to store nutrient labels and their values

    #Apply OCR to to blobs and save data in organized dict
    for blob_cord in text_blob_list:
        word_image = crop(cropped_image, blob_cord, "./", 0.005, False)
        word_image = preprocess_for_ocr(word_image)
        text = ocr(word_image)
 
        if text:
            center_x = (blob_cord[0]+blob_cord[2])/2
            center_y = (blob_cord[1]+blob_cord[3])/2
            box_center = (center_x, center_y)

            new_location = {
                'bbox': blob_cord,
                'text': text,
                'box_center': box_center,
                'string_type': string_type(text)
            }
            text_location_list.append(new_location)

    #Spacial algorithm that maps all boxes according to their location and append the string 
    for text_dict in text_location_list:
        if(text_dict['string_type']==2):
            for text_dict_test in text_location_list:
                if position_definer(text_dict['box_center'][1], text_dict_test['bbox'][1], text_dict_test['bbox'][3]) and text_dict_test['string_type']==1:
                    text_dict['text'] = text_dict['text'].__add__(' '+text_dict_test['text'])
                    text_dict['string_type'] = 0

    #Add the nutritional label and its value to the nutrient_dict
    for text_dict in text_location_list:
               
        if(text_dict['string_type']==0):
            # print(text_dict['text']) 
            text = clean_string(text_dict['text'])

            if check_for_label(text, make_list('data/big.txt')):
                label_name, label_value = get_label_from_string(text)
                nutrient_dict[label_name] = separate_unit(label_value)
    
    time_taken = time.time() - start_time
    print("Total Time Taken: %.5fs" % time_taken)

    return nutrient_dict


#main function to test different functions independently
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = ap.parse_args()
    
    print(detect(args.image))

if __name__ == '__main__':
    main()