import cv2 
from datetime import date,datetime
import time
face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
#today=str(date.today())
def Capture():
    TIMER = int(5)
    
    # capture frames from a camera 
    cap = cv2.VideoCapture(0) 
    while True:
        ret, img = cap.read() 
        # convert to gray scale of each frames 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detects faces of different sizes in the input image 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces: 
            # To draw a rectangle in a face 
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w]
            area=x*y
            print(x)
            print("\n",y)
        # Display an image in a window
            print(area)
        cv2.imshow('image',img)
        cv2.waitKey(20) 
        if len(faces)>0: 
                prev = time.time() 

                while TIMER >= 0: 
                    ret, img = cap.read() 

                    # Display countdown on each frame 
                    # specify the font and draw the 
                    # countdown using puttext 
                    font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
                    cv2.putText(img, str(TIMER), 
                                (200, 250), font, 
                                7, (0, 255, 255), 
                                4, cv2.LINE_AA) 
                    cv2.imshow('img', img) 
                    cv2.waitKey(125) 

                    # current time 
                    cur = time.time() 

                    # Update and keep track of Countdown 
                    # if time elapsed is one second 
                    # than decrese the counter 
                    if cur-prev >= 1: 
                        prev = cur 
                        TIMER = TIMER-1

                else: 
                    ret, img = cap.read() 

                    # Display the clicked frame for 2 
                    # sec.You can increase time in 
                    # waitKey also 
                    cv2.imshow('image', img) 

                    # time for which image displayed 
                    cv2.waitKey(20) 

                    # Save the frame
                    resize = cv2.resize(img,(400,400))
                    cv2.imwrite("camera.jpg", resize)
                    print("image captured")
                    break
                
    
    # Close the window 
    cap.release() 
    
    # De-allocate any associated memory usage 
    cv2.destroyAllWindows() 
    return(0)
