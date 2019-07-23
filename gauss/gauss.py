#随机生成符合正态（高斯）分布的随机数，means,sigma为两个参数
import numpy as np
import cv2
from numpy import shape
import random
from matplotlib import pyplot as plt
from random import randint

from PIL import Image
img = Image.open('../org_image/fengjing.jpg').convert("RGB")

def Gauss_noise(img):
    img = np.array(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sigma = randint(4,36)  #可以调节方差范围
            g=random.gauss(0,sigma)
            r1=np.where((g+img[i,j])>255,255,(g+img[i,j]))
            r2=np.where(r1<0,0,r1)
            img[i,j]=np.round(r2)
    img_s = Image.fromarray(img, mode='RGB')
    return img_s

a = Gauss_noise(img)
a.save('./gauss.jpg')
plt.imshow(a)
plt.show()
