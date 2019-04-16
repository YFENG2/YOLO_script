#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 1 to 2 files, 1:0.1
import os
import random
import shutil
from shutil import copy2
trainfiles = os.listdir('/home/feng/darknet/data/cele_A/ac/img_celeba') # （图片文件夹）
num_train = len(trainfiles)
print( "num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)
num = 0
trainDir = '/home/feng/darknet/data/cele_A/ac/train/' #（将图片文件夹中的7份放在这个文件夹下）
validDir = '/home/feng/darknet/data/cele_A/ac/valid/' #（将图片文件夹中的3份放在这个文件夹下）
for i in index_list:
    fileName = os.path.join('/home/feng/darknet/data/cele_A/ac/img_celeba', trainfiles[i])
    if num < num_train*0.1:
        print(str(fileName))
        copy2(fileName, trainDir)
    else:
        copy2(fileName, validDir)
    num += 1
 
 
 
 
 
 
 
 
 
 
 
 
 
 
