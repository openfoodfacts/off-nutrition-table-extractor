# off-nutrition-table-extractor

This repository shows how we are using the SSD model to detect the nutrition tables in images. The provided Jupyter Notebook shows how we can use the pre-trained graph to detect the tables in the product images.
Before running the notebook, install the object detection model from the [Tensorflow Github Repository](https://github.com/tensorflow/models).

The work is going on in this repository and until now, we have extracted the nutritional facts from a table but the results are preliminary.

To detect the table Single Shot Detector (SSD) object detection model is used which is trained on Tensorflow Object Detection API. The text detection is done using the [text-detection-ctpn](https://github.com/eragonruan/text-detection-ctpn) which uses fast-rcnn to detect text. In the future we will update it to a faster text detection model. For the text recognition, we are using Tesseract OCR.

## Requirements
If you find any other dependency required during the run, do raise an issue and inform there. 
```
1. Tensorflow
2. OpenCV
3. Pillow
4. Numpy
5. Tesseract v4.0
6. Pytesseract
```
## How to test your image
- Download the frozen model for ctpn from [here](https://github.com/eragonruan/text-detection-ctpn/releases/download/untagged-48d74c6337a71b6b5f87/ctpn.pb).
- Save the model to `./data`.
- Make a directory named test_images and put the images in that folder.
- run `python detection.py -i [IMAGE-PATH]`