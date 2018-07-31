from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import pickle
import cv2
import os

args = {'model': 'fruitnet.model', 'labelbin': 'lb.pickle', 'image': 'None'}

imagePath = input('Please enter the path of an image of a fruit: ').strip().replace("'",'')
args['image']=imagePath

image = cv2.imread(args["image"])
output = image.copy()
 
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())
 
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

filename = args["image"][args["image"].rfind(os.path.sep) + 1:]

label = "{}: {:.2f}%".format(label, proba[idx] * 100)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

print("[INFO] {}".format(label))
cv2.imshow("Output", output)
print('Press a button to exit!')
cv2.waitKey(0)
