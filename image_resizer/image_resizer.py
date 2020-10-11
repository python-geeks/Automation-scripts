import cv2
import os

# std in of image path and use opencv to read image
# and output current image ratio
while True:
    img_path = str(input('Enter the image path: '))
    img = cv2.imread(img_path)
    if img is None:
        print(
            'Directory or file is not vaild,' +
            ' please enter a valid file directory ...')
    else:
        break

original_width = img.shape[0]
original_height = img.shape[1]
print(f'Current image ratio is {original_width} x {original_height}')

# std in of new image ratio and file name
while True:
    try:
        resized_width = int(input('Enter the new width: '))
        resized_height = int(input('Enter the new height: '))
        break
    except Exception:
        print('Width and height need to be inegter, please enter again ...')

new_file = str(input('Enter new file name: '))

# Export new resized image onto the same dir as image_resizer.py.
new_img = cv2.resize(img, (resized_width, resized_height))
cv2.imwrite(f'{os.path.dirname(__file__)}/{new_file}.jpeg', new_img)
