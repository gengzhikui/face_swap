# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np

def get_filenames_from_path(path):
    from os import walk
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    return f


def face_beauty(src_image_path, dst_image_path, value):
	print(src_image_path, dst_image_path, value)
	# 1 加载一张图片
	image_origin = cv2.imread(src_image_path)

	# 根据图片的尺寸，等比例缩放图片
	size = image_origin.shape
	print(size)

	# 缩小倍数
	mini_num = 1
	image_resize = cv2.resize(image_origin, (int(size[1] / mini_num), int(size[0] / mini_num)),
	                          interpolation=cv2.INTER_CUBIC)


	# bilateralFilter—图像双边滤波
	# 函数原型：bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
	# src：图像矩阵
	# d：邻域直径
	# sigmaColor：颜色标准差
	# sigmaSpace：空间标准差
	# value值越大美颜的程度越大
	image_beauty = cv2.bilateralFilter(image_resize, value, value * 2, value / 2)


	# 生成图片
	cv2.imwrite(dst_image_path, image_beauty)

	"""
	merged_img = np.hstack([image_resize, image_beauty])
	cv2.imwrite(dst_image_path+"_vs", merged_img)

	# 创建一个窗口
	cv2.namedWindow('image')

	# 将两张图片的元组叠加在一起
	merged_img = np.hstack([image_resize, image_beauty])

	# 展示窗口
	cv2.imshow('image', merged_img)

	# 窗口等待
	cv2.waitKey(0)

	# 销毁窗口e
	cv2.destroyAllWindows()
	"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="image_path")
    parser.add_argument("beauty_value", help="0-50")
    args = parser.parse_args()
    
    image_file_names = get_filenames_from_path(args.image_path)
    for image_file_name in image_file_names:
        if (".jp" in image_file_name) and (".txt" not in image_file_name):
            image_file_name = args.image_path + "/" + image_file_name
            face_beauty(image_file_name, image_file_name, int(args.beauty_value))

