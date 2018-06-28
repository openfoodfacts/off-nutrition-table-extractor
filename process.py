import os
import argparse
import csv

import pytesseract

from crop import crop_img

# def crop(image_path, coords, saved_location, extend_ratio=0):
#     """
#     @param image_path: The path to the image to edit
#     @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
#     @param saved_location: Path to save the cropped image
#     @param extend_ratio: The value by which the bounding boxes to be extended to accomodate the text that has been cut
#     """
#     image_obj = Image.open(image_path)
#     nx, ny = image_obj.size
#     print()
#     # extend_ratio = 0.005
#     modified_coords = (coords[0]-extend_ratio*nx, coords[1]-extend_ratio*ny, coords[2]+extend_ratio*nx, coords[3]+extend_ratio*ny)
#     cropped_image = image_obj.crop(modified_coords)
#     # cropped_image.save(saved_location)
#     cropped_image.show()
#     return cropped_image


def ocr(img, oem=1):
    """
    @param img: The image to be OCR'd
    @param oem: for specifying the type of Tesseract engine( default=1 for LSTM OCR Engine)
    """
    config = ('-l eng --oem {} --psm 3'.format(oem))

    text = pytesseract.image_to_string(img, config=config)
    return text


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

    for blob_cord in coordinates_list:
        cropped_image = crop(image, blob_cord, 'testing/ocr/cropped{}.jpg'.format(blob_cord[1]), 0.005)
        text = ocr(cropped_image)
        print(text)

    
