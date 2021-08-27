#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
## Import the relevant files
from sys import exit as Die
try:
    import sys
    import cv2
    import numpy as np
    from colordetection import ColorDetector
except ImportError as err:
    Die(err)
 
#Variable Used For testing
cameratesting = False 
 
'''
Initialize the camera here
'''
#change cam_port if Video in Live feed is not being Displayed
cam_port         = 2 
#create a my camera object to read from
cam         = cv2.VideoCapture(cam_port)   
 
 
 
"""
    We are going to want to draw some stickers. In the solution
    we have 3 sets of stickers. Each set has 9 stickers to represent
    each sticker on any given face of the rubik's cube.
 
    The 'stickers' set of stickers are physical markers used to help the
    user see where to place the cube for color scanning.
 
    The 'current_stickers' set show which colors are currently being detected 
    for each position on the face.
 
    The 'preview_stickers' set shows the most recently recorded face.
    You can rescan a face if the preview does not match the actual colors
    on the face of the rubik's cube.
 
    These are the coordinates of each sticker for each set. Feel free to play
    with these values if you don't like the sticker placement.
 
    
"""
detector_stickers = [[200, 120], [300, 120], [400, 120],
                   [200, 220], [300, 220], [400, 220],
                   [200, 320], [300, 320], [400, 320]]
 
current_stickers = [[20, 20], [54, 20], [88, 20],
                   [20, 54], [54, 54], [88, 54],
                   [20, 88], [54, 88], [88, 88]]
 
recorded_stickers = [[20, 130], [54, 130], [88, 130],
                   [20, 164], [54, 164], [88, 164],
                   [20, 198], [54, 198], [88, 198]]
 
#Draws the 9 static stickers in the frame
def draw_detector_stickers(frame):
    for (x,y) in (detector_stickers):
        cv2.rectangle(frame, (x,y), (x+50, y+50), (255,255,255), 1)
    
#Draws the 9 detected stickers in the frame 
def draw_current_stickers(frame, state):
 
    for index,(x,y) in enumerate(current_stickers):
        cv2.rectangle(frame, (x,y), (x+32, y+32), ColorDetector.name_to_rgb(state[index]), -1)

#Draws the 9 Recorded stickers in the frame
def draw_recorded_stickers(frame, state):


    for index,(x,y) in enumerate(recorded_stickers):
        cv2.rectangle(frame, (x,y), (x+32, y+32), ColorDetector.name_to_rgb(state[index]), -1)
    
 
def color_to_notation(color):
    """
    Helper function for converting colors to notation
    used by solver.
    """
    notation = {
        'green'  : 'F',
        'white'  : 'U',
        'blue'   : 'B',
        'red'    : 'R',
        'orange' : 'L',
        'yellow' : 'D'
    }
    return notation[color]
 
def empty_callback(x):
    '''
    Empty function for callback when slider positions change. Need input x, this is the value 
    the slider has changed to.
    '''
    pass
 
