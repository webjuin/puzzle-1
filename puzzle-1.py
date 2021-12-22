# puzzle 이미지로 동영상 만들기

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random


file = './test-7.jpg'
img = cv2.imread(file)

Mw = 1920 #1024
Mh = 1200 #768
img = cv2.resize(img, dsize=(Mw, Mh))
h, w, c = img.shape

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 26
out = cv2.VideoWriter('output-7.mp4', fourcc, fps, (Mw, Mh))

img_1 = np.zeros((h, w, c))
img_res = np.zeros((Mh, Mw, 3))
sss = [32]

for ss in sss:
    pp = []
    sh = int(Mh/ss)
    sw = int(Mw/ss)
    print(sh, sw)
    for w in range(1, ss+1):
        for h in range(1, ss+1):
            tt = np.array(img[(h-1)*sh:h*sh, (w-1)*sw:w*sw, :])
            pp.append(tt)
    #print(len(pp))
    
    #while True:
    for k in range(0, fps*100):
        i = random.randrange(0, ss**2)
        img_1 = pp[i:(i+1)][0]
        
        #print(img_1.shape)
        j = random.randrange(0, ss**2)
        c = int(j/ss)
        r = j%ss
        
        #print(c, r)
        img_res[sh*(c):sh*(c+1), sw*(r):sw*(r+1), :] = img_1

        img_2 = np.array(img_res, dtype=np.uint8)
        
        cv2.imshow('img_1', img_1)
        cv2.imshow('img_2', img_2)
        cv2.waitKey(int(1000/fps))
        
        out.write(img_2)

out.release()
cv2.destroyAllWindows()
