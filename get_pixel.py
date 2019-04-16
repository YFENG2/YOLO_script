from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import os
path = "/home/feng/darknet/data/cele_A/ac/img_celeba/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称


s = [[],[],[]]
count = 0
for file in files:
    s[0].append(file)
    img=Image.open(path + file)
    s[1].append(img.size[0])
    s[2].append(img.size[1])
    count+=1
    print(count)
s1 = np.array(s)
s2 = s1.T
s3 = s2[s2[:,0].argsort()]
np.savetxt('_weight11.txt',s3,fmt='%s')
