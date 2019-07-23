# coding: utf-8
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random

from PIL import Image
img = Image.open('../org_image/fengjing.jpg').convert("RGB")

def salt_pepper(img, SNR):
    img_ = img.copy()
    c, h, w = img_.shape
    mask = np.random.choice((0, 1, 2), size=(1, h, w), p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    mask = np.repeat(mask, c, axis=0)     # 按channel 复制到 与img具有相同的shape
    img_[mask == 1] = 255    # 盐噪声
    img_[mask == 2] = 0      # 椒噪声

    return img_

def add_salt_pepper(img):
    SNR = random.uniform(0.9,1.0)
    img = np.array(img)
    img_s = salt_pepper(img.transpose(2, 1, 0), SNR)
    img_s = img_s.transpose(2, 1, 0)
    img_s = Image.fromarray(img_s, mode='RGB')

    return img_s

img_s = add_salt_pepper(img)
img_s.save("./salt_pepper.jpg")
plt.imshow(img_s)
plt.show()
