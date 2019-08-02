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

# 注意!!!

实践时发现一个错误。

python3 下 运行gauss2.py没有问题，但是在python2环境下运行会发生异常，产生下图所示图片。
![](https://github.com/cassie1728/add-noise-to-images/raw/master/gauss/1.png)

经过排查，发现是在做除法时，python2和python3不一致产生的bug……
```
    image = np.array(image)
    image = np.array(image/255, dtype=float) //python
```
python2中两个整数相除，会自动四舍五入保存为整数。所以0.2什么的都变成0了，就全是黑的了……

解决办法是，把分子转换为float，再做除法，即可得到float。

```
    image = np.array(image, dtype=float)
    image = np.array(image/255, dtype=float) //python
```

## 细节决定成败啊朋友们！
