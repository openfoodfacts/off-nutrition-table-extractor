# Install process on Debian Stretch (YMMV)

### nutrition table detection
```
git clone git@github.com:openfoodfacts/off-nutrition-table-extractor.git
git clone git@github.com:tensorflow/models.git
cd off-nutrition-table-extractor
ln -s ../models/research/object_detection object_detection
sudo apt-get install python3-pip
sudo python3 -m pip install matplotlib
sudo python3 -m pip install tensorflow
sudo python3 -m pip install PIL
sudo python3 -m pip install Pillow
protoc object_detection/protos/*.proto --python_out=.
mkdir test_images
ls test_images
jupyter notebook
```

### nutrition table analysis
```
sudo python3 -m pip install opencv-python
sudo python3 -m pip install pytesseract
sudo python3 -m pip install easydict
cd data
wget https://github.com/eragonruan/text-detection-ctpn/releases/download/untagged-48d74c6337a71b6b5f87/ctpn.pb
cd ..
python3 detection.py -i test_images/9.jpg
```

### tesseract dictionary optimisation
```
combine_tessdata -u /usr/share/tesseract-ocr/tessdata/eng.traineddata ../tesseract_bckp/eng
wordlist2dawg data/big.txt eng.word-dawg ../tesseract_bckp/eng.unicharset
sudo combine_tessdata -o /usr/share/tesseract-ocr/tessdata/eng.traineddata eng.word-dawg
```

### to do: tesseract training
see for instance http://www.dullroar.com/training-tesseract.html
