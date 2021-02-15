import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

HEIGHT = 300
WIDTH = 300

filename = ""
global img
global load
global render

def generateOBJ(filename):
    filenamea = '"' + filename + '"'
    cmd = "python 5_landmark_detection.py --shape-predictor shape_predictor_68_face_landmarks.dat --image " + filenamea
    imma = os.path.basename(filename)
    img = os.path.splitext(imma)[0]
    abel = tk.Label(root, bg = 'green', fg = 'blue', text = "DONE LOADING: " + str(img))
    abel.pack()
    os.system(cmd)
    os.system("python main.py")
    # cmd2 = '"' + str(os.getcwd()) + "\\output\\" + str(img) + "._mesh.obj" '"'
    # os.system(cmd2)
    cmd33 = "python convert.py --input " + '"' + "output/" + str(img) + "._mesh.obj" + '"' + " --output " + '"' + "ply_output/" + str(img) + "PLY.ply" + '"'
    print(cmd33)
    os.system(cmd33)

    f = open("img.txt", "w")
    f.write(str(img))
    f.close()

    os.system('blender --background --python blend.py')
    cmd2 = '"' + str(os.getcwd()) + "\\final_output\\" + str(img) + "_final.ply" '"'
    os.system(cmd2)
    # abel1 = tk.Label(root, bg = 'green', fg = 'red', text = cmd2)
    # abel1.pack()

def fileDialog():
    filename = filedialog.askopenfilename(initialdir = "", title = "Select Image File")
    load = Image.open(filename)
    if load.size[0] > load.size[1]:
        load = load.resize((300, 200), Image.ANTIALIAS)    
    else:
        load = load.resize((200, 300), Image.ANTIALIAS)    
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x = 0, y = 0)
    button2 = tk.Button(root, text="Generate OBJ", font=40, command=lambda:generateOBJ(filename))
    button2.pack(anchor = 'center')


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Browse jpg file", font=40, command=lambda:fileDialog())
button.place(relx = 0.5, rely = 0.5, anchor = 'center')


root.mainloop()