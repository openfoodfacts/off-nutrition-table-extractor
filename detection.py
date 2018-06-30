from PIL import Image
import argparse

from detect_table_class import NutritionTableDetector
from crop import crop_img

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = ap.parse_args()


    obj = NutritionTableDetector()
    image = Image.open(args.image)
    boxes, scores, classes, num  = obj.get_classification(image)
    width, height = image.size
    print(scores)

    ymin = boxes[0][0][0]*height
    xmin = boxes[0][0][1]*width
    ymax = boxes[0][0][2]*height
    xmax = boxes[0][0][3]*width

    # print(xmin, ymin, xmax, ymax, scores[0][0])

    coords = (xmin, ymin, xmax, ymax)

    cropped_image = crop_img(image, coords, "./")
    cropped_image.show()

if __name__ == '__main__':
    main()