def scan():
    """
    Opens up the webcam and scans the 9 regions in the center
    and show a preview.
 
    After hitting the space bar to confirm, the block below the
    current stickers shows the current state that you have.
    This is show every user can see what the computer took as input.
 
    :returns: dictionary
    """
 
    sides   = {}                            # collection of scanned sides
    preview = ['white','white','white',     # default starting preview sticker colors
               'white','white','white',
               'white','white','white']
    state   = [0,0,0,                       # current sticker colors
               0,0,0,
               0,0,0]
 
    defaultcal = {                          # default color calibration
                'white':[[179,67,255],[0,0,0]],
                'green':[[72,255,218],[47,61,21]],
                'red':[[179,255,240],[6,0,102]],
                'orange':[[179,255,255],[17,147,207]],
                'yellow':[[49,242,255],[18,61,211]],
                'blue':[[127,255,212],[82,72,51]]
                }
 
    colorcal  = {}                          # color calibration dictionary
    color = ['white', 'green', 'red', 'orange', 'yellow', 'blue']  # list of valid colors            
 
    cv2.namedWindow('default',0)
    # create trackbars here
    cv2.createTrackbar('H Upper','default',defaultcal[color[len(colorcal)]][0][0], 179, empty_callback)
    cv2.createTrackbar('S Upper','default',defaultcal[color[len(colorcal)]][0][1], 255, empty_callback)
    cv2.createTrackbar('V Upper','default',defaultcal[color[len(colorcal)]][0][2], 255, empty_callback)
    cv2.createTrackbar('H Lower','default',defaultcal[color[len(colorcal)]][1][0], 179, empty_callback)
    cv2.createTrackbar('S Lower','default',defaultcal[color[len(colorcal)]][1][1], 255, empty_callback)
    cv2.createTrackbar('V Lower','default',defaultcal[color[len(colorcal)]][1][2], 255, empty_callback)
 
    # Remember that the range for S and V are not 0 to 179

 
    colorcal = defaultcal
 
    # Creates a window named 'my_window_name' 
    cv2.createTrackbar('My track bar','my_window_name',125,255, empty_callback)
 
    while cameratesting:
        #--------------- Used for Testing ------------------------
        # Captures a frame of video from the camera object
        _,frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
        # create a mask
        # Bounds for HSV values we are interested in (Blue)
        lower_hsv = np.array([89,178,51])     #hmin,smin,vmin
        upper_hsv = np.array([118,255,194])   #hmax,smax,vmax
 
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv) 
        frame = cv2.bitwise_and(frame,frame, mask= mask)

        # Draw rectangle on the frame
        cv2.rectangle(frame, (200,200), (250, 250), (255,0,0), 2) 
 
        # -1 borderwidth is a fill
        cv2.rectangle(frame, (300,200), (350, 250), (0,0,255), -1)
 
        # Note the construction of a rectangle
        # arg1 = frame to draw on
        # arg2 = x,y coordinates of the rectangle's top left corner
        # arg3 = x,y coordinates of the rectangle's bottom right corner
        # arg4 = r,g,b values
        # arg5 = borderwidth  => width of the border or make a fill using -1
 
        # cv2.rectangle(frame, (xtop_left,ytop_left), (xbot_right,ybot_right), (r,g,b), borderwidth)
 
        # Displays the frame on the window we made
        value = cv2.getTrackbarPos('My track bar','my_window_name')
        print(value)
        cv2.imshow('my_window_name', frame) 
 
        # Sets the amount of time to display a frame in milliseconds
        key = cv2.waitKey(10)
 
 
 
 
    while not cameratesting:
 
        _, frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        key = cv2.waitKey(10)
 
        # init certain stickers.
        draw_detector_stickers(frame)
        draw_recorded_stickers(frame, preview)
 
        for index,(x,y) in enumerate(detector_stickers):
            roi          = hsv[y:y+32, x:x+32]              # extracts hsv values within sticker
            avg_hsv      = ColorDetector.median_hsv(roi)    # filters the hsv values into one hsv
            color_name   = ColorDetector.get_color_name(avg_hsv,colorcal) # extracts the color based on hsv
            state[index] = color_name                       # stores the color 
 
            # update when space bar is pressed.
            if key == 32:
                preview = list(state)
                draw_recorded_stickers(frame, state)         # draw the saved colors on the preview
                face = color_to_notation(state[4])          # convert the color to notation of the middle sticker and label this as the face
                notation = [color_to_notation(color) for color in state] # convert all colors to notation
                sides[face] = notation                      # update the face in the sides dictionary
 
        # show the new stickers
        draw_current_stickers(frame, state)                 # draw live sampling of face colors
 
        # append amount of scanned sides
        text = 'scanned sides: {}/6'.format(len(sides))
        cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA)
 
        # indicate the scanning instruction
        textInstruction = 'scan and rotate the cube with white on the top and green on the front (towards camera)'
        textInstruction2 = 'the color of center brick is used as the side identifier (since the center brick does not move)'
        textInstruction3 = 'you can scan as many times as you want'
        textInstruction4 = 'the program will overwrite the old scan when same side is detected, press esc key get the solution'
        cv2.putText(frame, textInstruction, (20, 600), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction2, (20, 620), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction3, (20, 640), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction4, (20, 660), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA)
 
        # quit on escape.
        if key == 27:
            break
 
        # show result
        cv2.imshow("default", frame)
 
        if key == 99: 
            colorcal = {}   
            while len(colorcal) < 6:
                _, frame = cam.read()
 
 
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                key = cv2.waitKey(10) & 0xff
 
                # hue upper lower
                hu = cv2.getTrackbarPos('H Upper','default')
                hl = cv2.getTrackbarPos('H Lower','default')
                # saturation upper lower
                su = cv2.getTrackbarPos('S Upper','default')
                sl = cv2.getTrackbarPos('S Lower','default')
                # value upper lower
                vu = cv2.getTrackbarPos('V Upper','default')
                vl = cv2.getTrackbarPos('V Lower','default')
                print("H upper", hu)
                print("H Lower", hl)
                print("S upper", su)
                print("S Lower", sl)
                print("V upper", vu)
                print("V Lower", vl)

 
                if color[len(colorcal)] == 'red' or color[len(colorcal)] == 'orange':
                    lower_hsv = np.array([0,sl,vl])
                    upper_hsv = np.array([hl,su,vu])
                    mask1 = cv2.inRange(hsv, lower_hsv, upper_hsv)
                    lower_hsv = np.array([hu,sl,vl])
                    upper_hsv = np.array([179,su,vu])
                    mask2 = cv2.inRange(hsv, lower_hsv, upper_hsv)
                    mask = cv2.bitwise_or(mask1, mask2)
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    lower_hsv = np.array([hl,sl,vl])
                    upper_hsv = np.array([hu,su,vu])
                else:
                    lower_hsv = np.array([hl,sl,vl])
                    upper_hsv = np.array([hu,su,vu])
 
                    
                    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
                    res = cv2.bitwise_and(frame,frame, mask = mask)
 
                if key == 32:
                    defaultcal[color[len(colorcal)]] = [upper_hsv,lower_hsv]
                    colorcal[color[len(colorcal)]] = [upper_hsv,lower_hsv]
 
                    if(len(colorcal) < 6):
                        cv2.setTrackbarPos('H Upper','default',defaultcal[color[len(colorcal)]][0][0])
                        cv2.setTrackbarPos('S Upper','default',defaultcal[color[len(colorcal)]][0][1])
                        cv2.setTrackbarPos('V Upper','default',defaultcal[color[len(colorcal)]][0][2])
                        cv2.setTrackbarPos('H Lower','default',defaultcal[color[len(colorcal)]][1][0])
                        cv2.setTrackbarPos('S Lower','default',defaultcal[color[len(colorcal)]][1][1])
                        cv2.setTrackbarPos('V Lower','default',defaultcal[color[len(colorcal)]][1][2])
 
                if(len(colorcal) < 6):
                    text = 'calibrating {}'.format(color[len(colorcal)])
                cv2.putText(res, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
 
                cv2.imshow("default", res)
                # quit on escape key.
                if key == 27:
                    break
 
    cam.release()
    cv2.destroyAllWindows()
    return sides if len(sides) == 6 else False
 
 