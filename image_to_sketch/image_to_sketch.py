import cv2

# Add the source file path here
image_source = "<img_source_path/img_name.jpg"
# Add the destination file path here
image_destination = "/img_destination_path/img_name.jpg"

img = cv2.imread(image_source)
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imwrite(image_destination, dst_gray)
print("Your Sketched image got saved in" + image_destination + "....")
