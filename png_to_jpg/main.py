from PIL import Image
import os

project_root_path = os.path.dirname(os.path.abspath(__file__))

# open image in png format
img_png = Image.open(project_root_path + '/input/mario.png')

# converting image to RGB
rgb_im = img_png.convert('RGB')

# The image object is used to save the image in jpg format
rgb_im.save(project_root_path + '/output/mario.jpg')
