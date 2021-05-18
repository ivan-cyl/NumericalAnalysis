from PIL import Image
import numpy as np

# 最近邻插值算法
# dstH为新图的高;dstW为新图的宽
def NearestNeighbourInterpolate(img,dstH,dstW):
    scrH,scrW,_=img.shape
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH-1):
        for j in range(dstW-1):
            scrx=round(i*(scrH/dstH))
            scry=round(j*(scrW/dstW))
            retimg[i,j]=img[scrx,scry]
    return retimg


def nearest(image, target_size):
    """
    Nearest Neighbour interpolate for RGB  image

    :param image: rgb image
    :param target_size: tuple = (height, width)
    :return: None
    """
    if target_size[0] < image.shape[0] or target_size[1] < image.shape[1]:
        raise ValueError("target image must bigger than input image")
    # 1：按照尺寸创建目标图像
    target_image = np.zeros(shape=(*target_size, 3))
    # 2:计算height和width的缩放因子
    alpha_h = target_size[0] / image.shape[0]
    alpha_w = target_size[1] / image.shape[1]

    for tar_x in range(target_image.shape[0] - 1):
        for tar_y in range(target_image.shape[1] - 1):
            # 3:计算目标图像人任一像素点
            # target_image[tar_x,tar_y]需要从原始图像
            # 的哪个确定的像素点image[src_x, xrc_y]取值
            # 也就是计算坐标的映射关系
            src_x = round(tar_x / alpha_h)
            src_y = round(tar_y / alpha_w)

            # 4：对目标图像的任一像素点赋值
            target_image[tar_x, tar_y] = image[src_x, src_y]

    return target_image

if __name__ == '__main__':
    im_path = "D:/Desktop/数值分析/图片/4.jpg"
    image = np.array(Image.open(im_path))

    #image1 = NearestNeighbourInterpolate(image, image.shape[0] * 10, image.shape[1] * 10)
    image1=nearest(image,(image.shape[0] * 2, image.shape[1] * 2))
    image1 = Image.fromarray(image1.astype('uint8')).convert('RGB')
    image1.save("D:/Desktop/数值分析/图片/NearestNeighbourInterpolate4.png")

