import os

f = open("img.txt", "r")
filer = str(f.read())
f.close()

cmd1 = 'python 68_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image render_images/' + str(filer) + '.jpg'
cmd2 = 'python 68_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image render_images/head.jpg'

os.system(cmd1)
os.system(cmd2)