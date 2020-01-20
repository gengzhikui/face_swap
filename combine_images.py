# -*- coding: utf-8 -*-

import argparse
import sys
import time
from PIL import Image


def get_filenames_from_path(path):
    from os import walk
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    return f
    
def combine_images(src_image_dir, dst_image_path, background_image_path, cols = 3, base_width=600, base_height=800, margin=10):
    # 1. read images
    filenames = get_filenames_from_path(src_image_dir)
    src_image_path_list = []    
    for filename in filenames:
        src_image_path_list.append(src_image_dir + "/" + filename)
    raw_images = [Image.open(x) for x in src_image_path_list]
    
    # 2. calc rows/cols/total_width/total_height
    image_num = len(raw_images)
    rows = int(image_num/cols)
    if image_num % cols != 0:
        rows += 1
    total_width = (base_width+margin)*cols + margin
    total_height = (base_height+margin)*rows + margin
    print(rows, cols)

    # 3. resize images
    resize_images = []
    for img in raw_images:
        img.thumbnail((base_width, base_height), Image.ANTIALIAS)
        resize_images.append(img)
    
    # 4. create background images
    background_img = Image.open(background_image_path) # image extension *.png,*.jpg
    background_img = background_img.resize((total_width, total_height), Image.ANTIALIAS)

    # 5. create new image    
    new_im = Image.new('RGB', (total_width, total_height))
    new_im.paste(background_img, (0,0))
    for i in range(0, cols):
        for j in range(0, rows):
            if i*rows+j < image_num:
                im = resize_images[i*rows + j]
                pos_x = i*(base_width+margin) + margin
                pos_y = j*(base_height+margin) + margin
                new_im.paste(im, (pos_x,pos_y))
    new_im.save(dst_image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("src_image_dir", help="images directory to combine")
    parser.add_argument("dst_image_dir", help="images directory to generate")
    parser.add_argument("background_image_path", help="background_image_path")
    parser.add_argument("cols", help="cols")
    parser.add_argument("base_width", help="base_width for a single image")
    parser.add_argument("base_height", help="base_height for a single image")
    parser.add_argument("margin", help="margin space")
    args = parser.parse_args()
    dst_image_path = args.dst_image_dir + "/combine_" + str(int(time.time() * 1000)) + '.jpg'

    combine_images(args.src_image_dir, dst_image_path, args.background_image_path, int(args.cols), int(args.base_width), int(args.base_height), int(args.margin))
