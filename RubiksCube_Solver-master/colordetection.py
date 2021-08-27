#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit as Die
try:
    import sys
    import numpy as np
except ImportError as err:
    Die(err)

class ColorDetection:

    def get_color_name(self, hsv, cal):
        """ Get the name of the color based on the hue.

        :returns: string
        """
        (h,s,v) = hsv
        for color in cal:
            if color == 'red' or color == 'orange':
                if (h < cal[color][1][0] or h > cal[color][0][0]) and s in range(cal[color][1][1],cal[color][0][1]) and v in range(cal[color][1][2],cal[color][0][2]):
                    return color
            elif h in range(cal[color][1][0],cal[color][0][0]) and s in range(cal[color][1][1],cal[color][0][1]) and v in range(cal[color][1][2],cal[color][0][2]):
                return color
        

        return 'white'

    def name_to_rgb(self, name):
        """
        Get the main RGB color for a name.

        :param name: the color name that is requested
        :returns: tuple
        """
        color = {
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
        }
        return color[name]

    def average_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        for y in range(len(roi)):
            if y % 10 == 0:
                for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        
                        if chunk[0] != 0:
                            h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
        h /= num
        s /= num
        v /= num
        return (int(h), int(s), int(v))

    def median_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = []
        s   = []
        v   = []
        num = 0
        for y in range(len(roi)):
            if y % 10 == 0:
                for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h.append(chunk[0])
                        s.append(chunk[1])
                        v.append(chunk[2])
        
        return (int(np.median(h)), int(np.median(s)), int(np.median(v)))

ColorDetector = ColorDetection()
