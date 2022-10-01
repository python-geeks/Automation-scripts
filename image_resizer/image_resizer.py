import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f',
    type=str,
    help='The file path of target image. '
    + 'ex. /home/user/example.jpeg.\nDefault value is "demo.jpeg"',
    default=os.path.dirname(__file__) + '/demo.jpeg'
)
parser.add_argument(
    '-rw',
    type=int,
    help='The new width to be resize.\nDefault value is "640"',
    default=640
)
parser.add_argument(
    '-rh',
    type=int,
    help='The new height to be resize.\nDefault value is "480"',
    default=480
)
parser.add_argument(
    '-n',
    type=str,
    help='The file name.\n'
    + 'Default value is current {current file name}_{rw}x{rh}.jpeg',
)

args = parser.parse_args()
img_path = args.f
resized_width = args.rw
resized_height = args.rh

if args.n:
    new_file = args.n
else:
    new_file = (lambda x: x.split('/')[-1].split('.')[0])(args.f)
    new_file += f'_{args.rw}x{args.rh}.jpeg'

# If path is invalid, ask user to input image path again
# and output current image ratio
while True:
    img = cv2.imread(img_path)
    if img is None:
        print(
            'Directory or file is not valid,'
            + ' please enter a valid file directory ...')
        img_path = str(input('Enter the image path again (absolute path): '))
    else:
        break

original_width = img.shape[0]
original_height = img.shape[1]
print(f'Current image ratio is {original_width} x {original_height}')

# If stdin rw & rh value larger than original img size
# ask user to input again.
while True:
    try:
        if resized_width > original_width:
            raise RuntimeError(
                'Resized width must be no larger than original width'
                + f' (< {original_width})'
            )
        if resized_height > original_height:
            raise RuntimeError(
                'Resized height must be no larger than original height'
                + f' (< {original_height})'
            )
        break
    except RuntimeError as err:
        print(err)
        resized_width = int(input('Enter the new width: '))
        resized_height = int(input('Enter the new height: '))

# Export new resized image onto the same dir as image_resizer.py
new_img = cv2.resize(img, (resized_width, resized_height))
cv2.imwrite(f'{os.path.dirname(__file__)}/{new_file}', new_img)

comment = f'Resized image ({resized_width} x {resized_height})'
comment += ' is now stored on the directory below:'
comment += f'\n{os.path.dirname(__file__)}/{new_file}'

print(comment)
