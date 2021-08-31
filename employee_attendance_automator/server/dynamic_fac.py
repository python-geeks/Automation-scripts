import face_recognition.api as face_recognition
import os,shutil
import json
import numpy
from PIL import Image
from datetime import date,datetime
def match(current_img,temppath,erpath,jsonpath,excelpath):
    now = datetime.now()
    time=str(now.strftime("%I:%M %p"))
    data = open(jsonpath,"r")
    n=data.read()
    originallist=json.loads(n)
    for i in originallist:
        originallist[i]=numpy.asarray(originallist[i])
    l=[]
    
    for a in range(0,2):
        #extracted images encoding
        extractedlist=[]
        for filename in os.listdir(temppath):
            sublist=[]
            filename=str(filename)
            sublist.append(filename)
            file_path=temppath+filename
            image=face_recognition.load_image_file(file_path)
            image_encoding=face_recognition.face_encodings(image,num_jitters=5)
            if len(image_encoding)>0:
                image_encoding=image_encoding[0]
                sublist.append(image_encoding)
                extractedlist.append(sublist)
            else:
                shutil.move(temppath+filename,erpath)
                print("Error! Please retake the photo",filename)
        for key in originallist:
            rollno=key[0:20]
            if rollno in l:
                continue
            for esublist in extractedlist:
                oimg=originallist[key]
                eimg=esublist[1]
                result=face_recognition.compare_faces([oimg],eimg,tolerance=0.415)
                if result[0]== True:
                    print("Both are matched ",rollno,esublist[0])
                    os.remove(temppath+esublist[0])
                    l.append(rollno)
                    extractedlist.remove(esublist)
                    break
    for temp_img in os.listdir(temppath):
        os.remove(temppath+str(temp_img))
    for err_img in os.listdir(erpath):
        os.remove(erpath+str(err_img))
    return l



