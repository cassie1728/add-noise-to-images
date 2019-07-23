import numpy as np
import cv2
from numpy import shape
import random
from matplotlib import pyplot as plt
from random import randint

from PIL import Image
img = Image.open('fengjing.jpg').convert("RGB")

def gauss_noise(image):
    image = np.array(image)
    image = np.array(image/255, dtype=float)
    var = random.uniform(0.001,0.01)
    noise = np.random.normal(0, var ** 0.5, image.shape)
    out = image + noise
    out = np.clip(out, 0, 1.0)
    out = np.uint8(out*255)
    out = Image.fromarray(out, mode='RGB')
    return out

a = gauss_noise(img)
a.save('./gauss2.jpg')
plt.imshow(a)
plt.show()
