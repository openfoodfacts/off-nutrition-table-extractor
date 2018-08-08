
# off-nutrition-table-extractor

This repository shows how we are using the SSD model to detect the nutrition tables in images. The provided Jupyter Notebook shows how we can use the pre-trained graph to detect the tables in the product images.
Before running the notebook, install the object detection model from the [Tensorflow's Github Repository](https://github.com/tensorflow/models).

![Table detection](/data/images/table_detection.jpeg)

To detect the table, Single Shot Detector (SSD) object detection model is used which is trained on Tensorflow Object Detection API. The text detection is done using the [text-detection-ctpn](https://github.com/eragonruan/text-detection-ctpn) which uses fast-rcnn to detect text. In the future we will update it to a faster text detection model. For the text recognition, we are using Tesseract OCR.

## Requirements
The code is compatible with Python 3.0+. If you find any other dependency required during the execution, do raise an issue and inform there. 
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
- Save the model in `./data` repository.
- Make a directory named test_images and put the images in that folder.
- run `python detection.py -i [IMAGE-PATH]`.

## Future Work
With GSoC 2018 being the kickstarter of this project, we are just getting started. There are a lot of things to do that we are going to do
* Improving the spacial mapping algorithm. 
* Training and using a faster and more accurate text detection model than the currently used fast-rcnn model.
*  Creating a bigger nutritional table dataset and training that on a recent and bleeding edge object detection model to improve the accuracy.
