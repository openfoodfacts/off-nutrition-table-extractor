Important: Please have a look at the higher level issue in Robotoff: https://github.com/openfoodfacts/robotoff/issues/372
This is an old model and we have made progress since then.

# off-nutrition-table-extractor
This repository is the accumulation of all the work done during Google Summer of Code 2018.
- **Student**: Sagar Panchal
- **Github**: [sgrpanchal31](https://github.com/sgrpanchal31)
- **Organisation**: [Open Food Facts](https://world.openfoodfacts.org/)
- **Project**: [OCR on Nutritional Facts Table](https://summerofcode.withgoogle.com/projects/#6627107531128832)

## Technical Details
The pipeline is made up of three major parts namely table detection, text detection and OCR with post-processing.

### Table Detection
For detecting tables in an image, we are using the Single Shot Detector (SSD) object detection model. The model is trained on Tensorflow's Object Detection API. The provided Jupyter Notebook shows how we are using the pre-trained graph to detect tables in product images.
Before running the notebook, install the object detection model from the [Tensorflow's Github Repository](https://github.com/tensorflow/models).
![Table detection](/data/images/table_detection.jpeg)

### Text Detection and extraction
Text detection is done using the [text-detection-ctpn](https://github.com/eragonruan/text-detection-ctpn) which uses fast-rcnn to extract textual regions in the image. In future, we are planning to update it to a faster and more accurate text detection model.
![Text Detection](/data/images/text_detection.jpg)

### OCR and post-processing
For the text recognition, we are using Tesseract OCR. Every text box detected from the text detection step will be passed through the OCR and a raw string will be returned which is then passed throught many post processing steps that clean the string (through regular expressions) and rectify any spelling mistakes in the string (using the [symspell](https://github.com/wolfgarbe/SymSpell) spelling correction algorithm).

### Final Results
![Full pipeline detection](/data/images/final_result.jpg)
Output for the above image is given below:
```
Nutritional content = {
    'Dietary Fiber': (2.0, 'g'), 
    'Sugars': (9.0, 'g'),
    'Soluble Fiber': (1.0, 'g'), 
    'Monounsaturated Fat': (0.5, 'g'), 
    'Polyunsaturated Fat': (0.5, 'g'), 
    'Trans Fat': (0.0, 'g'), 
    'Other Carbohydrate': (11.0, 'g')
}
```

## Requirements
The code is compatible with Python 3.0+. If you find any other dependency required during the execution, do raise an issue and inform there. 
```
1. Tensorflow
2. OpenCV
3. Pillow
4. Numpy
5. Tesseract v4.0
6. Pytesseract
7. Django-2.0.5 (Only for API)
```

## How to test your image
- Download the frozen model for ctpn from [here](https://github.com/eragonruan/text-detection-ctpn/releases/download/untagged-48d74c6337a71b6b5f87/ctpn.pb).
- Save the model in `./nutrition_extractor/data` repository.
- Make a directory named `test_images` and put the images in that folder.
- run `python detection.py -i [IMAGE-PATH]` from inside nutrition_extractor folder.

## Planned functionality
- [x] Develop a table detection model to extract the region of interest (nutritional facts table) from images.
- [x] Crop the RoI from images and apply text detection pipeline to the region.
- [x] Pass every text blob through Tesseract OCR to extract the text.
- [x] Develop a post-processing method to clean the text and extract the nutritional label and its value form it.
- [ ] Create a spatial mapping algorithm to map the text blobs according to their location in the image. (Done but the accuracy is not upto the standards).

## Future Work
With GSoC 2018 being the kickstarter of this project, we are just getting started. There are a lot of things to do that we are going to do
* Improving the spatial mapping algorithm. 
* Training and using a faster and more accurate text detection model than the currently used fast-rcnn model.
* Creating a bigger nutritional table dataset and training that on a recent and bleeding edge object detection model to improve the accuracy.
* Developing a better image preprocessing algorithm to detect bold text.
* Implementing a method to unify the two models into one since the same calculations are being done twice in initial layers of the two models.
