import face_recognition.api as face_recognition
from PIL import Image
from resizeimage import resizeimage
import os,shutil
import json
def Encodings():
    project=os.getcwd()+"/"
    default=project+"images/"
    opath=str(default+"original/")
    erpath=str(default+"error/")
    jsonpath=str(default+"/original.json")
    dict1={}
    f=open(jsonpath,"w")
    error_image_name=[]
    for filename in os.listdir(opath):
        sublist=[]
        filename=str(filename)
        sublist.append(filename)
        imgpath=opath+filename
        image=face_recognition.load_image_file(imgpath)
        image_encoding=face_recognition.face_encodings(image,num_jitters=100)
        if len(image_encoding)<=0:
            img=Image.open(imgpath)
            l=img.size
            m=max(l)
            img=resizeimage.resize_crop(img,[m,m])
            img.save(imgpath,img.format)
            out=Image.open(imgpath)
            out=out.rotate(270)
            out.save(imgpath)
            image = face_recognition.load_image_file(imgpath)
            image_encoding=face_recognition.face_encodings(image,num_jitters=100)
        if len(image_encoding)>0:
            image_encoding=image_encoding[0]
            fname=filename.split(".")
            dict1.update({fname[0]:list(image_encoding)})
        else:
            shutil.move(opath+filename,erpath)
            error_image_name.append(fname[0])
            print("Error! Please retake the photo",filename)
    d=json.dumps(dict1)
    f.write(d)
return error_image_name
Encodings()



