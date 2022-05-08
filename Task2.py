#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:43:40 2022

@author: tahaelmoudden
"""
import os
import glob
from PIL import Image
import pillow_heif
import cv2 as cv


# All comand line are in a single loop in order to gain efficacity
# But  first we need to import our data, by defining our directory

path = input('Path of your image -->   ') + "/*"
path_exp = input('Path to export -->   ')
extension_to_save = "." + input("What is the extension you would like to use (without the point)-->   ")
list_of_file = sorted(glob.glob(path))
size = len(list_of_file) # If we were working only in a file type I won't use the index
#of our file, but since i'm managing multiple list at the same time, having the index 
#of the wanted file are an advantage.
name_list = []
n_path_list =[]

for i in range (size):
    name = os.path.basename(list_of_file[i])
    name_list.append(name)
    r_file = pillow_heif.read_heif(list_of_file[i])
    image = Image.frombytes(r_file.mode,r_file.size,r_file.data,"raw",)
    new_path = os.path.join(path_exp,name+extension_to_save)
    image.save(new_path, format="png")
    reading = cv.imread(new_path)
    reading = cv.cvtColor(reading, cv.COLOR_BGR2GRAY)
    (T,reading) = cv.threshold(reading, 65,255, cv.THRESH_BINARY)
    cnts = cv.findContours(reading, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)[-2]
    cv.drawContours(reading, cnts, -1, (0,255,0), 3)
    s1 = 3500
    s2 = 20000
    xcnts = []
    for cnt in cnts:
        if s1<cv.contourArea(cnt) <s2:
            xcnts.append(cnt)
    print (len(xcnts))
    cv.imwrite(new_path,reading)
    
