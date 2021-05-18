#!/usr/bin/env python
# encoding: utf-8
"""
@author: H
@software: Pycharm
@file: ImageInterpolation1.py
@time: 2020/10/17 20:31
"""

import os
import numpy as np
from PIL import Image

"""
    图像缩放常见三种方法的实现：
        - 最近邻插值法
        - 双线性插值法
        - 双立方插值法
"""


def Interpolation_NNI(filepath):
    """
        最近邻插值法(nearest neighbor interpolation)
    :param filepath:
    :return:
    """
    img = Image.open(file_path)  # 读取图片，格式为Image
    # img.show()  # 显示图片

    # 把Image格式的图片转化为numpy格式进性图像处理
    img = np.array(img, dtype=np.uint8)

    height, width, mode = img.shape[0], img.shape[1], img.shape[2]  # 取出高、宽、通道数
    print(height, width, mode)  # (275 183 3)

    # 缩放的目标大小，这里以缩放为原图的1/2为例
    desWidth = int(width * 0.5)
    desHeight = int(height * 0.5)
    desImage = np.zeros((desHeight, desWidth, mode), np.uint8)  # 定义一个目标图片代表的array，纯黑图片

    # 像素填充
    # 方法1：最近邻插值法
    for des_x in range(0, desHeight):
        for des_y in range(0, desWidth):
            # 判断新像素点在原图中的像素点坐标
            src_x = int(des_x * (height / desHeight))
            src_y = int(des_y * (width / desWidth))
            desImage[des_x, des_y] = img[src_x, src_y]  # 填充
    print(desImage.shape)
    des_img = Image.fromarray(desImage)
    des_img.save("D:/Desktop/数值分析/图片/BilinearInterpolation1.png")


def Interpolation_Bilinear(filepath, desHeight, desWidth):
    # 双线性插值法
    img = Image.open(filepath)  # 读取图片
    img = np.array(img, np.uint8)  # 转化为numpy数组
    desImageNumpy = np.zeros(img.shape, np.uint8)  # 生成一个大小相同的全0的numpy数组
    height, width, mode = img.shape[0], img.shape[1], img.shape[2]  # 高、宽、channel数

    # 找出目标位置在源图中的位置
    scale_x = float(width) / desWidth  # x轴缩放比例
    scale_y = float(height) / desHeight  # y轴缩放比例
    des_image = np.zeros((desHeight, desWidth, mode), np.uint8)
    for n in range(mode):
        for des_y in range(desHeight):
            for des_x in range(desWidth):
                # 确定四个近邻点坐标
                src_x = (des_x + 0.5) * scale_x - 0.5  #
                src_y = (des_y + 0.5) * scale_y - 0.5

                src_x_1 = int(np.floor(src_x))  #
                src_y_1 = int(np.floor(src_y))
                src_x_2 = min(src_x_1 + 1, width - 1)  # 防止坐标点寻找溢出
                src_y_2 = min(src_y_1 + 1, height - 1)
                # 两次x轴线性插值
                value_1 = (src_x_2 - src_x) * img[src_y_1, src_x_1, n] + (src_x - src_x_1) * img[src_y_1, src_x_2, n]
                value_2 = (src_x_2 - src_x) * img[src_y_2, src_x_1, n] + (src_x - src_x_1) * img[src_y_2, src_x_2, n]
                # y轴线性插值
                des_image[des_y, des_x, n] = (src_y_2 - src_y) * value_1 + (src_y - src_y_1) * value_2
    print(des_image.shape)
    des_img = Image.fromarray(des_image)
    des_img.save("D:/Desktop/数值分析/图片/BilinearInterpolation2.png")


if __name__ == '__main__':
    file_path = r"D:/Desktop/数值分析/图片/source.jpeg"
    Interpolation_Bilinear(file_path, int(183 * 2), int(275 * 2))  # 双线性插值法
