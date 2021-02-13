from collections import OrderedDict
import imutils
import numpy as np
import os
import cv2
import dlib
import argparse
import shutil
from shutil import copyfile



facial_features_cordinates = {}

FACIAL_LANDMARKS_INDEXES = OrderedDict([
    ("Mouth", (48, 68)),
    ("Right_Eyebrow", (17, 22)),
    ("Left_Eyebrow", (22, 27)),
    ("Right_Eye", (36, 42)),
    ("Left_Eye", (42, 48)),
    ("Nose", (27, 35)),
    ("Jaw", (0, 17))
])

leftEye = []
rightEye = []
nose = []
leftMouth = []
rightMouth = []

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


def shape_to_numpy_array(shape, dtype="int64"):
    coordinates = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)
    return coordinates

def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):
    overlay = image.copy()
    output = image.copy()

    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
                  (168, 100, 168), (158, 163, 32),
                  (163, 38, 32), (180, 42, 220)]

    for (i, name) in enumerate(FACIAL_LANDMARKS_INDEXES.keys()):
        (j, k) = FACIAL_LANDMARKS_INDEXES[name]
        pts = shape[j:k]
        facial_features_cordinates[name] = pts
        if name == "Jaw":
            for l in range(1, len(pts)):
                ptA = tuple(pts[l - 1])
                ptB = tuple(pts[l])
                cv2.line(overlay, ptA, ptB, colors[i], 2)
        else:
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)

    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    return output

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)

for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_numpy_array(shape)
    output = visualize_facial_landmarks(image, shape)
    #cv2.imshow("Image", output)
    cv2.waitKey(0)

from mtcnn import MTCNN
import cv2

img132 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
detector = MTCNN()
kp = detector.detect_faces(img132)
print(kp[0]['keypoints'])

leftEye = kp[0]['keypoints']['left_eye']
rightEye = kp[0]['keypoints']['right_eye']
nose = kp[0]['keypoints']['nose']
leftMouth = kp[0]['keypoints']['mouth_left']
rightMouth = kp[0]['keypoints']['mouth_right']


# for (i, name) in enumerate(FACIAL_LANDMARKS_INDEXES.keys()):
#         (j, k) = FACIAL_LANDMARKS_INDEXES[name]
#         pts = shape[j:k]
#         facial_features_cordinates[name] = pts

#         if name=="Right_Eyebrow":
#             continue
#         if name=="Left_Eyebrow":
#             continue
#         if name=="Jaw":
#             continue

#         a = 0
#         b = 0
#         for l in range(0, len(pts)):
#             (a, b) = (a, b) + pts[l]
#         a = a/len(pts)
#         b = b/len(pts)
#         print(name, ": ", a, b)

#         if name=="Mouth":
#             (c, d) = pts[0]
#             (e, f) = pts[0]
#             for l in range(0, len(pts)):
#                 (x, y) = pts[l]
#                 if x > c:
#                     c = x
#                 if x < e:
#                     e = x
#             leftMouth = (e, b)
#             rightMouth = (c, b)

#         if name=="Right_Eye":
#             leftEye = (a, b)
#         if name=="Left_Eye":
#             rightEye = (a, b)
#         if name=="Nose":
#             (g, h) = pts[0]
#             for k in range(0, len(pts)):
#                 (u, v) = pts[k]
#                 if u > g:
#                     h = v
#             nose = (a, h)


print("\nleftEye: ", leftEye, "\nrightEye: ", rightEye, "\nNose: ", nose, "\nleftMouth: ", leftMouth, "\nrightMouth: ", rightMouth)

imma = os.path.basename(args["image"])
img = os.path.splitext(imma)[0]
print("\n\nimage: ", img)

file1 = open("input/" + img + ".txt", "w")
file1.write(str(leftEye[0]) + "\t" + str(leftEye[1]) + "\n")
file1.write(str(rightEye[0]) + "\t" + str(rightEye[1]) + "\n")
file1.write(str(nose[0]) + "\t" + str(nose[1]) + "\n")
file1.write(str(leftMouth[0]) + "\t" + str(leftMouth[1]) + "\n")
file1.write(str(leftMouth[0]) + "\t" + str(leftMouth[1]) + "\n")

file1.close()

shutil.copy2('./images/' + img + '.jpg', './input')