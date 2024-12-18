import PIL
import PIL.ImageGrab
import cv2
import easyocr
import time

import numpy as np
import pygsheets
import sys

import os
import gui


font = ("VT323", 24)



bottomline = ""
topline = ""
client = pygsheets.authorize(service_file="screensuckerlethal-633f15c2da18.json")
sh = client.open_by_url(gui.spreadsheet_link)
wks = sh.sheet1

day = int(gui.day)

multiplier_x = round(int(gui.resx) / 1920, 3)
multiplier_y = round(int(gui.resy) / 1080, 3)

print(multiplier_x)

bbox1 = (800 * multiplier_x, 791 * multiplier_y, 920 * multiplier_x, 838 * multiplier_y)
bbox2 = (800 * multiplier_x, 851 * multiplier_y, 920 * multiplier_x, 891 * multiplier_y)
singlebbox = (814 * multiplier_x, 669 * multiplier_y, 815 * multiplier_x, 670 * multiplier_y)

minred = np.array([6, 100, 100])
maxred = np.array([6, 255, 255])

reader = easyocr.Reader(['en'])

while True:
    prev_topline = 0
    prev_bottomline = 0

    single_pixel = PIL.ImageGrab.grab(singlebbox)
    single_pixel.save("SinglePixel.png")

    single_pixel = cv2.imread("SinglePixel.png")
    single_pixel_hsv = cv2.cvtColor(single_pixel, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(single_pixel_hsv, minred, maxred)
    if cv2.countNonZero(mask) > 0:

        topline_img = PIL.ImageGrab.grab(bbox1)
        bottomline_img = PIL.ImageGrab.grab(bbox2)
        topline_img.save("topline.png")
        bottomline_img.save("bottomline.png")

        toplinePath = "topline.png"
        bottomlinePath = "bottomline.png"

        img = cv2.imread(toplinePath)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img_hsv, minred, maxred)
        mask = cv2.bitwise_not(mask)
        mask = cv2.GaussianBlur(mask, (3, 3), 1)

        cv2.imwrite("toplineMask.png", mask)
        topline_text = reader.readtext(mask)

        img = cv2.imread(bottomlinePath)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img_hsv, minred, maxred)
        mask = cv2.bitwise_not(mask)
        mask = cv2.GaussianBlur(mask, (3, 3), 1)

        bottomline_text = reader.readtext(mask)


        if not bottomline_text == []:
             if bottomline_text[0][1].isdigit():
                prev_bottomline = bottomline
                bottomline = bottomline_text[0][1]






        if not topline_text == []:
             if topline_text[0][1].isdigit():
                prev_topline = topline

                topline = topline_text[0][1]

                if not prev_topline == topline:

                    wks.update_value("k" + str(2 + day), topline)
                    print(topline)
                    wks.update_value("l" + str(2 + day), bottomline)
                    print(bottomline)
                    day += 1


