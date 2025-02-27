# -*- coding: utf-8 -*-
"""image_dectection_yolov10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13zQ-ju1Kjl70w2y3CQvZkn3wdDiwcXJE
"""

from ultralytics import YOLOv10  # type: ignore

MODEL_PATH = '/content/yolov10/yolov10n.pt'
model = YOLOv10(MODEL_PATH)

IMG_PATH = 'vi_tri_duong_dan_anh' #type: ignore
result = model(source = IMG_PATH) [0]

result.save('/content/street-view-of-pham-ngu-lao-street--vietnam-921731936-5c353f9746e0fb000180251c.jpg')

#!pip install google-colab
import cv2 # type: ignore
from google.colab.patches import cv2_imshow # type: ignore # Import the Colab patch for cv2.imshow()
image = cv2.imread('/content/street-view-of-pham-ngu-lao-street--vietnam-921731936-5c353f9746e0fb000180251c.jpg')
cv2_imshow(image) # Use cv2_imshow instead of cv2.imshow

#!git clone https://github.com/THU-MIG/yolov10.git

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov10
#!pip install -q -r requirements.txt
#!pip install -e .

#!pip install --upgrade torch==2.3

#!pip install --upgrade torchvision==0.18

#!wget https://github.com /THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt

from google.colab import drive # type: ignore

# Create the directory where you want to mount Google Drive, use a Linux-style path
#!mkdir "/content/Safety_Helmet_Dataset"

# Mount Google Drive to the newly created directory
drive.mount('/content/Safety_Helmet_Dataset')

YAML_PATH = "/content/safety_helmet_dataset/data.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)

#!unzip -q '/content/Safety_Helmet_Dataset/MyDrive/Safety_Helmet_Dataset.zip' -d '/content/safety_helmet_dataset'

TRAINED_MODEL_PATH = '/content/yolov10/runs/detect/train5/weights/best.pt'
model = YOLOv10 ( TRAINED_MODEL_PATH )

model . val ( data = YAML_PATH ,
imgsz = IMG_SIZE ,
split ='test')