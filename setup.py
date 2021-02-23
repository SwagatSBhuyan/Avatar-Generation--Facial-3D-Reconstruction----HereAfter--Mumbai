import os
import webbrowser
import requests
import shutil

choice = 'NOOOO'
choice = input("Do you want to install Anaconda Python? [Y: Yes, else: No]\n")
if choice == 'y' or choice == 'Y' or choice == 'Yes' or choice == 'YES' or choice == 'yes' or choice == 'YeS' or choice == 'yES':
    url_anaconda = 'https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe'
    r_anaconda = requests.get(url_anaconda, allow_redirects=True)
    print("Downloading Anaconda")
    open('Anaconda3-2020.11-Windows-x86_64.exe', 'wb').write(r_anaconda.content)
    shutil.move('Anaconda3-2020.11-Windows-x86_64.exe', 'downloads/Anaconda3-2020.11-Windows-x86_64.exe')
    os.system('start Anaconda3-2020.11-Windows-x86_64.exe')

os.system('pip install opencv-python')
os.system('pip uninstall pyinstaller')
os.system('pip install numpy')
os.system('pip install cmake')
os.system('pip install argparse')
os.system('pip install json')
os.system('pip install dlib')
os.system('pip install blender')
os.system('pip install imutils')
os.system('pip install scipy')
os.system('pip install Pillow')
os.system('pip install pyunpack')
os.system('pip install pyinstaller')
os.system('pip install mtcnn')
os.system('pip install unrar')

choiceT = 'NOOOO'
choiceT = input("Do you want to install TensorFlow for Python 3.8? [Y: Yes, else: No]\n")
if choiceT == 'y' or choiceT == 'Y' or choiceT == 'Yes' or choiceT == 'YES' or choiceT == 'yes' or choiceT == 'YeS' or choiceT == 'yES':
    os.system('pip install tensorflow')

from pyunpack import Archive
# from unrar import rarfile

# webbrowser.open('https://faces.dmi.unibas.ch/bfm/bfm2019.html', new=2)

# webbrowser.open('https://drive.google.com/file/d/0B0A9UsiwtVTHY0p4em5qUzRISW8/view', new=2)

# webbrowser.open('https://drive.google.com/u/0/uc?id=176LCdUDxAj7T2awQ5knPMPawq5Q2RUWM&export=download', new=2)

# Archive('data.rar').extractall(os.getcwd())
rary = input("Do you want to automatically extract data.rar?[Y: Yes, else: No]\n")
if choiceT == 'y' or choiceT == 'Y' or choiceT == 'Yes':
    import patoolib
    patoolib.extract_archive("data.rar", outdir=os.getcwd())

os.system('pyinstaller.exe --onefile main_pipeline.py')

shutil.move('dist/main_pipeline.exe', 'main_pipeline.exe')

