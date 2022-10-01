# Importing Image class from PIL module
from PIL import Image


def crop():
    # Taking the image path as an input
    file_path = str(input('Enter the image path (absolute path): '))

    # Opening image with an RGB mode, works only with jpeg/jpg formats
    img = Image.open(file_path, mode="r")

    # Calculating size of the original image in pixels for reference
    width, height = img.size
    print('the old width is: ' + str(width) + ' and the old height is: ' + str(height))

    # Taking left, top, right, bottom points for the cropped image as input
    # Image pixels coorginate grid: X increases from left to right, Y increases from top to bottom
    left = int(input('Enter the new left point: '))
    top = int(input('Enter the new top point: '))
    right = int(input('Enter the new right point: '))
    bottom = int(input('Enter the new bottom point: '))

    # Crop the image with specified points
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image as a separate image named "cropped_img.jpg" under a specified directory
    cropped_image_path = str(input('Enter the path to save the cropped image (absolute path): '))
    cropped_img.save(f"{cropped_image_path}/cropped_img.jpg")

    # Show the image in the image viewer
    cropped_img.show()


if __name__ == '__main__':
    crop()
