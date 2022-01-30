import random
from os import path
import sys
from PIL import Image, ImageDraw, ImageFont

try:
    int(sys.argv[3])
    int(sys.argv[4])
    if len(str(sys.argv[2])) != 1:
        raise ValueError
except ValueError: 
    print('Must input correct parameters')
    print('Ex:\n python3 "letter_img.py" "file_name" "letter" "width" "height"',
            '\n\n python3 "letter_img.py" letter l 500 500')


width = int(sys.argv[3])
height = int(sys.argv[4])

color =(random.randint(0,255), random.randint(0,255), random.randint(0,255))

if not path.exists(str(sys.argv[1]) + '.png'):
    image = Image.new('RGB', (width, height), color)
    image.save(str(sys.argv[1]) + '.png' , "PNG")
    state = 'created'
else:
    image = Image.open(str(sys.argv[1]) + '.png')
    ImageDraw.Draw(image).rectangle([(0,0),width, height], fill = color )
    image.save(str(sys.argv[1]) + '.png' , "PNG")
    state = 'updated'
    



draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", width, encoding="unic")
w, h = font.getsize(str(sys.argv[2]))
draw.text(((width-w)/2, (height-h)/2), str(sys.argv[2]), font=font)

image.save(str(sys.argv[1]) + '.png' , "PNG")


print('Successfully ' + state + ' file.')
