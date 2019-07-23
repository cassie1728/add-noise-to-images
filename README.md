# add-noise-to-images
add Guass Noise and Salt And Pepper Noise to images

### 1. 在图像中加入椒盐噪声

运行SaltandPepper.py<br>

原图：<br>
![](https://github.com/cassie1728/add-noise-to-images/raw/master/org_image/fengjing.jpg)
<br>
结果图：<br>
![](https://github.com/cassie1728/add-noise-to-images/raw/master/SaltandPepper/salt_pepper.jpg)
<br>

### 1. 在图像中加入高斯噪声

gauss.py使用两个循环来实现图中像素点的遍历，缺点，速度很慢，时间很长。<br>

gauss2.py使用矩阵相加实现，速度很快。<br>

#### 注意：<br>

gauss.py 使用 `random.gauss(0,sigma)` 生成服从高斯分布的数字，但是只能生成一个数。<br>

gauss2.py 使用 `np.random.normal(0, var ** 0.5, image.shape)` 生成正态分布随机数，可设定生成尺寸（设置图片尺寸）<br>

结果图：<br>

![](https://github.com/cassie1728/add-noise-to-images/raw/master/gauss/gauss2.jpg)
<br>
<br>
continue to learn
