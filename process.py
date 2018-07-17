import os
import argparse
import csv
import cv2
import pytesseract
from PIL import Image
import numpy as np

# from crop import crop

def preprocess_for_ocr(img):

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)

    # img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)[1]

    return img

def ocr(img, oem=1):
    """
    @param img: The image to be OCR'd
    @param oem: for specifying the type of Tesseract engine( default=1 for LSTM OCR Engine)
    """
    config = ('-l eng --oem {} --psm 3'.format(oem))

    try:
        img = Image.fromarray(img)
        text = pytesseract.image_to_string(img, config=config)
        return text
    except:
        return ""


if __name__ == '__main__':

    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required=True, help="path to the input image")
    # args = vars(ap.parse_args())

    filename = '0044000028015_2'
    # filename = "0044738018340_2"
    image = 'testing/demo/{}.jpg'.format(filename)


    with open(os.path.join("testing/results", "res_{}.txt".format(filename)), 'r') as f:
        c = csv.reader(f,delimiter=',')
        l = []
        for row in c:
            l.append(tuple(map(int, row)))
        coordinates_list = tuple(l)

    # coordinates_list = ((31, 952, 1853, 2241), (31, 1152, 1683, 2241), (39, 752, 1853, 2241))

    # for blob_cord in coordinates_list:
    #     cropped_image = crop(image, blob_cord, 'testing/ocr/cropped{}.jpg'.format(blob_cord[1]), 0.005)
    #     text = ocr(cropped_image)
    #     print(text)

    
