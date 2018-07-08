from PIL import Image
import argparse

from detect_table_class import NutritionTableDetector
from crop import crop_img, crop
from text_detection import text_detection
from process import ocr
from regex import *
from nutrient_list import make_list

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = ap.parse_args()

    #Make the table detector class and predict the score
    obj = NutritionTableDetector()
    image = Image.open(args.image)
    boxes, scores, classes, num  = obj.get_classification(image)
    width, height = image.size

    #Select the bounding box with most confident output
    ymin = boxes[0][0][0]*height
    xmin = boxes[0][0][1]*width
    ymax = boxes[0][0][2]*height
    xmax = boxes[0][0][3]*width

    # print(xmin, ymin, xmax, ymax, scores[0][0])
    coords = (xmin, ymin, xmax, ymax)

    #Crop the image with the given bounding box
    crop_img(image, coords, "./test_images/output.jpg", 0, True)

    #detect the text
    text_blob_list = text_detection("./test_images/output.jpg")

    #Apply OCR to to blobs
    for blob_cord in text_blob_list:
        
        cropped_image = crop("./test_images/output.jpg", blob_cord, 0.005)

        text = ocr(cropped_image)
        text = clean_string(text)
        
        if check_for_label(text, make_list('big.txt')):

            label_name, label_value = get_label_from_string(text)
            print(label_name+", "+ label_value)

        # print(text)
if __name__ == '__main__':
    main()