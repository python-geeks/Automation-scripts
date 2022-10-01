import cv2


def colour_to_bw(original_image_path, output_path):
    '''
    Function to convert colour image to black and white
    '''
    original_image = cv2.imread(original_image_path)
    gray_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    thresh = 128
    img_bw = cv2.threshold(gray_img, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(output_path + 'final_image.png', img_bw)
