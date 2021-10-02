
# flake8: noqa
import cv2
import numpy as np
import os


shapes = {}

def scan_image(img_file_path):

    global shapes
    img = cv2.imread(img_file_path)

    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, timg = cv2.threshold(gimg, 254, 255, cv2.THRESH_BINARY)
    co, _ = cv2.findContours(timg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    shapes1 = {}
    for i in range(1, len(co)):
        app = cv2.approxPolyDP(co[i], 0.01 * cv2.arcLength(co[i], True), True)
        M = cv2.moments(co[i])
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
        Area = round(cv2.contourArea(co[i]), 1)

        colorarr = img[cY, cX]
        fincol = 'NA'
        B = colorarr[0]
        G = colorarr[1]
        R = colorarr[2]

        if (R > G):
            if (B > R):
                fincol = 'blue'
            else:
                fincol = 'red'
        else:
            if (B > G):
                fincol = 'blue'
            else:
                fincol = 'green'
        if (len(app) == 3):
            shapes1['Triangle'] = [fincol, Area, cX, cY]
        elif (len(app) == 4):
            ptsarr = app.ravel()

            x1 = ptsarr[0]
            y1 = ptsarr[1]
            x2 = ptsarr[2]
            y2 = ptsarr[3]
            x3 = ptsarr[4]
            y3 = ptsarr[5]
            x4 = ptsarr[6]
            y4 = ptsarr[7]

            l1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
            l2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2)
            l3 = ((x4 - x3) ** 2 + (y4 - y3) ** 2)
            l4 = ((x4 - x1) ** 2 + (y4 - y1) ** 2)

            d1 = ((x3 - x1) ** 2 + (y3 - y1) ** 2)
            d2 = ((x4 - x2) ** 2 + (y4 - y2) ** 2)

            ap1 = float(l1) / l2
            ap2 = float(l2) / l3
            ap3 = float(l3) / l4
            ap4 = float(l4) / l1

            f = 0

            if (abs(x2 - x1) < 3 and abs(x3 - x4) < 3):
                f = 1
            if (abs(y2 - y1) < 3 and abs(y3 - y4) < 3):
                f = 1
            if (abs(x1 - x4) < 3 and abs(x2 - x3) < 3):
                f = 1
            if (abs(y1 - y4) < 3 and abs(y2 - y3) < 3):
                f = 1

            if ((x2 - x1) != 0 and (x3 - x4) != 0):
                sl1 = float(y2 - y1) / (x2 - x1)
                sl2 = float(y3 - y4) / (x3 - x4)
                if (sl2 != 0):
                    sl = abs(float(sl1) / sl2)
                    if (sl >= 0.9 and sl <= 1.1):
                        f = 1
            if ((x1 - x4) != 0 and (x2 - x3) != 0):
                sl1 = float(y1 - y4) / (x1 - x4)
                sl2 = float(y2 - y3) / (x2 - x3)
                if (sl2 != 0):
                    sl = abs(float(sl1) / sl2)
                    if (sl >= 0.9 and sl <= 1.1):
                        f = 1


            if ((ap1 >= 0.9 and ap1 <= 1.1) and (ap2 >= 0.9 and ap2 <= 1.1) and (ap3 >= 0.9 and ap3 <= 1.1) and (
                    ap4 >= 0.9 and ap4 <= 1.1)):
                if (float(d1) / d2 >= 0.9 and float(d1) / d2 <= 1.1):
                    shapes1['Square'] = [fincol, Area, cX, cY]
                else:
                    shapes1['Rhombus'] = [fincol, Area, cX, cY]
            elif ((float(l1) / l3 >= 0.9 and float(l1) / l3 <= 1.1) and (
                    float(l2) / l4 >= 0.9 and float(l2) / l4 <= 1.1)):
                shapes1['Parallelogram'] = [fincol, Area, cX, cY]
            elif (f):
                shapes1['Trapezium'] = [fincol, Area, cX, cY]
            else:
                shapes1['Quadrilateral'] = [fincol, Area, cX, cY]
        elif (len(app) == 5):
            shapes1['Pentagon'] = [fincol, Area, cX, cY]
        elif (len(app) == 6):
            shapes1['Hexagon'] = [fincol, Area, cX, cY]
        else:
            shapes1['Circle'] = [fincol, Area, cX, cY]

    shapes.clear()

    for key, value in sorted(shapes1.items(), key=lambda e: e[1][1], reverse=True):
        shapes[key] = value

    shapes1.clear()

    return shapes


if __name__ == '__main__':

    total_sam = 1

    while(total_sam != 0 ):

        curr_dir_path = os.getcwd()
        print('Currently working in '+ curr_dir_path)

        img_dir_path = curr_dir_path + '/Samples/'


        file_num = total_sam
        total_sam-=1
        img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

        if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
            print('\nFound Sample' + str(file_num) + '.png')

        else:
            print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
            exit()



        try:

            shapes = scan_image(img_file_path)
            print('*******************************')

            print('Total Shapes Found =' , len(shapes))

            for i , j  in shapes.items():
                print ( 'Shape Name:' , i )
                print('Color:', j[0])
                print('Area:', j[1])
                print('Location cX, cY:', j[2] , j[3])
                print('Color:', j[3])
                print('*******************************')




        except Exception:
            print('\n[ERROR] scan_image function is throwing an error.')
            exit()


