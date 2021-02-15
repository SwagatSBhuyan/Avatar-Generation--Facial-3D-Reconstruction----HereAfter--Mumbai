# Facial-Feature-Detection-and-3D-Reconstruction-with-Texture-Generation

This repository has been built to detect facial features using the standard 68 landmark data file and will hance generate a 5 landmark coordinate system that will eventually be used by the 3D reconstruction scripts to generate an object file with built-in vector textures.

The Avatar Generation SDK was built internally, through various reconstruction and face detection repositories already available in Github, under fair use policies and guidelines. Many files, such as various morph files, the network folder present in the directory, and BFM files for texture generation are protected under copyright guidelines, and hence must be looked upon carefully before use. Otherwise, Citations have been provided by our personal github repository to replicate the final Avatar generation SDK repository. All the relevant links are provided in this documentation.


## System Requirements

Project uses below python packages:

- __NumPy__ : A fundamental package for scientific computing with Python.

- __OpenCV__ : A library of Python bindings designed to solve computer vision problems.

- __dlib__ : A toolkit for making real world machine learning and data analysis applications.

- __imutils__ : A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.

- __Reconstruction__ : Reconstructions can be done on both Windows and Linux. However, we suggest running on Linux because the rendering process is only supported on Linux currently. If you wish to run on Windows, you have to comment out the rendering part.

- __scipy__ 

- __pillow__

- __Tensorflow 1.4 ~ 1.12__

- __Basel Face Model 2009 (BFM09)__ : Expression Basis (transferred from Facewarehouse by Guo et al.). The original BFM09 model does not handle expression variations so extra expression basis are needed.

- __tf mesh renderer__ : We use the library to render reconstruction images. Install the library via pip install mesh_renderer. Or you can follow the instruction of tf mesh render to install it using Bazel. Note that current rendering tool does not support tensorflow version higher than 1.13 and can only be used on Linux.

- __BLENDER__ : Blender is a free and open-source 3D computer graphics software toolset used for creating animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games.
>NOTE: Both the Blender environment Software and the pip Blender Package Module will be required for functioning of the rendered 3d face reconstructions.
```
pip install blender
```


## Server Installation

A server side installation would make sense as the dependencies are very operating system / device specific. A simple AWS ec2 instance connected with Lambda or a Google Cloud Server can be set up, and above dependencies can be integrated.


1. Clone the repository:
```
git clone https://github.com/SwagatSBhuyan/Avatar-Generation--Facial-3D-Reconstruction----HereAfter--Mumbai.git
cd Avatar-Generation--Facial-3D-Reconstruction----HereAfter--Mumbai
```

2. Download and install Python 3.8 or Anaconda 4 on your system as per your operating system. [Download Anaconda 4](https://www.anaconda.com/products/individual)
> It is crucial to have only upto Python 3.8 for the TensorFlow codes to work, hence it is strongly advised to install Python along with Anaconda. 
The given setup.exe or setup.py files have been built with options to download and install the same

3. Install the required python packages needed to run the scripts. Use the given setup.py or setup.exe in the dedicated server to install the dependencies.
> To install special dependencies like dlib into an online server, it is advised to separately seek out documentations, as their installations also require other pre-built dependencies and builders like Visual Studio.
> Make sure to turn down option to extract data.rar manually.

4. Download the Basel Face Model. Due to the license agreement of Basel Face Model, you have to download the BFM09 model after submitting an application on its [home page](https://faces.dmi.unibas.ch/bfm/bfm2019.html). After getting the access to BFM data, download "01_MorphableModel.mat" and put it into ```./BFM``` subfolder.

5. Download the Expression Basis provided by [Guo et al](https://github.com/Juyong/3DFace). You can find a link named "CoarseData" in the first row of Introduction part in their repository. Download and unzip the Coarse_Dataset.zip. Put "Exp_Pca.bin" into ```./BFM``` subfolder. The expression basis are constructed using Facewarehouse data and transferred to BFM topology.

6. Download the trained [reconstruction network](https://drive.google.com/file/d/176LCdUDxAj7T2awQ5knPMPawq5Q2RUWM/view), unzip it and put "FaceReconModel.pb" into ```./network``` subfolder.

7. The directory should now have a ./main_pipeline.exe file ready for execution. 
> If not, simply run the ./main_pipeline.py script file in your server, to open the dedicated GUI to browse a JPG image and generate its 3D Face Reconstructed obj file for further rendering in Unreal.
```
python ./main_pipeline.py
```
8. Check the ./output folder to acquire the generated .obj files with built-in vector textures, that can be rendered using softwares, such as meshlab.


## Citation
Please cite the following paper if this model helps your research:
```
@inproceedings{deng2019accurate,
    title={Accurate 3D Face Reconstruction with Weakly-Supervised Learning: From Single Image to Image Set},
    author={Yu Deng and Jiaolong Yang and Sicheng Xu and Dong Chen and Yunde Jia and Xin Tong},
    booktitle={IEEE Computer Vision and Pattern Recognition Workshops},
    year={2019}
}
```

## References
1. @microsoft/Deep3DFaceReconstruction Deep 3D face Reconstruction [GitHub](https://github.com/microsoft/Deep3DFaceReconstruction)
2. @raviranjan0309/Detect-Facial-Features Detect Facial Features [GitHub](https://github.com/raviranjan0309/Detect-Facial-Features)
2. @nabeel3133/file-converter-.obj-to-.ply [GitHub](https://github.com/nabeel3133/file-converter-.obj-to-.ply)


