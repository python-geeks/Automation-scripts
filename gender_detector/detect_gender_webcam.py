from keras.preprocessing.image import img_to_array
from keras.models import load_model
import os
from keras.utils import get_file
import numpy as np
import cv2
import cvlib as cv

# load model
dwnld_link = "https://github.com/arunponnusamy/cvlib/releases/download/v0.2.0/gender_detection.model"
model_path = get_file("gender_detection.model", dwnld_link, cache_subdir="pre-trained", cache_dir=os.getcwd())

model = load_model(model_path)
# open_webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

classes = ['man' , 'woman']

# loop through frames
while webcam.isOpened():
    # read frame from webcam
    status, frame = webcam.read()

    if not status:
        print("Could not read frame")
        exit()
    # apply face detection
    face, confidence = cv.detect_face(frame)

    print(face)
    print(confidence)

    # loop through detected faces
    for idx, f in enumerate(face):
        # get corner points of face rectangle
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # draw rectangle over face
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

        # crop the detected face region
        face_crop = np.copy(frame[startY:endY, startX:endX])

        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue

        # preprocessing for gender detection model
        face_crop = cv2.resize(face_crop, (96, 96))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)

        # apply gender detection on face
        conf = model.predict(face_crop)[0]
        print(conf)
        print(classes)

        # get label with max accuracy
        idx = np.argmax(conf)
        label = classes[idx]
        label = "{}: {:.2f}%".format(label, conf[idx] * 100)
        Y = startY - 10 if startY - 10 > 10 else startY + 10
        # write label and confidence above face rectangle
        cv2.putText(frame, label, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    # display output
    cv2.imshow("gender detection", frame)
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release resources
webcam.release()
cv2.destroyAllWindows()
