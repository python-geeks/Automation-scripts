from PIL import Image,ImageEnhance
import face_recognition
from resizeimage import resizeimage
# Load the jpg file into a numpy array
def extract_count(gpath,epath,filename):
	image = face_recognition.load_image_file(gpath)
	face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=0)
	count=len(face_locations)
	# Portrait image to landscape conversion
	if count==0:
	    img=Image.open(gpath)
	    l=img.size
	    m=max(l)
	    #img=resizeimage.resize_crop(img,[m,m])
	    img.save(gpath,img.format)
	    out=Image.open(gpath)
	    out=out.rotate(270)
	    out.save(gpath)
	    image = face_recognition.load_image_file(gpath)
	    face_locations = face_recognition.face_locations(image)
	    count=len(face_locations)
	if count>0:
	    print("I found ",count," face(s) in this photograph")
	    i=0
	    for face_location in face_locations:
		    i=i+1
		    # Print the location of each face in this image
		    top, right, bottom, left = face_location
		    # You can access the actual face itself like this:
		    face_image = image[top:bottom, left:right]
		    pil_image = Image.fromarray(face_image)
		    name =filename+ "-"+str(i) +'.jpg'
		    pil_image.save(epath+name)  
	return count 


