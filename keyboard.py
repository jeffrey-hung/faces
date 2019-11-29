#!/usr/bin/python3

import cv2
import numpy as np

# size of keyboard height, width, channel (for color)
keyboard = np.zeros((1000,1500,3), np.uint8) 

# Draw keys

x = 0
y = 0
width = 200
height = 200
thickness = 3

#draw square accounting for border size of line
cv2.rectangle(keyboard,(x+thickness,y+thickness), (x+width-thickness,y+height - thickness), (255,0,0), thickness)

# Text Settings
font_letter = cv2.FONT_HERSEHY_PLAIN
text = "A"
font_scale = 10
font_thickness = 4
text_size = cv2.getTextSize(, font_letter, font_scale, font_thickness)
width_text, height_text = text_size[0]

# put A in square
cv2.putText(keyboard, text, (20,100), font_letter, font_scale, (255,0,0), font_thickness)

cv2.imshow("keyboard", keyboard)
cv2.waitKey(0)
cv2.destoryAllWindows()
