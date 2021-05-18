from PIL import Image
import numpy as np
import math

def nearest(image, target_size):
    if target_size[0] < image.shape[0] or target_size[1] < image.shape[1]:
        raise ValueError("target image must bigger than input image")
    target_image = np.zeros(shape=(*target_size, 3))

    alpha_h = target_size[0] / image.shape[0]
    alpha_w = target_size[1] / image.shape[1]

    for tar_x in range(target_image.shape[0] - 1):
        for tar_y in range(target_image.shape[1] - 1):
            src_x = round(tar_x / alpha_h)
            src_y = round(tar_y / alpha_w)

            target_image[tar_x, tar_y] = image[src_x, src_y]

    return target_image
#最近邻域插值法
def BiLinear_interpolation(img, dstH, dstW):
    scrH, scrW, _ = img.shape
    img = np.pad(img, ((0, 1), (0, 1), (0, 0)), 'constant')
    retimg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx = (i + 1) * (scrH / dstH) - 1
            scry = (j + 1) * (scrW / dstW) - 1
            x = math.floor(scrx)
            y = math.floor(scry)
            u = scrx - x
            v = scry - y
            retimg[i, j] = (1 - u) * (1 - v) * img[x, y] + u * (1 - v) * img[x + 1, y] + (1 - u) * v * img[
                x, y + 1] + u * v * img[x + 1, y + 1]
    return retimg
#双线性插值法
def BiBubic(x):
    x = abs(x)
    if x <= 1:
        return 1 - 2 * (x ** 2) + (x ** 3)
    elif x < 2:
        return 4 - 8 * x + 5 * (x ** 2) - (x ** 3)
    else:
        return 0
#BiCubic基函数
def BiCubic_interpolation(img, dstH, dstW):
    scrH, scrW, _ = img.shape
    retimg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx = i * (scrH / dstH)
            scry = j * (scrW / dstW)
            x = math.floor(scrx)
            y = math.floor(scry)
            u = scrx - x
            v = scry - y
            tmp = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if x + ii < 0 or y + jj < 0 or x + ii >= scrH or y + jj >= scrW:
                        continue
                    tmp += img[x + ii, y + jj] * BiBubic(ii - u) * BiBubic(jj - v)
            retimg[i, j] = np.clip(tmp, 0, 255)
    return retimg
#双三次插值

if __name__ == '__main__':
    im_path = "D:/Desktop/数值分析/图片/source.jpeg"
    image = np.array(Image.open(im_path))

    image1 = nearest(image, (image.shape[0] * 2, image.shape[1] * 2))
    image1 = Image.fromarray(image1.astype('uint8')).convert('RGB')
    image1.save("D:/Desktop/数值分析/图片/NearestNeighbourInterpolate3.png")

    image2 = BiLinear_interpolation(image, image.shape[0] * 2, image.shape[1] * 2)
    image2 = Image.fromarray(image2.astype('uint8')).convert('RGB')
    image2.save("D:/Desktop/数值分析/图片/BilinearInterpolation.png")

    image3 = BiCubic_interpolation(image, image.shape[0] * 2, image.shape[1] * 2)
    image3 = Image.fromarray(image2.astype('uint8')).convert('RGB')
    image3.save("D:/Desktop/数值分析/图片/BiCubicInterpolation.png")
