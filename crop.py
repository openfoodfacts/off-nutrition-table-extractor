import argparse
# from PIL import Image
import cv2

def crop(image_obj, coords, saved_location, extend_ratio=0, SAVE=False):
    """
    @param image_path: The image object to be cropped
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    @param extend_ratio: The value by which the bounding boxes to be extended to accomodate the text that has been cut
    @param SAVE: whether to save the cropped image or not
    """
    nx = image_obj.shape[1]
    ny = image_obj.shape[0]

    modified_coords = (
        int(coords[0]-extend_ratio*nx), 
        int(coords[1]-extend_ratio*ny), 
        int(coords[2]+extend_ratio*nx), 
        int(coords[3]+extend_ratio*ny)
    )
    # cropped_image = image_obj.crop(modified_coords)
    cropped_image = image_obj[modified_coords[1]:modified_coords[3], modified_coords[0]:modified_coords[2]]

    if(SAVE):
        cv2.imwrite(saved_location, cropped_image)


    return cropped_image

#main function to test different functions independently
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    ap.add_argument("-c", "--coords", nargs="+", type = int, required=True, help="path to the input image")
    args = ap.parse_args()

    coords = tuple(args.coords)
    saved_location = './'
    image = cv2.imread(args.image)
    crop_img(image, coords, saved_location)

if __name__ == '__main__':
    main()